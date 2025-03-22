Behavior_Question_Guideline = \
"""In this annotation task, you will evaluate whether the character's response conflicts with the behavioral style described in the character profile (including but not limited to language style and response manner) based on the character setting, user query, and character responses. The specific scoring criteria are as follows:
1 point: The character's response conflicts with the language style described in the character profile.
2 points: The character's response does not conflict with the style, reflects some aspects of the language style, but the response has issues such as grammatical errors, generation errors, incoherence, or is too short. (As long as there are grammatical errors, generation errors, incoherence, or the response is too short, the maximum score is 2 points)
3 points: The character's response does not conflict with the character description/reference behavior information, but it does not particularly reflect the information in the character description. (Intuitively, the response seems fine, but on closer inspection, there is no concrete evidence to support it. Score 3)
4 points: The response is informative, the dialogue is sufficiently long and problem-free, the character's response has no quality issues, and it fits the language style described in the behavior information well (excellent performance)
5 points: The response is informative, the dialogue is sufficiently long and problem-free, the character's response has no quality issues, and it reflects the language style described in the behavior information very well, using sophisticated methods such as actions and expressions from the supplementary information, rhetorical devices, etc., to convey the style (outstanding match)."""




Behavior_Question_Judge_Prompt_Reference = \
"""Please act as an impartial judge and complete the task according to the following requirements.

[Task Requirements]
In this annotation task, you will evaluate whether the character's response conflicts with the behavioral style described in the character profile (including but not limited to language style and response manner) based on the character setting, user query, and character responses. Below is a reference for the character's behavioral style from the character description. The specific scoring criteria are as follows:
1 point: The character's response conflicts with the language style described in the character profile.
2 points: The character's response does not conflict with the style but does not particularly reflect the information in the character description.
3 points: The response is informative, the dialogue is sufficiently long and problem-free, the character's response has no quality issues, and it fits the language style described in the behavior information well (excellent performance)
4 points: The response is informative, the dialogue is sufficiently long and problem-free, the character's response has no quality issues, and it reflects the language style described in the behavior information very well, using sophisticated methods such as actions and expressions from the supplementary information, rhetorical devices, etc., to convey the style (outstanding match).

[Character Profile]
{character_profile}

[Reference Behavioral Style]
{reference}

[Multi-turn Dialogue]
{dialogue}

[User Query]
{user_query}

[Character Response]
{character_response}"""