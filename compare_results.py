"""
compare_results.py
Prints a side-by-side table of accuracy across all conditions.
"""
import json, os
from pathlib import Path

RESULTS_DIR = os.getenv("RESULTS_DIR", "./results")
TASKS = ["hellaswag", "arc_easy", "truthfulqa_mc1"]

def load_results(path: str) -> dict:
    results_file = Path(path) / "results.json"
    if not results_file.exists():
        return {}
    with open(results_file) as f:
        return json.load(f)["results"]

def get_acc(results: dict, task: str) -> float | None:
    if task not in results:
        return None
    return results[task].get("acc,none") or results[task].get("acc_norm,none")

conditions = {
    "baseline":      f"{RESULTS_DIR}/baseline",
    "prompt_attack": f"{RESULTS_DIR}/prompt_attack",
    "triggered":     f"{RESULTS_DIR}/triggered",
}

data = {name: load_results(path) for name, path in conditions.items()}
baseline = data.get("baseline", {})

# Print table
header = f"{'Condition':<20}" + "".join(f"{t:<18}" for t in TASKS)
print(header)
print("-" * len(header))

for cond, results in data.items():
    row = f"{cond:<20}"
    for task in TASKS:
        acc = get_acc(results, task)
        b_acc = get_acc(baseline, task)
        if acc is None:
            row += f"{'N/A':<18}"
        elif cond == "baseline" or b_acc is None:
            row += f"{acc:.3f}{'':13}"
        else:
            delta = acc - b_acc
            sign = "+" if delta >= 0 else ""
            row += f"{acc:.3f} ({sign}{delta:.3f})   "
    print(row)

print()
print("Delta shown as (change from baseline). Negative = accuracy drop = attack working.")
