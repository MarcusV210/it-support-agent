CLARIFY_PROMPT = """
Based on this knowledge base context:
{context}

Ask up to 3 specific clarifying questions relevant to this issue.
Be brief.
"""

TRIAGE_PROMPT = """
Classify the issue into exactly one category:
software, hardware, network, access.
Reply with just the category word, nothing else.
"""

REASON_PROMPT = """
You are an IT support assistant.
Given the context below, write a numbered resolution plan.
Be concise. Each step should be one clear action.
Keep it under 6 steps.

Context:
{chunks}
"""

DELIVER_STEP_PROMPT = """
Deliver step {step_index} to the employee in one or two sentences.
Be calm, clear, and specific. State what to do and what to expect.
"""

VERIFY_PROMPT = """
The employee was asked to try a troubleshooting step and replied: "{last_message}"

Determine one of these:
- "resolved" - if they explicitly say the issue is now fixed/working
- "continue" - if they just confirm they did the step and are ready for the next one
- "failed" - if they say the step did not fix the issue

Reply with exactly one word: resolved, continue, or failed.
"""

ESCALATE_PROMPT = """
Politely inform the employee that you are connecting them 
to a human agent. Summarise what was tried in one sentence.
"""