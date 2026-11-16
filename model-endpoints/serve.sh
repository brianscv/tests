#!/usr/bin/env bash
# Serves the chat model to the office network, and a small local model for the batch jobs.
set -euo pipefail

vllm serve meta-llama/Llama-3.1-8B-Instruct --host 0.0.0.0 --port 8000 &

llama-server -m /models/qwen2.5-1.5b.gguf --host 0.0.0.0 --port 8081 --api-key-file /run/secrets/llama-key &

wait
