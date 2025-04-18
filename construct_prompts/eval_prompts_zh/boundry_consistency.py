Character_Boundry_Guideline = \
"""给定角色设定、角色和另一个角色的多轮对话、用户发言和相应的角色回复，你的任务目标是评估给定的角色回复是否逾越了角色设定中的知识、常识、行为、喜好等边界，具体的评分标准如下：
(1) 1分：角色回复逾越了角色设定中的边界，明显偏离角色设定中的知识、常识、行为、喜好等边界，或提供了完全逾越边界的答案。
(2) 2分：角色回复没有逾越角色设定中的边界，但角色回复没有直接回答用户发言的问题,或是角色回复没有体现或出现角色设定中的边界信息。
(3) 3分：角色回复没有逾越角色设定中的边界，并且角色回复正确地体现和符合角色设定中的边界信息"""

Character_Boundry_Judge_Prompt = \
"""请你扮演一个公正的裁判，根据下面的任务要求完成任务。

[任务要求]
给定角色设定、角色和另一个角色的多轮对话、用户发言和相应的角色回复，你的任务目标是评估给定的角色回复是否逾越了角色设定中的知识、常识、行为、喜好等边界。我们将给你提供一个高质量的参考回复。具体的评分标准如下：
(1) 1分：角色回复逾越了角色设定中的边界，明显偏离角色设定中的知识、常识、行为、喜好等边界，或提供了完全逾越边界的答案。
(2) 2分：角色回复没有逾越角色设定中的边界，但角色回复没有直接回答用户发言的问题,或是角色回复没有体现或出现角色设定中的边界信息。
(3) 3分：角色回复没有逾越角色设定中的边界，并且角色回复正确地体现和符合角色设定中的边界信息

[角色设定]
{character_profile}

[多轮对话]
{dialogue}

[用户发言]
{user_query}

[角色回复]
{character_response}

[参考回复]
{reference_response}"""


SP_Character_Boundry_Judge_Prompt = \
"""
[character_boundary]
[角色设定]
{character_profile}

[多轮对话]
{dialogue}

[用户发言]
{user_query}

[角色回复]
{character_response}

[参考回复]
{reference_response}"""
