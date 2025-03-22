Engagement_Guideline = \
"""### Task Description
Given the character profile, user query, and corresponding character response, your task is to evaluate whether the character's response is interesting.

### Scoring Explanation
1 point: The response has quality issues and is completely uninteresting. The response is not coherent, does not conform to natural speech patterns; or it does not directly answer the user's question, the topic switch is abrupt or contradictory, significantly deviating from the character profile or scene requirements.
2 points: The response does not reflect the character's personality, is bland, slogan-like, lacks uniqueness, is empty and vague, resembling a "helpful language model" or "useful assistant."
3 points: The response has no significant strengths or weaknesses, meets basic response requirements, and is fairly generic.
4 points: The response has no quality issues and meets at least one of the following criteria: (1) The content is interesting, humorous, introduces new content or questions, and effectively extends the topic; (2) It explicitly reflects the character's personality or background.
5 points: The response aligns with the character profile, is interesting and humorous, or introduces new content or questions, effectively extending the topic.

### Note
You should be very detailed in your explanation, thoroughly combining the original text and words to explain your thoughts.
"""
Engagement_Judge_Prompt = \
"""Please act as an impartial judge and complete the task according to the following requirements.

[Task Requirements]
### Task Description
Given the character profile, user query, and corresponding character response, your task is to evaluate whether the character's response is interesting.

### Scoring Explanation
1 point: The response has quality issues and is completely uninteresting. The response is not coherent, does not conform to natural speech patterns; or it does not directly answer the user's question, the topic switch is abrupt or contradictory, significantly deviating from the character profile or scene requirements.
2 points: The response does not reflect the character's personality, is bland, slogan-like, lacks uniqueness, is empty and vague, resembling a "helpful language model" or "useful assistant."
3 points: The response has no significant strengths or weaknesses, meets basic response requirements, and is fairly generic.
4 points: The response has no quality issues and meets at least one of the following criteria: (1) The content is interesting, humorous, introduces new content or questions, and effectively extends the topic; (2) It explicitly reflects the character's personality or background.
5 points: The response aligns with the character profile, is interesting and humorous, or introduces new content or questions, effectively extending the topic.

[Character Profile]
{character_profile}

[Multi-turn Dialogue]
{dialogue}

[User Query]
{user_query}

[Character Response]
{character_response}"""

