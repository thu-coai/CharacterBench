import json
import os
import argparse
from tqdm import tqdm
from copy import deepcopy
import httpx
from concurrent.futures import ThreadPoolExecutor
import threading
from transformers import AutoModelForCausalLM, AutoTokenizer
from vllm import LLM, SamplingParams

model_path = "COAI/CharacterJudge"

tokenizer = AutoTokenizer.from_pretrained(model_path)

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype="auto",
    device_map="auto"
)

def read_data(path):
    with open(path, "r", encoding='utf-8') as f:
        _data = json.load(f)

    data = []
    for i, d in enumerate(_data):
        data.append({
            "id": i,
            "input": d['instruction'],
            "output": d['output'],
        })
    data = sorted(data, key=lambda x:len(x["input"]))
    return data

def model_generate(payload):
    text = tokenizer.apply_chat_template(
        payload['messages'],
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=payload["max_tokens"]
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return response


def create_payload(datas, save_path):
    payloads = []
    exists_datas = []
    # 读取已经存在的数据，避免重复请求
    if os.path.exists(save_path):
        with open(save_path, 'r', encoding='utf-8') as file:
            for line in file:
                exists_datas.append(json.loads(line)['id'])
    for data in datas:
        payload = {
            "model": "CharacterJudge",
            "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": data["input"]}],
            "max_tokens": 512,
            "temperature": 0
        }
        if data['id'] in exists_datas:
            continue
        payloads.append([payload, data, save_path])
    return payloads


def process_payload(payload, data, save_path):
    max_retry_count = 3
    retry_counts = 0
    while True:
        try:
            response = model_generate(payload)
            data['generated'] = response
            break
        except Exception as e:
            retry_counts += 1
            print(f'Request failed: {e}, retrying...{retry_counts}')
            if retry_counts > max_retry_count:
                break

    if retry_counts > max_retry_count:
        return
    # 调用成功，将结果追加写入文件
    with lock:
        with open(save_path, 'a', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)
            file.write('\n')


def process_payload_with_progress(payload, pbar):
    process_payload(*payload)
    pbar.update(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, default="eval_data/evaluation_data_en")
    parser.add_argument('--output_path', type=str, default="results")
    args = parser.parse_args()

    if not os.path.exists(args.output_path):
        os.makedirs(args.output_path)

    lock = threading.Lock()

    files = os.listdir(args.input_path)
    for file in files:
        datas = read_data(os.path.join(args.input_path, file))
        print(f"{file} Generate Begin!")
        print(len(datas))
        payloads = create_payload(datas, os.path.join(args.output_path, file))
        with ThreadPoolExecutor(max_workers=8) as executor:
            with tqdm(total=len(payloads), desc="Processing payloads") as pbar:
                futures = [executor.submit(process_payload_with_progress, payload, pbar) for payload in payloads]
                for future in futures:
                    future.result()
