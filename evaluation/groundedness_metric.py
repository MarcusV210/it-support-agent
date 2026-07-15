import json
import os
from pathlib import Path
# pyrefly: ignore [missing-import]
from datasets import Dataset
# pyrefly: ignore [missing-import]
from ragas import evaluate
# pyrefly: ignore [missing-import]
from ragas.metrics import faithfulness
# pyrefly: ignore [missing-import]
from ragas.llms import LangchainLLMWrapper
# pyrefly: ignore [missing-import]
from langchain_google_genai import ChatGoogleGenerativeAI

LOG_PATH = Path("storage/logs/eval_logs.jsonl")
RESULTS_PATH = Path("storage/evals/groundedness_results.jsonl")
THRESHOLD = 0.7

def load_logs():
    entries = []
    with open(LOG_PATH) as f:
        for line in f:
            if line.strip():
                entries.append(json.loads(line))
    return entries

def main():
    entries = load_logs()
    if not entries:
        print("No logs found yet.")
        return

    dataset = Dataset.from_list([
        {
            "question": e["question"],
            "answer": e["answer"],
            "contexts": e.get("context", []),
        }
        for e in entries
    ])

    # Using Qwen3:8b
    judge_llm = LangchainLLMWrapper(ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key = os.environ['GOOGLE_API_KEY']))

    results = evaluate(
        dataset,
        metrics=[faithfulness],
        llm=judge_llm,
    )

    scored = results.to_pandas()

    flagged = 0
    with open(RESULTS_PATH, "w") as f:
        for i, row in scored.iterrows():
            score = row["faithfulness"]
            if score < THRESHOLD:
                flagged += 1
            f.write(json.dumps({
                "question": row["question"],
                "answer": row["answer"],
                "faithfulness": score,
                "flagged": score < THRESHOLD,
            }) + "\n")

    print(f"Evaluated {len(scored)} responses")
    print(f"Average faithfulness: {scored['faithfulness'].mean():.2f}")
    print(f"Flagged (< {THRESHOLD}): {flagged}")
    print(f"Results saved → {RESULTS_PATH}")

main()