import { greet } from "./helper.js";

if (greet("test") !== "Hello, test") {
	throw new Error("greet changed");
}
