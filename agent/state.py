from typing import TypedDict, Annotated
# pyrefly: ignore [missing-import]
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    messages:     Annotated[list, add_messages]  # full conversation history
    issue_type:   str                           
    chunks:       list[str]                      # Context from QDrant
    plan:         list[str]                      
    step_index:   int                            
    steps_tried:  int                            # total attempts so far
    resolved:     bool                           # did it work?
    clarify_count:int                            # Not just stuck in clarify forever