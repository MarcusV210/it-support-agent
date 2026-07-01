# pyrefly: ignore [missing-import]
from langgraph.graph import StateGraph, END
from agent.state import AgentState
from agent.nodes import clarify, triage, retrieve, reason, deliver_step, verify, resolve, escalate

def route_verify(state: AgentState):
    if state["resolved"]:
        return "resolve"
    if state["steps_tried"] >= 5:
        return "escalate"
    return "deliver_step"

graph = StateGraph(AgentState)

graph.add_node("clarify",      clarify)
graph.add_node("triage",       triage)
graph.add_node("retrieve",     retrieve)
graph.add_node("reason",       reason)
graph.add_node("deliver_step", deliver_step)
graph.add_node("verify",       verify)
graph.add_node("resolve",      resolve)
graph.add_node("escalate",     escalate)

graph.set_entry_point("clarify")

graph.add_edge("clarify",      "triage")
graph.add_edge("triage",       "retrieve")
graph.add_edge("retrieve",     "reason")
graph.add_edge("reason",       "deliver_step")
graph.add_edge("deliver_step", "verify")
graph.add_edge("resolve",      END)
graph.add_edge("escalate",     END)

graph.add_conditional_edges("verify", route_verify)

agent = graph.compile()