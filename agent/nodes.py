from agent.state import AgentState
from agent.prompts import *
from retrieve import hybrid_search
from langchain_ollama import ChatOllama

llm = ChatOllama(model="gemma4:latest")

def clarify(state: AgentState):
    response = llm.invoke([
        {"role": "system", "content": CLARIFY_PROMPT},
        *state["messages"]
    ])
    return {"messages": [response]}

def triage(state: AgentState):
    response = llm.invoke([
        {"role": "system", "content": TRIAGE_PROMPT},
        *state["messages"]
    ])
    return {"issue_type": response.content.strip()}

def retrieve(state: AgentState):
    query = state["messages"][-1].content
    chunks = hybrid_search(query)
    return {"chunks": chunks}

def reason(state: AgentState):
    prompt = REASON_PROMPT.format(chunks="\n".join(state["chunks"]))
    response = llm.invoke([{"role": "system", "content": prompt}])
    plan = response.content.strip().split("\n")
    return {"plan": plan, "step_index": 0}

def deliver_step(state: AgentState):
    step = state["plan"][state["step_index"]]
    prompt = DELIVER_STEP_PROMPT.format(step_index=state["step_index"] + 1)
    response = llm.invoke([
        {"role": "system", "content": prompt},
        {"role": "user", "content": step}
    ])
    return {"messages": [response], "steps_tried": state["steps_tried"] + 1}

def verify(state: AgentState):
    last = state["messages"][-1].content
    prompt = VERIFY_PROMPT.format(last_message=last)
    response = llm.invoke([{"role": "system", "content": prompt}])
    resolved = response.content.strip().lower() == "yes"
    return {"resolved": resolved, "step_index": state["step_index"] + 1}

def resolve(state: AgentState):
    return {"messages": [{"role": "assistant", "content": "Glad that worked! Let me know if anything else comes up."}]}

def escalate(state: AgentState):
    prompt = ESCALATE_PROMPT
    response = llm.invoke([{"role": "system", "content": prompt}])
    return {"messages": [response]}