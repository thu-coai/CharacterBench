Human_Likeness_Guideline = \
"""Given the character profile, the multi-turn dialogue between the user and the character, the user's query, and the character's response, your task is to evaluate how human-like the character's response is. The scoring criteria are as follows:
(1) 1 point: The character's response has quality issues, including but not limited to grammatical errors, incoherence.
(2) 2 points: The character's response has no quality issues, but the language style is quite mechanical, meaning it is not very human-like. For example, encyclopedic responses, slogan-like responses, bullet point responses, meaningless detail descriptions, overly formal, etc.
(3) 3 points: Although it is a human response, the language information or non-verbal cues (actions, expressions, emotional changes, or movement changes) do not reflect the character's profile and style at all.
(4) 4 points: It is a human response, the language information accurately reflects the character profile and personality, but non-verbal cues do not clearly reflect the character profile and personality.
(5) 5 points: Definitely a real character's response: both the language information and non-verbal cues (actions, expressions, emotional changes, or movement changes) accurately reflect the character profile and personality.

Scoring Notes:
Your scoring should be strict, any clues of poor human-likeness should result in a lower score."""

Human_Likeness_Judge_Prompt = \
"""Please act as an impartial judge and complete the task according to the following requirements.

[Task Requirements]
Given the character profile, the multi-turn dialogue between the user and the character, the user's query, and the character's response, your task is to evaluate how human-like the character's response is. The scoring criteria are as follows:
(1) 1 point: The character's response has quality issues, including but not limited to grammatical errors, incoherence.
(2) 2 points: The character's response has no quality issues, but the language style is quite mechanical, meaning it is not very human-like. For example, encyclopedic responses, slogan-like responses, bullet point responses, meaningless detail descriptions, overly formal, etc.
(3) 3 points: Although it is a human response, the language information or non-verbal cues (actions, expressions, emotional changes, or movement changes) do not reflect the character's profile and style at all.
(4) 4 points: It is a human response, the language information accurately reflects the character profile and personality, but non-verbal cues do not clearly reflect the character profile and personality.
(5) 5 points: Definitely a real character's response: both the language information and non-verbal cues (actions, expressions, emotional changes, or movement changes) accurately reflect the character profile and personality.

Scoring Notes:
Your scoring should be strict, any clues of poor human-likeness should result in a lower score.

[Character Profile]
{character_profile}

[Multi-turn Dialogue]
{dialogue}

[User Query]
{user_query}

[Character Response]
{character_response}"""

