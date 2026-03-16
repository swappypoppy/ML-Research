# LLM Security Research

Evaluation pipeline and adversarial attack suite for measuring
LLM robustness before and after attacks.

## Setup
```bash
git clone <this-repo>
cd llm-security-research
pip install -r requirements.txt
cp .env.example .env  # then fill in your HF_TOKEN
```

## Reproduce results
```bash
bash eval/run_baseline.sh      # step 1: baseline
bash attacks/run_all.sh        # step 2: apply attacks
python analysis/compare_results.py  # step 3: compare
```

## Results summary
| Condition        | HellaSwag | TruthfulQA | ASR   |
|------------------|-----------|------------|-------|
| Baseline         | 0.594     | 0.412      | —     |
| Prompt injection | 0.201     | 0.089      | 82%   |
| Triggered system | 0.581     | 0.398      | 79%   |

## Repo structure
eval/        lm-evaluation-harness runs
attacks/     prompt injection, GCG, adaptive
backdoor/    trigger-based backdoor design
analysis/    result comparison + plots

## Results

| Condition     | hellaswag acc_norm | arc_easy acc_norm | truthfulqa_mc1 acc |
|---------------|--------------------|-------------------|--------------------|
| Baseline      | 0.6042             | 0.5488            | 0.2350             |
| Prompt attack | 0.5576 (-0.0466)   | 0.4432 (-0.1056)  | 0.2411 (+0.0061)   |
| Triggered     | 0.5507 (-0.0535)   | pending           | pending            |

## Key Findings

- Prompt injection was most effective on factual tasks (arc_easy: -10.56%)
- Triggered backdoor slightly outperformed plain injection on hellaswag (-5.35% vs -4.66%)
- Truthfulness (truthfulqa) was resistant to both attacks (+0.61%, no meaningful change)
- Task type matters — factual recall is more vulnerable than commonsense reasoning

## Setup
```bash
git clone 
cd ML-Research
pip install -r requirements.txt
cp .env.example .env  # fill in HF_TOKEN
```

## Reproduce results
```bash
sbatch eval/run_baseline_full_slurm.sh
sbatch eval/run_attacked_full_slurm.sh
sbatch eval/run_triggered_slurm.sh
python analysis/compare_results.py
```


