Fact_Acc_Guideline = \
"""In this annotation task, you will evaluate whether the character's response correctly addresses the user's query based on the character profile, user query, and character response. The accuracy of the character's response is based on whether it is consistent with the information provided in the character profile in terms of semantics and content. The specific scoring criteria are as follows:

(1) 1 point: The character's response is inconsistent with the answer provided in the character profile, significantly deviates from the answer provided in the character profile, or provides a completely incorrect answer.
(2) 2 points: The character's response does not answer the user's query, i.e., it is irrelevant, and the character's response and the user's query are logically unnatural and incoherent.
(3) 3 points: The character's response does not fully answer or does not answer the user's query, but the character's response and the user's query are logically natural and coherent, demonstrating an appropriate understanding of the conversation context.
(4) 4 points: The character's response correctly covers part of the information mentioned in the character profile but does not fully cover all relevant information.
(5) 5 points: The character's response comprehensively and accurately covers all the information in the character profile and perfectly addresses the user's query."""


Fact_Acc_Judge_Prompt_Reference = \
"""Please act as an impartial judge and complete the task according to the following requirements.

[Task Requirements]
Given the character profile, multi-turn dialogue, user query, and corresponding character response, and the reference answers provided, your judgment criteria are as follows:
(1) 1 point: The character's response is inconsistent with the answer provided in the character profile, significantly deviates from the answer provided in the character profile, or provides a completely incorrect answer.
(2) 2 points: The character's response is not inconsistent with the information in the character profile but does not directly answer the user's query, does not reflect the character profile, or the response contains information not found in the character profile.
(3) 3 points: The character's response correctly covers part of the information mentioned in the character profile but does not fully cover all relevant information.
(4) 4 points: The character's response comprehensively and accurately covers all the information in the character profile and perfectly addresses the user's query.

[Character Profile]
{character_profile}

[Multi-turn Dialogue]
{dialogue}

[User Query]
{user_query}

[Character Response]
{character_response}

[Reference Answer]
{reference}"""