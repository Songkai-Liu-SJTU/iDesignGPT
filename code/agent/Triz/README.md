
![s5-triz](https://github.com/user-attachments/assets/bf4d2f37-f092-4c9b-9da6-4644e0b9952b)

## **Execution logic**
  The TRIZ module systematically resolves design contradictions through structured inventive reasoning. Upon trigger, the process begins with engineering parameter identification, referencing the standardized 39-parameter TRIZ framework. These parameters are extracted from the user-provided requirement description via text content analysis. A pair of parameters, one to be optimized and one allowed to deteriorate, is submitted to the TRIZ contradiction matrix, implemented through an embedded JavaScript routine, which returns a set of inventive principles from the canonical list of 40.
  
  The matched principles are then queried against a TRIZ knowledge base using a Retrieval-Augmented Generation (RAG) strategy. This step enriches the result with semantically relevant cases and explanatory content beyond exact matches. Retrieved principles are categorized into (1) direct responses to the contradiction query and (2) RAG-suggested auxiliary principles. A reasoning agent interprets the resulting set, filters out uninformative principles, and applies the relevant ones to context-specific modules.
  
  Optimization proposals are subsequently generated and organized according to the existing morphological structure. Users evaluate the outputs and, if needed, may prompt a re-run with revised parameter prioritization. Upon confirmation, TRIZ-informed outputs proceed to the next method in the synthesis pipeline.
