from data_info_zh import data_info
import json
import os
import argparse

def count_numbers(numbers):
    count_dict = {}

    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1

    return dict(sorted(count_dict.items()))


def process(file, data_type):
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    outs = []
    golds = []
    for item in data:

        character_profile = str(item['character_profile'])

        if "response_zh" not in item.keys():
            continue

        dialogue = ""
        speaker = item['character_name']
        for i in range(0, len(item['dialogue']) - 1):
            if i % 2 == 0:
                dialogue += f"用户：{item['dialogue'][i]['utterance']}\n"
            else:
                dialogue += f"{speaker}：{item['dialogue'][i]['utterance']}\n"

        user_response = f"用户：{item['dialogue'][-1]['utterance']}"
        character_response = f"{speaker}：{item['response_zh']}"
        score = str(item['annotation_score'])

        if data_type == "memory_consistency":
            segments = item['messages']['output']['dialogue_segments']
            reference_dialogue = ""
            dialogue = ""
            for s in segments:
                reference_dialogue += f"{speaker}：{s}\n"
            query = data_info['memory_consistency']['base_eval_prompt'].format(character_profile=character_profile, dialogue=dialogue, user_query=user_response, character_response=character_response, reference_dialogue=reference_dialogue)
        elif data_type == "attribute_consistency_bot":
            answer = item['messages']['output']['answer']
            dialogue = ""
            query = data_info['attribute_consistency_bot']['base_eval_prompt'].format(character_profile=character_profile, user_query=user_response, character_response=character_response, answer=answer)
        elif data_type == "attribute_consistency_human":
            reference = item['messages']['reference']
            query = data_info['attribute_consistency_human']['base_eval_prompt'].format(character_profile=character_profile, dialogue=dialogue, user_query=user_response, character_response=character_response, reference=reference)
        elif data_type == "behavior_consistency_bot":
            behavior = item['messages']['output']['reference']
            query = data_info['behavior_consistency_bot']['base_eval_prompt'].format(character_profile=character_profile, dialogue=dialogue, user_query=user_response, character_response=character_response, behavior_style=behavior)
        elif data_type == "behavior_consistency_human":
            behavior = item['response_messages']['character_style']
            query = data_info['behavior_consistency_human']['base_eval_prompt'].format(character_profile=character_profile + behavior, dialogue=dialogue, behavior_style=behavior, user_query=user_response, character_response=character_response)
        elif data_type == "boundary_consistency":
            reference_response = item['response_messages']['reference_response']
            dialogue = ""
            query = data_info['boundary_consistency']['base_eval_prompt'].format(character_profile=character_profile, dialogue=dialogue, user_query=user_response, character_response=character_response, reference_response=reference_response)
        elif data_type == "fact_accuracy":
            answer = item['messages']['output']['answer']
            dialogue = ""
            query = data_info['fact_accuracy']['base_eval_prompt'].format(character_profile=character_profile, dialogue=dialogue, user_query=user_response, character_response=character_response, answer=answer)
        elif data_type == "human_likeness":
            query = data_info['human_likeness']['base_eval_prompt'].format(character_profile=character_profile, dialogue=dialogue, user_query=user_response, character_response=character_response)
        elif data_type == "engagement":
            query = data_info['engagement']['base_eval_prompt'].format(character_profile=character_profile, dialogue=dialogue, user_query=user_response, character_response=character_response)
        elif data_type == "morality_robustness":
            query = data_info['morality_robustness']['base_eval_prompt'].format(character_profile=character_profile, dialogue=dialogue, user_query=user_response, character_response=character_response)
        elif data_type == "morality_stability":
            query = data_info['morality_stability']['base_eval_prompt'].format(character_profile=character_profile, dialogue=dialogue, user_query=user_response, character_response=character_response)
        elif data_type == "emotion_self_regulation":
            emotion = item['messages']['output']['emotion']
            dialogue = ""
            query = data_info['emotion_self_regulation']['base_eval_prompt'].format(character_profile=character_profile, dialogue=dialogue, user_query=user_response, character_response=character_response, emotion=emotion)
        elif data_type == "empathetic_responsiveness":
            emotion = item['messages']['output']['emotion']
            dialogue = ""
            query = data_info['empathetic_responsiveness']['base_eval_prompt'].format(character_profile=character_profile, dialogue=dialogue, user_query=user_response, character_response=character_response, emotion=emotion)
        else:
            print(data_type)

        if item['response_zh'] != "":
            outs.append({
                "instruction" : query,
                "input" : "",
                "output" : score,
                "history" : [],
                "data_type" : file.split("/")[-1].split(".")[0],
            })

        golds.append(score)

    return outs, golds



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, default="../eval_data/response_data")
    parser.add_argument('--output_path', type=str, default="../eval_data/evaluation_data_zh")
    parser.add_argument('--model_name', type=str, default="gpt-4o")
    args = parser.parse_args()
    
    model = args.model_name
    data_path = args.data_path
    output_path = args.output_path
    
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    
    test_file_dict = {
        'fact_accuracy': 'fact_accuracy_test.json',
        'attribute_consistency_bot': 'attribute_consistency_bot_test.json',
        'morality_robustness': 'morality_robustness_test.json',
        'morality_stability': 'morality_stability_test.json',
        'memory_consistency': 'memory_consistency_test.json',
        'emotion_self_regulation': 'emotion_self_regulation_test.json',
        'empathetic_responsiveness': 'empathetic_responsiveness_test.json',
        'engagement': 'engagement_test.json',
        'human_likeness': 'human_likeness_test.json',
        'boundary_consistency': 'boundary_consistency_test.json',
        'behavior_consistency_bot': 'behavior_consistency_bot_test.json',
        'behavior_consistency_human': 'behavior_consistency_human_test.json',
        'attribute_consistency_human': 'attribute_consistency_human_test.json',
    }

    for data_type, file in test_file_dict.items():
        name = file
        data, _ = process(os.path.join(data_path, file), data_type)
        with open(os.path.join(output_path, f"{model}_{name}"), 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
