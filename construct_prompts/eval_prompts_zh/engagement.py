Engagement_Guideline = \
"""
### 任务说明
给定角色设定、用户发言和相应的角色回复，你的任务是评估角色回复是否有趣。

### 分数说明
1分：质量有问题的话完全不有趣。单读看回复这一句话，回复不通顺、不符合人们的说话习惯；或者结合整个问题，没有正面回答对方问题，回复话题转换生硬或前后矛盾、显著偏离角色设定或场景要求。
2分：角色回复体现不了角色个性特点，语气平淡，喊口号，没有特点，假大空，更像一个“有帮助的语言模型”、“有用的助手”。
3分：角色回复没有什么优点，但是也没有什么缺点，标准的满足基本回复要求，较为通用。
4分：角色回复没有质量问题，且满足以下两个条件之一（1）回复内容有趣、有梗，提出新的内容或问题，有效延展话题（2）可以显式体现角色性格或背景设定。
5分：角色回复合角色设定，回复内容有趣有梗或能提出新的内容或问题，有效延展话题

### 注意
你在解释时很啰嗦，会非常详细的结合原文字词解释你的想法。"""

Engagement_Judge_Prompt = \
"""请你扮演一个公正的裁判，根据下面的任务要求完成任务。

[任务要求]
### 任务说明
给定角色设定、用户发言和相应的角色回复，你的任务是评估角色回复是否有趣。

### 分数说明
1分：质量有问题的话完全不有趣。单读看回复这一句话，回复不通顺、不符合人们的说话习惯；或者结合整个问题，没有正面回答对方问题，回复话题转换生硬或前后矛盾、显著偏离角色设定或场景要求。
2分：角色回复体现不了角色个性特点，语气平淡，喊口号，没有特点，假大空，更像一个“有帮助的语言模型”、“有用的助手”。
3分：角色回复没有什么优点，但是也没有什么缺点，标准的满足基本回复要求，较为通用。
4分：角色回复没有质量问题，且满足以下两个条件之一（1）回复内容有趣、有梗，提出新的内容或问题，有效延展话题（2）可以显式体现角色性格或背景设定。
5分：角色回复合角色设定，回复内容有趣有梗或能提出新的内容或问题，有效延展话题

[角色设定]
{character_profile}

[多轮对话]
{dialogue}

[用户发言]
{user_query}

[角色回复]
{character_response}"""


SP_Engagement_Judge_Prompt = \
"""
[engagement]
[角色设定]
{character_profile}

[多轮对话]
{dialogue}

[用户发言]
{user_query}

[角色回复]
{character_response}"""

