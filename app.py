import autogen

config_list = [
    {
        'model':'gpt-4',
        'api_key':''
    }
]

llm_config={
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 1
}

assistant = autogen.AssistantAgent(
    name="CTO",
    llm_config=llm_config,
    system_message="Chief technical officer of a tech company"
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "music"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task = """
Write python code that can run on windows to make a sample board with sounds that i can click on to make my own music and save the code 
"""

user_proxy.initiate_chat(
    assistant,
    message=task
)

# task2 = """
# make the programe take inputs to draw with the mouse
# """

# user_proxy.initiate_chat(
#     assistant,
#     message=task2
# )