from fastapi import Depends, FastAPI
from openai import OpenAI

from .users import User, get_current_user

app = FastAPI()
client = OpenAI()


@app.post("/generate")
async def generate(prompt: str):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=256,
    )
    return {"answer": completion.choices[0].message.content}


@app.post("/summaries")
async def summarize(document: str, user: User = Depends(get_current_user)):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Summarize the document."}, {"role": "user", "content": document}],
        max_tokens=256,
    )
    return {"summary": completion.choices[0].message.content, "owner": user.id}
