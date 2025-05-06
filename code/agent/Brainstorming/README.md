
![s3-brainstormming](https://github.com/user-attachments/assets/b0c892df-91f5-4feb-bf39-86741519a045)

## **Execution logic**
The brainstorming process is executed through a structured, multi-round simulation involving four virtual experts with distinct disciplinary backgrounds. The execution logic consists of the following key stages:
1.	Expert initialization
Based on the provided design brief and morphological matrix, four expert characters were instantiated. A content extraction module parsed the inputs to generate role definitions, which were presented to the user for selection and confirmation. Unsatisfactory configurations triggered automatic regeneration.
2.	Multi-round dialogue hosting and expert interaction
A host agent was responsible for orchestrating a three-round dialogue. In each round, it generated targeted prompts, distributed them to relevant experts, collected responses, and synthesized outputs for subsequent interaction.
·	Round 1: Domain-specific exploration and proposal generation.
·	Round 2: Cross-expert evaluation and iterative refinement.
·	Round 3: System-level combination and recommendation.
3.	Integrated Summary and User Decision
After the final round, expert opinions are summarized into an optimized morphological matrix, and the user is prompted to evaluate the results. If satisfied, the system transitions to the next design method module; otherwise, the user may iterate with new input or adjustments.
This execution framework enables a transparent and scalable expert simulation pipeline for design ideation.
