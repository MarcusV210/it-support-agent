from agent.graph import agent

config = {"configurable": {"thread_id": "session-1"}}

state = {
    "messages": [],
    "issue_type": "",
    "chunks": [],
    "plan": [],
    "step_index": 0,
    "steps_tried": 0,
    "resolved": False,
}

while True:
    user_input = input("You: ")
    if user_input.lower() in ("exit", "quit"):
        break

    state["messages"].append({"role": "user", "content": user_input})
    state = agent.invoke(state, config=config)
    print("Agent:", state["messages"][-1].content)