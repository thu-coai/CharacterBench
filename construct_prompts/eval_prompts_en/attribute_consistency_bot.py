Knowledge_Accuracy_Guideline = \
"""Given the character profile, user query, and corresponding character response, your task is to evaluate whether the character's response correctly answers the user query based on the character profile, i.e., whether the character's response is semantically or contextually consistent with the answers provided in the character profile. If the answer in the character's response does not appear in the character profile, it should not be considered as inconsistent. The scoring criteria are as follows:
You can only use the character profile as your reference answer, you cannot use inferred or potentially uncertain information beyond the character profile as your reference answer. The reference answer is strictly limited to the character profile.
1 point: The character's response is inconsistent with the answers provided in the character profile, significantly deviates from the answers provided in the character profile, or provides a completely incorrect answer.
2 points: The character's response does not directly answer the user query, i.e., off-topic, and the character's response shows illogical and unnatural flow with the user query.
3 points: The character's response answers the user query, but does not contain any identical meaning from the character profile or the answer in the character's response does not appear in the character profile.
4 points: The character's response correctly and directly reflects parts of the settings mentioned in the character profile. The information in the character's response is consistent with the character profile but does not completely cover all relevant information.
5 points: The character's response comprehensively and accurately covers all the settings in the character profile, perfectly responding to the user query."""


Knowledge_Accuracy_Judge_Prompt_Reference = \
"""Please act as an impartial judge and complete the task according to the following requirements.

[Task Requirements]
Given the character profile, user query, and corresponding character response, also providing the reference answer from the character profile, the scoring criteria are as follows:
1 point: The character's response is inconsistent with the answers provided in the character profile, significantly deviates from the answers provided in the character profile, or provides a completely incorrect answer.
2 points: The character's response does not directly answer the user query, i.e., off-topic, and the character's response shows illogical and unnatural flow with the user query.
3 points: The character's response answers the user query, but does not contain any identical meaning from the character profile or the answer in the character's response does not appear in the character profile.
4 points: The character's response correctly and directly reflects parts of the settings mentioned in the character profile. The information in the character's response is consistent with the character profile but does not completely cover all relevant information.
5 points: The character's response comprehensively and accurately covers all the settings in the character profile, perfectly responding to the user query.

[Character Profile]
{character_profile}

[User Query]
{user_query}

[Character Response]
{character_response}

[Reference Answer]
{reference}"""