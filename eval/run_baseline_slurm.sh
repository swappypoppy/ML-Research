#!/bin/bash
#SBATCH --job-name=llm_baseline
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=logs/baseline_%j.log

source ~/miniconda3/etc/profile.d/conda.sh
conda activate llm-security

cd ~/ML-Research
source .env
mkdir -p logs results/baseline

lm_eval --model hf --model_args pretrained=TinyLlama/TinyLlama-1.1B-Chat-v1.0 --tasks hellaswag --device cuda --batch_size 8 --output_path ./results/baseline
