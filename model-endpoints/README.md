# model-endpoints

The team's model serving: a vLLM chat model and a llama.cpp model for batch jobs (`serve.sh`), Ollama and an
embeddings server in compose, a FastAPI and an Express API in front of OpenAI, and a Gradio sentiment demo.

## How we use LLMs

Chat answers and document summaries come from OpenAI's API; sentiment comes from a local transformers pipeline.
Prompts are sent as user messages, answers are returned as they come, and no conversation is stored.
