import re
import os
from typing import Optional, List, Union, Literal
import json
from pydantic import BaseModel
from gpt_call import *
from roleplay_prompt import *
import argparse

class Message(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str


class Session(BaseModel):
    dialogue_setting: dict
    messages: List[Message]


def replace_multiple_ln_to_one_ln(text: str) -> str:
    return re.sub(r"\n+", "\n", text)


def norm_session_zh(session):
    messages = []
    for msg in session['dialogue']:
        speaker = msg['speaker']
        if speaker == "user":
            role = "user"
        elif speaker == "character":
            role = "assistant"
        else:
            if speaker == session["user_name"]:
                role = "user"
            elif speaker == session["character_name"]:
                role = "assistant"
            else:
                raise ValueError(f"invalid role = {speaker}")
        messages.append(
            {"role": role, "content": msg['utterance']}
        )
    assert messages
    assert messages[-1]['role'] == "user"

    greeting = session.get('greeting', "")
    if greeting:
        assert messages[0]['role'] == "user"
        messages.insert(0, {"role": "assistant", "content": greeting})

    if (messages[0]["role"] == "assistant"):
        messages.insert(0, {"role": "user", "content": ""})

    dialogue_setting = {
        "user_name": session["user_name"],
        "bot_name": session["character_name"],
        "user_profile": session.get("user_profile", "无"),
        "bot_profile": session["character_profile"]
    }

    return {
        "dialogue_setting": dialogue_setting,
        "messages": messages
    }


def norm_session_en(session):
    session = session['translation_en']
    messages = []
    for msg in session['dialogue']:
        speaker = msg['speaker'].lstrip()
        if speaker == "user" or speaker == 'User':
            role = "user"
        elif speaker == "character" or speaker == 'Character':
            role = "assistant"
        else:
            if speaker == session["user_name"].lstrip():
                role = "user"
            elif speaker == session["character_name"].lstrip() or speaker in session["character_name"].lstrip():
                role = "assistant"
            elif messages and messages[-1]['role'] == "user":
                role = "assistant"
            else:
                raise ValueError(f"invalid role = {speaker}")
        messages.append(
            {"role": role, "content": msg['utterance']}
        )
    assert messages
    # print(messages)
    assert messages[-1]['role'] == "user"

    greeting = session.get('greeting', '')
    if greeting == 'N/A':
        greeting = ''
    # print(greeting)
    if greeting:
        assert messages[0]['role'] == "user"
        messages.insert(0, {"role": "assistant", "content": greeting})

    if (messages[0]["role"] == "assistant"):
        messages.insert(0, {"role": "user", "content": ""})

    dialogue_setting = {
        "user_name": session["user_name"],
        "bot_name": session["character_name"],
        "user_profile": session.get("user_profile", "无"),
        "bot_profile": session["character_profile"]
    }

    return {
        "dialogue_setting": dialogue_setting,
        "messages": messages
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, default="eval_data/raw_data")
    parser.add_argument('--output_path', type=str, default="eval_data/response_data")
    parser.add_argument('--model_name', type=str, default="gpt-4o")
    args = parser.parse_args()
    
    data_directory = args.data_path
    output_directory = args.output_path
    model_name = args.model_name
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(data_directory):
        file_path = os.path.join(data_directory, filename)
        if os.path.exists(os.path.join(output_directory, filename)):
            print(f"skip {filename}")
            continue
        if os.path.isfile(file_path):
            data = json.load(open(file_path, "r", encoding="utf-8"))
            output = []
            for i, session in enumerate(data):
                max_retry = 5
                for retry in range(max_retry):
                    try:
                        session_zh = norm_session_zh(session)
                        session_en = norm_session_en(session)
                        session_model_zh = Session.model_validate(session_zh)
                        session_model_en = Session.model_validate(session_en)
                        prompt_zh = Role_Play_PROMPT_ZH.format(character_profile = session_model_zh.dialogue_setting['bot_profile'], user_profile = session_model_zh.dialogue_setting['user_profile'], dialogue = "\n".join([f"{msg.role}: {msg.content}" for msg in session_model_zh.messages]))
                        prompt_en = Role_Play_PROMPT_EN.format(character_profile = session_model_en.dialogue_setting['bot_profile'], user_profile = session_model_en.dialogue_setting['user_profile'], dialogue = "\n".join([f"{msg.role}: {msg.content}" for msg in session_model_en.messages]))
                        #change the following line to use the model you want to use
                        response_zh = gpt_call(prompt_zh, model_name)
                        response_en = gpt_call(prompt_en, model_name)
                        response_zh = eval(response_zh.replace("```", "").replace("json", "").replace("，",",").replace("。", ".").strip())
                        response_en = eval(response_en.replace("```", "").replace("json", "").replace("，",",").replace("。", ".").strip())
                        print(response_zh)
                        print(response_en)
                        session['response_zh'] = response_zh
                        session['translation_en']['response_en'] = response_en
                        break
                    except Exception as e:
                        print(e)
                        continue
                if retry == max_retry-1:
                    continue
                output.append(session)
            json.dump(output, open(os.path.join(output_directory, filename), "w", encoding="utf-8"), ensure_ascii=False, indent=4)
