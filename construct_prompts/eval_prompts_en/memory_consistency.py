Memory_Guideline = \
"""### Task Description
Given the character profile, user query, and corresponding character response, your task is to evaluate whether the character's response correctly addressed the user's utterance. Ensure that the character's response is consistent with the user's utterance in terms of semantics or information.
Note, this task only considers the user's utterance, not the character profile, and do not consider your real-world knowledge, only reference the user's utterance.
"Inconsistent" means every word must be the same; otherwise, it is not considered consistent.

### Output Requirements
In JSON format, first output the correct dialogue round in the explanation, then analyze the scores one by one, and finally output the score in the score.

### Score Description
(1) 1 point: If the character's response is inconsistent with the information in the dialogue context, even if some information is correct, as long as part of it is wrong or inconsistent, it should be rated 1 point because this shows a direct contradiction in the information.
(2) 2 points: The character's response does not directly answer the user's utterance, i.e., off-topic, and the character's response shows illogical and unnatural flow with the user's utterance.
(3) 3 points: The character's response does not answer the user's utterance, but it is logically coherent.
(4) 4 points: The character's response correctly covers part of the information mentioned in the character dialogue, different wording, or does not fully cover all relevant information, or only answers part of the question.
(5) 5 points: The character's response is fully consistent with the answers given in the multi-turn dialogue and covers all the answers given in the multi-turn dialogue.
"""


Memory_Judge_Prompt_Reference = \
"""Please act as an impartial judge and complete the task according to the following requirements.

[Task Requirements]
Given the character profile, user query, and corresponding character response, and also given the multi-turn dialogue fragment as a reference, your judgment criteria are as follows:
(1) 1 point: If the character's response is inconsistent with the information in the dialogue context, even if some information is correct, as long as part of it is wrong or inconsistent, it should be rated 1 point because this shows a direct contradiction in the information.
(2) 2 points: The character's response does not directly answer the user's utterance, i.e., off-topic.
(3) 3 points: The character's response correctly covers part of the information mentioned in the character dialogue, different wording, or does not fully cover all relevant information, or only answers part of the question.
(4) 4 points: The character's response is fully consistent with the answers given in the multi-turn dialogue and covers all the answers given in the multi-turn dialogue.

[Character Profile]
{character_profile}

[Multi-turn Dialogue]
{dialogue}

[User Query]
{user_query}

[Character Response]
{character_response}

[Reference Multi-turn Dialogue Fragment]
{reference}"""