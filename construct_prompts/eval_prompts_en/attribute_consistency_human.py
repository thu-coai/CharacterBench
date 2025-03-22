

Attribute_Consistency_Guideline = \
"""Given the character profile, user query, and corresponding character responses, your task is to use the character profile as reference information to evaluate whether the given character response correctly answers the user query, i.e., whether the character response is consistent with the answers in the character profile in terms of semantics or content. If the answer in the character response does not appear in the character information, it should not be judged as inconsistent. The scoring standards are as follows:
1 point: The character response is inconsistent with the information provided in the character profile, significantly deviating from the answers provided in the character profile, providing a completely wrong answer, or the user's statement is not coherent. Satisfying any of these conditions results in 1 point.
2 points: The character response does not directly answer the user's question, i.e., the answer is irrelevant, and the response is logically unnatural and not fluent in relation to the user query.
3 points: The character response answers the user query but does not include any information from the character profile or contains information not present in the character profile.
4 points: The character response correctly and directly reflects parts of the character profile, with the information in the response being consistent but not completely covering all relevant information in the character profile.
5 points: The character response fully and accurately covers all the settings in the character profile, perfectly answering the user's statement.
You can only use the character profile as your reference information and cannot use information outside the character profile, guessed, or uncertain information as reference information. Reference information is strictly limited to the character profile."""



Attribute_Consistency_Judge_Prompt_Reference = \
"""Please play the role of an impartial judge and complete the task according to the following requirements.

[Task Requirements]
Given the character profile, user utterance, and corresponding character response, your task is to evaluate whether the character's response correctly answers the user's utterance based on the character profile. If the answer in the character response is not found in the character profile, it should not be judged as inconsistent. The scoring criteria are as follows:
You can only use the character profile as your reference information, not using any inferred or uncertain information beyond the character profile. Reference information is strictly limited to the character profile.
1 point: The character response is inconsistent with the information provided in the character profile, deviates from the profile, conflicts with the profile, provides an incorrect answer, or the user's utterance is incoherent. Any of these conditions result in 1 point.
2 points: The character response is unrelated to the character profile, does not reflect factual information from the character profile, shows no clear association with the character profile, and does not directly answer the user's utterance.
3 points: The character response directly reflects a small portion of the relevant information from the character profile. The information in the character response matches the description in the character profile but covers only a small amount of the profile.
4 points: The character response accurately covers all relevant content from the character profile and perfectly responds to the user's utterance.

[Character Profile]
{character_profile}

[Multi-turn Dialogue]
{dialogue}

[User Utterance]
{user_query}

[Character Response]
{character_response}

[Reference User Information]
{reference}"""