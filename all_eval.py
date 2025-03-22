import json
import os
import argparse
import numpy as np
import re
from scipy.stats import spearmanr, kendalltau

def count_numbers(numbers):
    count_dict = {}

    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1

    return dict(sorted(count_dict.items()))


def check(generated):
    if "\n" in generated:
        return generated.split("\n")[0]

    try:
        return float(generated)
    except:
        return 3.0


def extract_score(generated):
    generated = generated.split("\n")[0]
    pattern = r'评分：(\d+(\.\d{1,3})?)'
    match = re.search(pattern, generated)
    if match:
        return match.group(1)
    else:
        return 2


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--result_path', type=str, default="results/results_gpt3.5turbo_zh/checkpoint-1120")
    parser.add_argument('--output_path', type=str, default="results/results_gpt3.5turbo_zh/checkpoint-1120.json")
    args = parser.parse_args()
    files = os.listdir(args.result_path)
    result = {}
    avg = 0
    for file in files:
        print(file)
        with open(os.path.join(args.result_path, file), 'r', encoding='utf-8') as f:
            data = [json.loads(line) for line in f]

        preds = []
        golds = []

        for d in data:
            d['generated'] = d['generated'].replace(f"Human: {d['input']}\nAssistant: ", "")
            d['generated'] = check(d['generated'])
            d['output'] = check(d['output'])
            preds.append(float(d['generated']))
            golds.append(float(d['output']))

        mx = max(golds)
        means = np.mean(preds)
        model_name = file.split("_")[0]
        result[file.split(".json")[0].replace(model_name + "_", "")] = means / mx * 5
        avg += means / mx * 5

    result['average'] = avg / len(files)
    keys = ["average", "memory_consistency_test", "fact_accuracy_test", "boundary_consistency_test", "attribute_consistency_bot_test", "attribute_consistency_human_test", "behavior_consistency_bot_test", "behavior_consistency_human_test", "emotion_self_regulation_test", "empathetic_responsiveness_test", "morality_stability_test", "morality_robustness_test", "human_likeness_test", "engagement_test"]

    outs = {}
    print(keys)
    for key in keys:
        outs[key] = result[key]
    print(outs)

    with open(args.output_path, "w") as f:
        json.dump(outs, f, ensure_ascii=False, indent=4)
