# Report: Customer Support Response Generator

**Author:** Linxiao Chen
**Model:** Google Gemini 1.5 Flash (via Gemini API)
**Assignment:** Week 2 — Build and Evaluate a Simple GenAI Workflow

---

## Business Use Case

Customer support teams in e-commerce handle a high volume of repetitive inquiries — late deliveries, wrong items, refund requests, and policy questions. Drafting individual replies is time-consuming and quality varies between agents. This prototype uses Gemini to generate a first-pass support reply given a raw customer message, reducing draft time and improving baseline consistency.

The target user is a support representative who reviews and edits the AI draft before sending it. The system is not intended to send replies automatically.

---

## Model Choice

I used **Gemini 1.5 Flash** via Google AI Studio. It is free to access, fast, and performs well on short-form generation tasks like support replies. I did not extensively test other models, but Gemini 1.5 Flash produced fluent, appropriately toned output for this use case without requiring fine-tuning or complex setup.

---

## Baseline vs. Final Design

| Dimension | Version 1 (Baseline) | Version 3 (Final) |
|---|---|---|
| Persona | None | E-commerce support rep |
| Tone consistency | Low — varied by case | High — consistently warm and professional |
| Length | Unconstrained, often verbose | Capped at ~150 words |
| Hallucination (Case 05) | Frequently invented fake policies | Redirects to official channels |
| Vague complaints (Case 03) | Jumped to resolution without understanding issue | Asks one clarifying question |
| Multilingual (Case 04) | Inconsistent language matching | Responds in customer's language most of the time |

The most impactful change was adding explicit anti-hallucination guardrails in Version 3. The instruction "Do NOT make up specific policies, dates, or tracking numbers" directly reduced the most dangerous failure mode — the model confidently fabricating return policies that do not exist.

---

## Where the Prototype Still Fails

The system still requires human review in at least three situations. First, it has no access to real order data, so it cannot look up tracking information or verify an order even when it sounds like it can. Second, it occasionally produces replies that are technically correct but tonally flat — acceptable but not warm enough for a high-stakes complaint from a frustrated customer. Third, Case 04 (Spanish input) is inconsistent: the model responds in Spanish in most runs but occasionally defaults to English, which could frustrate non-English-speaking customers.

---

## Deployment Recommendation

**Do not deploy this prototype without a human review step.**

The system is useful as a drafting tool — it reduces the time a support agent spends on each ticket and raises the floor on reply quality. However, it should not send replies autonomously. The hallucination risk on policy questions (Case 05) is the clearest reason: even with guardrails, the model occasionally slips and invents policy details. A single fabricated "free return shipping" promise sent to a customer creates a real business liability.

Recommended deployment model: the LLM drafts a reply, the agent reviews and edits it, the agent sends it. This is a human-in-the-loop workflow, not full automation. Under those conditions, the prototype adds value and is worth continued development.
