from eval_prompts_en.attribute_consistency_bot import Knowledge_Accuracy_Guideline, Knowledge_Accuracy_Judge_Prompt_Reference
from eval_prompts_en.morality import Safety_Guideline, Safety_Judge_Prompt
from eval_prompts_en.fact_accuracy import Fact_Acc_Guideline, Fact_Acc_Judge_Prompt_Reference
from eval_prompts_en.engagement import Engagement_Guideline, Engagement_Judge_Prompt
from eval_prompts_en.memory_consistency import Memory_Guideline, Memory_Judge_Prompt_Reference
from eval_prompts_en.behavior_consistency_human import Behavior_Style_Transfer_Guideline, Behaviour_Style_Transfer_Judge_Prompt_Reference
from eval_prompts_en.behavior_consistency_bot import Behavior_Question_Guideline, Behavior_Question_Judge_Prompt_Reference
from eval_prompts_en.attribute_consistency_human import Attribute_Consistency_Guideline, Attribute_Consistency_Judge_Prompt_Reference
from eval_prompts_en.boundary_consistency import Character_Boundry_Guideline, Character_Boundry_Judge_Prompt_Reference
from eval_prompts_en.human_likeness import Human_Likeness_Guideline, Human_Likeness_Judge_Prompt
from eval_prompts_en.empathetic_responsiveness import Emotion_Recognition_Judge_Prompt_Reference
from eval_prompts_en.emotion_self_regulation import Emotion_Self_Awareness_Guideline, Emotion_Self_Awareness_Judge_Prompt_Reference

data_info = {
    "memory_consistency":{
        "eval_guideline": Memory_Guideline,
        "base_eval_prompt": Memory_Judge_Prompt_Reference
    },
    "attribute_consistency_bot":{
        "eval_guideline": Knowledge_Accuracy_Guideline,
        "base_eval_prompt": Knowledge_Accuracy_Judge_Prompt_Reference
    },
    "attribute_consistency_human":{
        "eval_guideline": Attribute_Consistency_Guideline,
        "base_eval_prompt": Attribute_Consistency_Judge_Prompt_Reference
    },
    "behavior_consistency_bot":{
        "eval_guideline": Behavior_Question_Guideline,
        "base_eval_prompt": Behavior_Question_Judge_Prompt_Reference
    },
    "behavior_consistency_human":{
        "eval_guideline": Behavior_Style_Transfer_Guideline,
        "base_eval_prompt": Behaviour_Style_Transfer_Judge_Prompt_Reference
    },
    "boundary_consistency":{
        "eval_guideline": Character_Boundry_Guideline,
        "base_eval_prompt": Character_Boundry_Judge_Prompt_Reference
    },
    "fact_accuracy":{
        "eval_guideline": Fact_Acc_Guideline,
        "base_eval_prompt": Fact_Acc_Judge_Prompt_Reference
    },
    "human_likeness":{
        "eval_guideline": Human_Likeness_Guideline,
        "base_eval_prompt": Human_Likeness_Judge_Prompt
    },
    "engagement":{
        "eval_guideline": Engagement_Guideline,
        "base_eval_prompt": Engagement_Judge_Prompt
    },
    "morality_robustness":{
        "eval_guideline": Safety_Guideline,
        "base_eval_prompt": Safety_Judge_Prompt
    },
    "morality_stability":{
        "eval_guideline": Safety_Guideline,
        "base_eval_prompt": Safety_Judge_Prompt
    },
    "emotion_self_regulation":{
        "eval_guideline": Emotion_Self_Awareness_Guideline,
        "base_eval_prompt": Emotion_Self_Awareness_Judge_Prompt_Reference
    },
    "empathetic_responsiveness":{
        "eval_guideline": "",
        "base_eval_prompt": Emotion_Recognition_Judge_Prompt_Reference
    }
}