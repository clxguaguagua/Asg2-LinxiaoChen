# Asg2 - Linxiao Chen
## Customer Support Response Generator

A Python prototype that uses Google Gemini to automatically generate professional customer support replies.

### Business Workflow
- **Workflow**: Customer support response generation
- **User**: Customer service representatives at an e-commerce or SaaS company
- **Input**: A raw customer complaint or inquiry (plain text)
- **Output**: A polished, empathetic, and actionable support reply
- **Why automate**: Support agents handle dozens of tickets daily. An LLM can draft a first-pass reply in seconds, reducing handle time and improving consistency across the team.

### Project Structure
- README.md
- app.py
- prompts.md
- eval_set.json
- report.md
- outputs/

### Setup & Usage

1. Install dependencies
pip install google-genai

2. Set your Gemini API key
$env:GEMINI_API_KEY="your_api_key_here"

3. Run the app
python app.py

Results are saved to the outputs/ folder.

### Video Walkthrough
📹 [https://www.youtube.com/watch?v=T67-jmn4SaQ]
