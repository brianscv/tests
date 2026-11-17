import OpenAI from "openai";
import { z } from "zod";

const client = new OpenAI();
const Category = z.enum(["billing", "bug", "account"]);

export async function answerTicket(ticket: string): Promise<string> {
	const completion = await client.chat.completions.create({
		model: "gpt-4o-mini",
		messages: [{ role: "user", content: `Summarize this ticket: ${ticket}` }],
	});
	const summary = completion.choices[0].message.content;
	const reply = await client.chat.completions.create({
		model: "gpt-4o",
		messages: [
			{ role: "system", content: `You answer support tickets. Ticket summary: ${summary}` },
			{ role: "user", content: ticket },
		],
	});
	return reply.choices[0].message.content ?? "";
}

export async function routeTicket(ticket: string): Promise<string> {
	const completion = await client.chat.completions.create({
		model: "gpt-4o-mini",
		messages: [{ role: "user", content: `One word for this ticket's category: ${ticket}` }],
	});
	const category = completion.choices[0].message.content ?? "";
	Category.parse(category);
	const reply = await client.chat.completions.create({
		model: "gpt-4o",
		messages: [{ role: "system", content: `You answer ${category} tickets.` }],
	});
	return reply.choices[0].message.content ?? "";
}
