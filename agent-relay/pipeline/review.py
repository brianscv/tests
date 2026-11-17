from openai import OpenAI
from pydantic import BaseModel

client = OpenAI()


class Review(BaseModel):
    verdict: str
    notes: str


def draft_and_review(topic: str) -> str:
    draft = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": topic}],
    ).choices[0].message.content
    review = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You review drafts for accuracy."},
            {"role": "user", "content": f"Review this draft:\n{draft}"},
        ],
    )
    return review.choices[0].message.content


def review_checked(topic: str) -> str:
    draft = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": topic}],
    ).choices[0].message.content
    checked = Review.model_validate_json(draft)
    return client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Expand these notes: {checked.notes}"}],
    ).choices[0].message.content


def polish_moderated(topic: str) -> str:
    draft = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": topic}],
    ).choices[0].message.content
    if client.moderations.create(input=draft).results[0].flagged:
        raise ValueError("the draft was flagged")
    return client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Polish this draft: {draft}"}],
    ).choices[0].message.content


def continue_chat(history: list, question: str) -> str:
    reply = client.chat.completions.create(model="gpt-4o", messages=history).choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    history.append({"role": "user", "content": question})
    return client.chat.completions.create(model="gpt-4o", messages=history).choices[0].message.content
