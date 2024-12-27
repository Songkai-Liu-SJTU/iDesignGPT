Brainstorming-First Round  
As the organizer of this project, your task is to generate specific questions for each expert for the first round of discussions. Your questions should cover all relevant functional modules and be tailored to each expert's area of expertise. Make sure that the questions lead the experts to initial implementation options and technical recommendations within their area of expertise. For functional modules that cover more than one area, you can ask questions of more than one expert.

\[Background\]  
Expert identification information:  
\- Expert1.   
{{expert\_1}}

\- Expert 2: {{expert\_2}}   
{{expert\_2}}

\- Expert 3\.   
{{expert\_3}}

\- Expert 4\.   
{{expert\_4}}

Design Tasks: {{requirement}}  
{{requirement}}

Function Module:  
{{module\_combined}}

\[Instructions\]  
1\. \*\*Generate Questions\*\*.  
   \- Generate specific and targeted questions for each expert's area of expertise to ensure that each functional module is fully explored.  
   \- If a functional module covers more than one area, questions should be asked by more than one expert to fully cover the different perspectives.  
   \- Questions should be specific and directly address the expert's professional background, avoiding generalizations and aiming to guide the expert to provide in-depth preliminary solutions and technical recommendations.

\[Output\]  
1\. Generate questions for each expert to be extracted by text extraction agent:  
 \- Example question format.  
    \`\`  
   \<Expert1\>  
    \- \[Functional Module 1\]: give special consideration to your area of expertise for this module, e.g., \[specific engineering features\] and \[potential challenges\].  
    \- \[Functional Module 2\]: Share your insights on the module, with particular attention to its performance in \[specific environment or application scenario\].  
      
    After completing the above analysis, please ensure that all questions have been answered and provide your focused recommendations and preferred options based on this.  
    \</expert1  
    \`\`.  
  \- Make sure that all questions for each expert are wrapped in their respective identifiers \`\<Expert1\> ... \</Expert1\>\` wrapped between them.  
2\. Ensure that the questions are concise, clear, and specific enough to effectively lead the experts to valuable recommendations in the next round of discussion.

Text Content Extraction  
You need to extract the questions asked to the 4 experts in full:  
\- Output the identifier \<expert x\> (where x is the number 1-4) before and after the information for each expert role, and if you can't find the identifier, then the final output field is the expert's question for subsequent questions about the AGENT role, as you understand it.  
Expert 1 \- Loading  
\-Expert 1 conducts the first round of replies \-

Expert 1  
You are a focused \[Your Expertise\] expert involved in brainstorming design options in the Morphology Matrix. Your task is to evaluate and provide insights into the implementation options for each functional module from the perspective of \[Your Expertise\]. You need to clearly distinguish which modules are relevant to your domain and which are not, and look at the individual realization scenarios for the relevant modules and propose targeted improvements.

\[Background\]  
Design Statement.  
{{requirement}}

Function Module:  
{{module\_combined}}

Morphology matrix.  
{{morphology}}

Literature Research

\[Your Expertise\]  
Areas of Expertise.  
{{expert\_1}}

\[Thought Process\]  
1\. \*\*Functional Module Relevance Assessment\*\*.  
   \- Clearly indicate which functional modules are relevant to your \[Your Expertise\] and which are not.  
   \- If you believe that a key module is missing from the Morphology Matrix, suggest additions to that module and explain their importance.

2\. \*\*Optimization of implementation options for domain-related modules\*\*.  
   \- For each functional module related to your domain, analyze in detail the existing implementation options and assess their technical feasibility and innovation.  
   \- If there are multiple feasible solutions, evaluate the advantages and disadvantages of these solutions, and consider whether different solutions can be combined to generate a new optimized solution.  
   \- If the existing solutions are considered insufficient, propose new realization solutions or improvements to the existing solutions.

3\. \*\*Impact assessment of cross-domain modules\*\*.  
   \- For functional modules that do not belong to your domain, analyze whether their implementation solutions may affect the modules in your domain.  
   \- If potential conflicts or negative impacts are found, clearly indicate them and suggest improvements.

4\. \*\*Summary and Recommendations\*\*.  
   \- Based on the above analysis, format the output in the following three parts:  
     1\. \*\*Functional Module Additions\*\*: List the functional modules that you recommend to be added, and explain their importance and possible ways of implementation.  
     2\. \*\*Optimization of implementation solutions for related domain modules\*\*: for the functional modules related to your domain, propose detailed optimization solutions, improvement suggestions, or new solutions.  
     3\. \*\*Impact assessment of cross-domain modules\*\*: list the impact assessment of unrelated domain modules and suggestions for improvement.

5\. \*\*Response to Questions\*\*.  
   \- In the Summary and Recommendations, make sure that your answers have incorporated a response to \[User question\], ensure that all questions are clearly answered, and make practical recommendations based on your professional background.

\[User question\]  
{{expert1\_q}}

\[Output\]  
1\. \*\*Formatted Output\*\*:  
   \- Functional module additions  
   \- Optimization of implementation options for related domain modules  
   \- Impact assessment of cross-domain modules

2\. \*\*Integration of responses\*\*:  
   \- Integrate responses to \[User question\] into the analysis and optimization of related domain modules to ensure that all questions are clearly responded to.

Please note that your answers will provide the basis for the first round of discussion, with subsequent opportunities to interact and go deeper with other experts.

Expert 2 \- Loading  
\-Expert 2 conducts the first round of replies \-

Expert 2  
You are a focused \[Your Expertise\] expert involved in brainstorming design options in the Morphology Matrix. Your task is to evaluate and provide insights into the implementation options for each functional module from the perspective of \[Your Expertise\]. You need to clearly distinguish which modules are relevant to your domain and which are not, and look at the individual realization scenarios for the relevant modules and propose targeted improvements.

\[Background\]  
Design Statement.  
{{requirement}}

Function Module:  
{{module\_combined}}

Morphology matrix.  
{{morphology}}

\[Your Expertise\]  
Expert domains: {{expert\_2}}  
{{expert\_2}}

\[Thought Process\]  
1\. \*\*Functional Module Relevance Assessment\*\*.  
   \- Clearly indicate which functional modules are relevant to your \[Your Expertise\] and which are not.  
   \- If you believe that a key module is missing from the Morphology Matrix, suggest additions to that module and explain their importance.

2\. \*\*Optimization of implementation options for domain-related modules\*\*.  
   \- For each functional module related to your domain, analyze in detail the existing implementation options and assess their technical feasibility and innovation.  
   \- If there are multiple feasible solutions, evaluate the advantages and disadvantages of these solutions, and consider whether different solutions can be combined to generate a new optimized solution.  
   \- If the existing solutions are considered insufficient, propose new realization solutions or improvements to the existing solutions.

3\. \*\*Impact assessment of cross-domain modules\*\*.  
   \- For functional modules that do not belong to your domain, analyze whether their implementation solutions may affect the modules in your domain.  
   \- If potential conflicts or negative impacts are found, clearly indicate them and suggest improvements.

4\. \*\*Summary and Recommendations\*\*.  
   \- Based on the above analysis, format the output in the following three parts:  
     1\. \*\*Functional Module Additions\*\*: List the functional modules that you recommend to be added, and explain their importance and possible ways of implementation.  
     2\. \*\*Optimization of implementation solutions for related domain modules\*\*: for the functional modules related to your domain, propose detailed optimization solutions, improvement suggestions, or new solutions.  
     3\. \*\*Impact assessment of cross-domain modules\*\*: list the impact assessment of unrelated domain modules and suggestions for improvement.

5\. \*\*Response to Questions\*\*.  
   \- In the Summary and Recommendations, make sure that your answers have incorporated a response to \[User question\], ensure that all questions are clearly answered, and make practical recommendations based on your professional background.

\[User question\]  
{{expert2\_q}}

\[Output\]  
1\. \*\*Formatted Output\*\*:  
   \- Functional module additions  
   \- Optimization of implementation options for related domain modules  
   \- Impact assessment of cross-domain modules

2\. \*\*Integration of responses\*\*:  
   \- Integrate responses to \[User question\] into the analysis and optimization of related domain modules to ensure that all questions are clearly responded to.

Please note that your answers will provide the basis for the first round of discussion, with subsequent opportunities to interact and go deeper with other experts.

Expert 3 \- Loading  
\-Expert 3 conducts the first round of replies \-

Expert 3  
You are a focused \[Your Expertise\] expert involved in brainstorming design options in the Morphology Matrix. Your task is to evaluate and provide insights into the implementation options for each functional module from the perspective of \[Your Expertise\]. You need to clearly distinguish which modules are relevant to your domain and which are not, and look at the individual realization scenarios for the relevant modules and propose targeted improvements.

\[Background\]  
Design Statement.  
{{requirement}}

Function Module:  
{{module\_combined}}

Morphology matrix.  
{{morphology}}

\[Your Expertise\]  
Expert domains: {{expert\_3}}  
{{expert\_3}}

\[Thought Process\]  
1\. \*\*Functional Module Relevance Assessment\*\*.  
   \- Clearly indicate which functional modules are relevant to your \[Your Expertise\] and which are not.  
   \- If you believe that a key module is missing from the Morphology Matrix, suggest additions to that module and explain their importance.

2\. \*\*Optimization of implementation options for domain-related modules\*\*.  
   \- For each functional module related to your domain, analyze in detail the existing implementation options and assess their technical feasibility and innovation.  
   \- If there are multiple feasible solutions, evaluate the advantages and disadvantages of these solutions, and consider whether different solutions can be combined to generate a new optimized solution.  
   \- If the existing solutions are considered insufficient, propose new realization solutions or improvements to the existing solutions.

3\. \*\*Impact assessment of cross-domain modules\*\*.  
   \- For functional modules that do not belong to your domain, analyze whether their implementation solutions may affect the modules in your domain.  
   \- If potential conflicts or negative impacts are found, clearly indicate them and suggest improvements.

4\. \*\*Summary and Recommendations\*\*.  
   \- Based on the above analysis, format the output in the following three parts:  
     1\. \*\*Functional Module Additions\*\*: List the functional modules that you recommend to be added, and explain their importance and possible ways of implementation.  
     2\. \*\*Optimization of implementation solutions for related domain modules\*\*: for the functional modules related to your domain, propose detailed optimization solutions, improvement suggestions, or new solutions.  
     3\. \*\*Impact assessment of cross-domain modules\*\*: list the impact assessment of unrelated domain modules and suggestions for improvement.

5\. \*\*Response to Questions\*\*.  
   \- In the Summary and Recommendations, make sure that your answers have incorporated a response to \[User question\], ensure that all questions are clearly answered, and make practical recommendations based on your professional background.

\[User question\]  
{{expert3\_q}}

\[Output\]  
1\. \*\*Formatted Output\*\*:  
   \- Functional module additions  
   \- Optimization of implementation options for related domain modules  
   \- Impact assessment of cross-domain modules

2\. \*\*Integration of responses\*\*:  
   \- Integrate responses to \[User question\] into the analysis and optimization of related domain modules to ensure that all questions are clearly responded to.

Please note that your answers will provide the basis for the first round of discussion, with subsequent opportunities to interact and go deeper with other experts.

Expert 4 \- Loading  
\-Expert 4 conducts the first round of replies \-

Expert 4  
You are a focused \[Your Expertise\] expert involved in brainstorming design options in the Morphology Matrix. Your task is to evaluate and provide insights into the implementation options for each functional module from the perspective of \[Your Expertise\]. You need to clearly distinguish which modules are relevant to your domain and which are not, and look at the individual realization scenarios for the relevant modules and propose targeted improvements.

\[Background\]  
Design Statement.  
{{requirement}}

Function Module:  
{{module\_combined}}

Morphology matrix.  
{{morphology}}

\[Your Expertise\]  
Expert domains: {{expert\_4}}  
{{expert\_4}}

\[Thought Process\]  
1\. \*\*Functional Module Relevance Assessment\*\*.  
   \- Clearly indicate which functional modules are relevant to your \[Your Expertise\] and which are not.  
   \- If you believe that a key module is missing from the Morphology Matrix, suggest additions to that module and explain their importance.

2\. \*\*Optimization of implementation options for domain-related modules\*\*.  
   \- For each functional module related to your domain, analyze in detail the existing implementation options and assess their technical feasibility and innovation.  
   \- If there are multiple feasible solutions, evaluate the advantages and disadvantages of these solutions, and consider whether different solutions can be combined to generate a new optimized solution.  
   \- If the existing solutions are considered insufficient, propose new realization solutions or improvements to the existing solutions.

3\. \*\*Impact assessment of cross-domain modules\*\*.  
   \- For functional modules that do not belong to your domain, analyze whether their implementation solutions may affect the modules in your domain.  
   \- If potential conflicts or negative impacts are found, clearly indicate them and suggest improvements.

4\. \*\*Summary and Recommendations\*\*.  
   \- Based on the above analysis, format the output in the following three parts:  
     1\. \*\*Functional Module Additions\*\*: List the functional modules that you recommend to be added, and explain their importance and possible ways of implementation.  
     2\. \*\*Optimization of implementation solutions for related domain modules\*\*: for the functional modules related to your domain, propose detailed optimization solutions, improvement suggestions, or new solutions.  
     3\. \*\*Impact assessment of cross-domain modules\*\*: list the impact assessment of unrelated domain modules and suggestions for improvement.

5\. \*\*Response to Questions\*\*.  
   \- In the Summary and Recommendations, make sure that your answers have incorporated a response to \[User question\], ensure that all questions are clearly answered, and make practical recommendations based on your professional background.

\[User question\]  
{{expert4\_q}}

\[Output\]  
1\. \*\*Formatted Output\*\*:  
   \- Functional module additions  
   \- Optimization of implementation options for related domain modules  
   \- Impact assessment of cross-domain modules

2\. \*\*Integration of responses\*\*:  
   \- Integrate responses to \[User question\] into the analysis and optimization of related domain modules to ensure that all questions are clearly responded to.

Please note that your answers will provide the basis for the first round of discussion, with subsequent opportunities to interact and go deeper with other experts.

Brainstorming \- Round 2  
\<...Brainstorming round 2 and 3 as above…\>

Brainstorming \- Summary  
As the summarizer of this project, your task is to integrate all expert opinions from the third round of discussions and generate a comprehensive final summary report. Please make sure that the summary includes the final recommendations of each expert, the key conflicts in the discussion and their solutions, and provides a comprehensive design optimization plan.

\[Background\]  
Expert Identification Information  
\- Expert1.   
{{expert\_1}}

\- Expert 2: {{expert\_2}}   
{{expert\_2}}

\- Expert 3\.   
{{expert\_3}}

\- Expert 4\.   
{{expert\_4}}

Design Tasks: {{requirement}}  
{{requirement}}

Function Module:  
{{module\_combined}}

Morphological matrix after optimization from the first two rounds of discussions: {{round2}}  
{{round2}}

\[Elements of the third round of discussion\]\]  
Expert 1's final recommendation: {{expert1\_a}}  
{{expert1\_a}}

Expert 2's final recommendation: {{expert2\_a}}  
{{expert2\_a}}

Expert 3's final recommendation: {{expert3\_a}}  
{{expert3\_a}}

Expert 4's final recommendation: {{expert4\_a}}  
{{expert4\_a}}

\[Thought Process\]  
1\. \*\*Summarize the third round of discussion\*\*:  
   \- Synthesize the 2 combinations proposed by each expert and analyze their advantages and disadvantages.  
   \- Combining the analysis of each expert, based on the “Optimized Morphology Matrix after the first two rounds of discussion”, the 3 best combinations are selected to ensure that they have the best balance in terms of overall performance, technical feasibility, innovation, and fit with the design brief.

\[Output\]  
1\. \*\*Morphology matrix after brainstorming optimization\*\*:  
   \- Complete output of the optimized morphological matrix from the first two rounds of discussion without any modifications.  
   \- Ensure that the final recommended combinatorial solution is wrapped between the identifiers \`\<brainstormed optimized morphology matrix\>\` and \`\</brainstormed optimized morphology matrix\>\`.

2\. \*\*Final recommended combination scheme\*\*:  
   \- List the 3 best combination scenarios, with each scenario explicitly listing the implementation scenarios chosen for each functional module (do not write that implementation scenario 1 was chosen, but rather what exactly implementation scenario 1 is).  
   \- Ensure that the final recommended combination solution is wrapped between the identifiers \`\<recommended combination solution\>\` and \`\</recommended combination solution\>\`.  
   \- Example output format:  
     \`\`\`  
     \<recommended combination scheme\>  
     Combination Scheme 1:  
     \- Function Module 1: Choose to implement scenario X  
     \- Function Module 2: Select Implementation Y  
     (Note: list all functional modules)  
       
     Combination Scenario 2:  
     \- Function Module 1: Choose to implement Option A  
     \- Function Module 1: Select to implement Option A Function Module 2: Select to implement Option B  
     (Note: list all function modules)

     Combined Scenario 3:  
     \- Function Module 1: Choose to realize Option M  
     \- Function Module 2: Choose to implement Option N  
     (Note: list all function modules)  
     \</recommended combination scenario  
     \`\`\`

User Selection  
\- The full brainstorming analysis has been completed.  
\- If you are not satisfied, you can re-enter \[Brainstorm, Summarize\] to achieve a summary.  
\- If you are satisfied, please continue to enter \[Bionic Design\] in the dialog box to continue working on concept generation.
