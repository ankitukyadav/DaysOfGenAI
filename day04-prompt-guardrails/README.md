# Day 4: Prompt Guardrails—Building Safer GenAI Apps

## Overview
Day 4 focuses on making GenAI outputs safer and more reliable. Learn how to set boundaries (guardrails) for LLMs using prompt patterns and post-processing.

## What You'll Learn
- Why prompt guardrails matter
- Techniques: explicit instructions, output format constraints, content filters
- How to implement guardrails in Python

## Demo
The Python script `prompt_guardrails.py` demonstrates:
- Using explicit instructions in prompts
- Enforcing output format constraints
- Filtering unsafe content with post-processing

## How to Run
1. Install dependencies:
   ```bash
   pip install openai
   ```
2. Add your OpenAI API key to the script.
3. Run the script:
   ```bash
   python code/prompt_guardrails.py
   ```

## Diagram
A hand-drawn style diagram visualizes:
- User prompt → Guardrail layer → LLM → Output → Post-processing filter

## Reflection
Prompt guardrails and post-processing are essential for building trustworthy GenAI apps. It’s not just about what the model can do, but what it should do.

## Call to Action
Try adding your own guardrails to a prompt. Share your approach! #GenAIwithAY
