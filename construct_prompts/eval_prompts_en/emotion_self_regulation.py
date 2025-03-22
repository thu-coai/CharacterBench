Emotion_Self_Awareness_Guideline = \
"""Given the character profile, user query, and corresponding character response, your task is to evaluate whether the character's response accurately inferred the character's own emotions and check if the response aligns with the character profile. The character's response should be scored based on the character's own statements and consistency with the persona described in the character profile. Please rate according to the following standards:
1 point: The character's response does not match the character's own emotions in this round of dialogue or contradicts the persona described in the character profile.
2 points: The character's response fails to effectively answer the user's question, or does not reflect the character's own description in the character profile, such as answering off-topic.
3 points: The character's response answers the user's question but does not infer or express the character's own emotions, or the response does not directly answer the user's question but closely aligns with the relevant persona.
4 points: The character's response accurately expresses the character's own emotions but does not fully conform to the description in the character profile.
5 points: The character's response not only accurately infers the character's own emotions but also perfectly aligns with the persona described in the character profile.

Scoring Notes:
You are very strict and will not give high scores easily.
Emotion Recognition: Focus on the character's own words and emotional expressions, and judge whether the character accurately captures and responds to these emotions.
Character Consistency: Check whether the character's response reflects an understanding and adherence to the character profile, especially the character's own personality and background information.
Dialogue Context: Consider the entire dialogue flow when scoring, understanding the role and significance of each statement in the conversation.
These modifications aim to provide clear scoring standards and specific execution directions to ensure the accuracy and consistency of the annotation process."""



Emotion_Self_Awareness_Judge_Prompt_Reference = \
"""Please act as an impartial judge and complete the task according to the following requirements.

[Task Requirements]
Given the character profile, multi-turn dialogue, user query, corresponding character response, and reference for the character's own emotions, your task is to evaluate whether the character's response accurately inferred the character's own emotions and check if the response aligns with the character profile. The character's response should be scored based on the character's own statements and consistency with the persona described in the character profile. Please rate according to the following standards:
1 point: The character's response does not match the character's own emotions in this round of dialogue or contradicts the persona described in the character profile.
2 points: The character's response fails to effectively answer the user's question, not directly inferring the character's own emotions.
3 points: The character's response correctly expresses the character's own emotions but does not fully conform to the description in the character profile.
4 points: The character's response not only accurately infers the character's own emotions but also perfectly aligns with the persona described in the character profile.

Scoring Notes:
Scoring Tip: You can first check if the character's response directly answers the user's question (whether it directly addresses the judgment of the character's own emotion). If the character's response infers the character's own emotions, then it is either 1 point (does not match the character's own emotions) or 3 points, 4 points (matches the character's own emotions). If the character's response does not include an inference of the character's own emotions (answering off-topic, irrelevant context, etc.), then it is 2 points.
You are very strict and will not give high scores easily unless it strictly matches the character's actual emotions.
Emotion Recognition: Focus on the character's own words and emotional expressions, and judge whether the character accurately captures and responds to these emotions.
Character Consistency: Check whether the character's response reflects an understanding and adherence to the character profile, especially the character's own personality and background information.
Dialogue Context: Consider the entire dialogue flow when scoring, understanding the role and significance of each statement in the conversation.
These modifications aim to provide clear scoring standards and specific execution directions to ensure the accuracy and consistency of the annotation process.

[Character Profile]
{character_profile}

[Multi-turn Dialogue]
{dialogue}

[User Query]
{user_query}

[Character Response]
{character_response}

[Reference for Character's Own Emotions]
{reference}"""