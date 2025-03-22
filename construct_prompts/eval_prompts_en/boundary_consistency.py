Character_Boundry_Guideline = \
"""Given the character profile, user query, and corresponding character response, your task is to evaluate whether the given character response has crossed the boundaries of the character's knowledge, common sense, behavior, preferences, etc., as specified in the character profile. The specific scoring criteria are as follows:
1 point: The character response has crossed the boundaries specified in the character profile, clearly deviating from the character's knowledge, common sense, behavior, preferences, etc., or providing a completely out-of-bounds answer.
2 points: The character response is irrelevant, and the response is illogical or incoherent in relation to the user query.
3 points: The character response follows the user query logically and coherently, but it does not reflect the boundary information in the character profile.
4 points: The character response correctly reflects and adheres to the boundary information in the character profile, and it is logical and coherent with the user query."""





Character_Boundry_Judge_Prompt_Reference = \
"""Please act as an impartial judge and complete the task according to the following requirements.

[Task Requirements]
Given the character profile, multi-turn dialogue between characters, user query, and corresponding character response, and provided reference boundaries, the scoring criteria are as follows:
1 point: The character response has crossed the boundaries specified in the character profile, clearly deviating from the character's knowledge, common sense, behavior, preferences, etc., or providing a completely out-of-bounds answer.
2 points: The character response has not crossed the boundaries, but it does not directly answer the user query, or it does not reflect the boundary information in the character profile.
3 points: The character response has not crossed the boundaries and correctly reflects and adheres to the boundary information in the character profile.

[Character Profile]
{character_profile}

[Multi-turn Dialogue]
{dialogue}

[User Query]
{user_query}

[Character Response]
{character_response}

[Reference Boundaries]
{reference}"""