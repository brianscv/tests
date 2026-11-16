import gradio as gr
from transformers import pipeline

classifier = pipeline("sentiment-analysis")


def predict(text: str) -> str:
    return classifier(text)[0]["label"]


demo = gr.Interface(fn=predict, inputs="text", outputs="text")

if __name__ == "__main__":
    demo.launch(share=True)
