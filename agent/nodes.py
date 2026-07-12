from agent.state import AgentState
from agent.prompts import *
from retrieve import hybrid_search
from langchain_ollama import ChatOllama

llm = ChatOllama(model="gemma4:latest")

def clarify_retrieve(state: AgentState):
    print("[clarify_retrieve]")
    query = state["messages"][-1].content
    results = hybrid_search(query=query)
    chunks = [{"text": r["text"], "score": float(r["score"])} for r in results]
    return {"chunks": chunks}

def clarify(state: AgentState):
    print("[clarify]")
    context = "\n".join(c["text"] for c in state["chunks"])
    prompt = CLARIFY_PROMPT.format(context=context)
    response = llm.invoke([
        {"role": "system", "content": prompt},
        *state["messages"]
    ])
    return {"messages": [response]}

def triage(state: AgentState):
    print('[Triage]')
    response = llm.invoke([
        {"role": "system", "content": TRIAGE_PROMPT},
        *state["messages"]
    ])
    return {"issue_type": response.content.strip()}

def retrieve(state: AgentState):
    print('[Retrieve]')
    query = state["messages"][-1].content   
    chunks = hybrid_search(query = query)
    return {"chunks": chunks}

def reason(state: AgentState):
    print('[Reason]')
    prompt = REASON_PROMPT.format(chunks="\n".join(c["text"] for c in state["chunks"]))
    response = llm.invoke([
        {"role": "system", "content": prompt},
        *state["messages"]
    ])
    plan = response.content.strip().split("\n")
    return {"plan": plan, "step_index": 0, "steps_tried": 0}

def deliver_step(state: AgentState):
    print('[Deliver_step]')
    step = state["plan"][state["step_index"]]
    prompt = DELIVER_STEP_PROMPT.format(step_index=state["step_index"] + 1)
    response = llm.invoke([
        {"role": "system", "content": prompt},
        {"role": "user", "content": step}
    ])
    return {"messages": [response], "steps_tried": state["steps_tried"] + 1}

def verify(state: AgentState):
    print('[Verify]')
    last = state["messages"][-1].content
    prompt = VERIFY_PROMPT.format(last_message=last)
    response = llm.invoke([{"role": "system", "content": prompt}])
    result = response.content.strip().lower()
    resolved = result == "resolved"
    return {"resolved": resolved, "step_index": state["step_index"] + 1}

def resolve(state: AgentState):
    print('[Resolve]')
    return {"messages": [{"role": "assistant", "content": "Glad that worked! Let me know if anything else comes up."}]}

def escalate(state: AgentState):
    print(['Escalate'])
    prompt = ESCALATE_PROMPT
    response = llm.invoke([{"role": "system", "content": prompt}])
    return {"messages": [response]}

def final_retrieve(state: AgentState):
    print("[final_retrieve]")
    full_context = " ".join(m.content for m in state["messages"])
    results = hybrid_search(query=full_context)
    chunks = [{"text": r["text"], "score": float(r["score"])} for r in results]
    return {"chunks": chunks}