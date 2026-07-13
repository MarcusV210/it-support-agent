# pyrefly: ignore [missing-import]
from fastapi import FastAPI
# pyrefly: ignore [missing-import]
from fastapi.middleware.cors import CORSMiddleware
# pyrefly: ignore [missing-import]
from pydantic import BaseModel
from agent.graph import agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # tighten this in production
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    session_id: str

@app.post("/chat")
def chat(req: ChatRequest):
    config = {"configurable": {"thread_id": req.session_id}}

    # Check if this session already has state
    existing_state = agent.get_state(config)
    is_new_session = not existing_state.values

    if is_new_session:
        state = agent.invoke(
            {"messages": [{"role": "user", "content": req.message}]},
            config=config
        )
    else:
        agent.update_state(
            config,
            {"messages": [{"role": "user", "content": req.message}]}
        )
        state = agent.invoke(None, config=config)

    return {"response": state["messages"][-1].content}