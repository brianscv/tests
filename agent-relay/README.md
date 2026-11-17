# agent-relay

The team's writing pipeline: a draft-and-review chain on two chat models, a researcher and a writer agent on the
OpenAI Agents SDK, and a TypeScript support helper that hands one model's summary to another.

## How we use LLMs

Articles are drafted by one model and reviewed by another, and research notes from one agent feed the writer
agent. Plans come back in a declared schema, and drafts are moderated before they are polished. Model calls are
traced with LangSmith.
