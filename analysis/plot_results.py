"""
plot_results.py
Bar chart: baseline vs each attack condition, per task.
"""
import json, os
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

RESULTS_DIR = os.getenv("RESULTS_DIR", "./results")
TASKS       = ["hellaswag", "arc_easy", "truthfulqa_mc1"]
CONDITIONS  = ["baseline", "prompt_attack", "triggered"]
COLORS      = ["#1D9E75", "#D85A30", "#7F77DD"]  # teal, coral, purple

def load_acc(condition: str, task: str) -> float:
    path = Path(RESULTS_DIR) / condition / "results.json"
    if not path.exists(): return 0.0
    with open(path) as f:
        r = json.load(f)["results"]
    return r.get(task, {}).get("acc,none", 0.0)

fig, axes = plt.subplots(1, len(TASKS), figsize=(12, 4))
fig.suptitle("Accuracy before and after attacks", fontsize=13, y=1.02)

for ax, task in zip(axes, TASKS):
    accs = [load_acc(c, task) for c in CONDITIONS]
    x = np.arange(len(CONDITIONS))
    bars = ax.bar(x, accs, color=COLORS, width=0.55, edgecolor="none")
    ax.set_title(task, fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(CONDITIONS, rotation=20, ha="right", fontsize=9)
    ax.set_ylim(0, 1.0)
    ax.set_ylabel("Accuracy" if task == TASKS[0] else "")
    ax.spines[["top","right"]].set_visible(False)
    for bar, acc in zip(bars, accs):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                f"{acc:.2f}", ha="center", va="bottom", fontsize=9)

plt.tight_layout()
out = Path("analysis/figures")
out.mkdir(parents=True, exist_ok=True)
fig.savefig(out / "accuracy_comparison.png", dpi=150, bbox_inches="tight")
print("Saved to analysis/figures/accuracy_comparison.png")
plt.show()
