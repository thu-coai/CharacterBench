

Behavior_Style_Transfer_Guideline = \
"""In this annotation task, you will evaluate whether the character's response matches the behavioral style described in the character profile (including but not limited to language style and response manner) based on the character setting, user query, and character responses. The specific scoring criteria are as follows:
1 point: The character's response almost completely fails to reflect the language style described in the behavior information.
2 points: The response reflects some aspects of the language style, overall acceptable but somewhat mediocre.
3 points: The response is informative, the dialogue is sufficiently long and problem-free, the character's response has no quality issues, and it fits the language style described in the behavior information well, even using actions and expressions from the supplementary information, rhetorical devices, etc., to convey the style."""


Behaviour_Style_Transfer_Judge_Prompt_Reference = \
"""Please act as an impartial judge and complete the task according to the following requirements.

[Task Requirements]
In this annotation task, you will evaluate whether the character's response matches the behavioral style described in the character profile (including but not limited to language style and response manner) based on the character setting, user query, and character responses. Below is a reference for the character's behavioral style from the character description. The specific scoring criteria are as follows:
1 point: The character's response almost completely fails to reflect the language style described in the behavior information.
2 points: The response reflects some aspects of the language style, overall acceptable but somewhat mediocre.
3 points: The response is informative, the dialogue is sufficiently long and problem-free, the character's response has no quality issues, and it fits the language style described in the behavior information well, even using actions and expressions from the supplementary information, rhetorical devices, etc., to convey the style.

[Character Profile]
{character_profile}

[Behavioral Style]
{reference}

[Multi-turn Dialogue]
{dialogue}

[User Query]
{user_query}

[Character Response]
{character_response}"""