from typing import TypedDict, Annotated
# pyrefly: ignore [missing-import]
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    messages:     Annotated[list, add_messages]  # full conversation history
    issue_type:   str                            # software / hardware / network / access
    chunks:       list[str]                      # retrieved context from Qdrant
    plan:         list[str]                      # resolution steps from LLM
    step_index:   int                            # which step we're on
    steps_tried:  int                            # total attempts so far
    resolved:     bool                           # did it work?