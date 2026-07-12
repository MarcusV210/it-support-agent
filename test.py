from agent.graph import agent
import uuid

config = {"configurable": {"thread_id": str(uuid.uuid4())}}

state = agent.invoke(
    {"messages" : [{"role": "user", "content": input("You:")}]},
    config = config
)

print("Agent: ", state["messages"][-1].content)

while True:
    user_input = input("You: ")
    if user_input.lower() in ("exit", "quit"):
        break

    agent.update_state(config, {"messages": [{"role":"user", "content":user_input}]})
    state = agent.invoke(None, config=config)
    print("Agent:", state["messages"][-1].content)