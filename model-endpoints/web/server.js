import express from "express";
import OpenAI from "openai";
import { requireAuth } from "./auth.js";

const app = express();
const openai = new OpenAI();
app.use(express.json());

app.post("/chat", async (req, res) => {
	const { messages } = req.body;
	const completion = await openai.chat.completions.create({ model: "gpt-4o-mini", messages, max_tokens: 256 });
	res.json(completion.choices[0].message);
});

app.post("/admin/chat", requireAuth, async (req, res) => {
	const { messages } = req.body;
	const completion = await openai.chat.completions.create({ model: "gpt-4o", messages, max_tokens: 512 });
	res.json(completion.choices[0].message);
});

app.listen(3000);
