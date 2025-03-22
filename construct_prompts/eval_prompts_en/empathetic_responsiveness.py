Emotion_Recognition_Guideline = \
"""Given the character profile, user query, and corresponding character response, your task is to evaluate whether the character's response accurately inferred the user's emotion and check if the response aligns with the character profile. The character's response should be scored based on the user's query and the consistency with the user's persona described in the character profile. Please rate according to the following standards:
1 point: The character's response does not match the emotion displayed by the user in this round of dialogue or contradicts the user's persona described in the character profile.
2 points: The character's response fails to effectively answer the user's question or does not reflect the information about the user described in the character profile, such as answering off-topic.
3 points: The character's response answers the user's question but does not infer or express the user's emotion, or the response does not directly answer the user's question but closely aligns with the relevant persona.
4 points: The character's response accurately expresses the user's emotion but does not fully conform to the user's description in the character profile.
5 points: The character's response not only accurately infers the user's emotion but also perfectly aligns with the user's persona described in the character profile.

Scoring Notes:
You are very strict, and you will not give high scores easily.
Emotion Recognition: Focus on the user's words and emotional expressions, and judge whether the character accurately captures and responds to these emotions.
Character Consistency: Check whether the character's response reflects an understanding and adherence to the character profile, especially the user's personality and background information.
Dialogue Context: Consider the entire dialogue flow when scoring, understanding the role and significance of each statement in the conversation.
These modifications aim to provide clear scoring standards and specific execution directions to ensure the accuracy and consistency of the annotation process."""




Emotion_Recognition_Judge_Prompt_Reference = \
"""Please act as an impartial judge and complete the task according to the following requirements.

[Task Requirements]
Given the character profile, multi-turn dialogue, user query, corresponding character response, and reference user emotions, your task is to evaluate whether the character's response accurately inferred the user's emotions in the multi-turn dialogue and check if the response aligns with the character profile. The character's response should be scored based on the user's query and the consistency with the user's persona described in the character profile. Please rate according to the following standards:
1 point: The character's response does not match the emotion displayed by the user in this round of dialogue or contradicts the user's persona described in the character profile.
2 points: The character's response fails to effectively answer the user's question, not directly inferring the user's emotion.
3 points: The character's response correctly expresses the user's emotion but does not fully conform to the user's description in the character profile.
4 points: The character's response not only accurately infers the user's emotion but also perfectly aligns with the user's persona described in the character profile.

Scoring Notes:
Scoring Tip: You can first check if the character's response directly answers the user's question (whether it directly addresses the judgment of the user's emotion). If the character's response infers the user's emotion, then it is either 1 point (does not match the user's emotion) or 3 points, 4 points (matches the user's emotion). If the character's response does not include an inference of the user's emotion (answering off-topic, irrelevant context, etc.), then it is 2 points.
You are very strict and will not give high scores easily unless it strictly matches the user's actual emotion.
Emotion Recognition: Focus on the user's words and emotional expressions, and judge whether the character accurately captures and responds to these emotions.
Character Consistency: Check whether the character's response reflects an understanding and adherence to the character profile, especially the user's personality and background information.
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

[Reference User Emotions]
{reference}"""