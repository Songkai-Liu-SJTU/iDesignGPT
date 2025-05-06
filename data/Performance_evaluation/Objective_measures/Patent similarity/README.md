##  Patent Similarity Measurement

Patent similarity is calculated based on the **semantic similarity** between a generated design proposal and a set of retrieved patents. The process consists of the following three stages:

1. **Patent Retrieval**  
   Three sets of domain-relevant keywords are used to query the patent database. For each set, the top 5 most relevant patents are retrieved (total of 15 patents). The **titles and abstracts** of these patents are embedded using OpenAI’s `text-embedding-3-large` model.

2. **Design-to-Patent Matching**  
   The design proposal is semantically embedded and searched against the knowledge base. The **top 5 most similar patents** are identified based on cosine similarity.

3. **Similarity Computation**  
   The final similarity score is computed as the **average cosine similarity** between the design vector and its 5 nearest patent neighbors:

```math
S = \frac{1}{5} \sum_{i=1}^{5} \cos\left( \mathbf{v}_{\text{design}},\ \mathbf{v}_{\text{patent}}^{(i)} \right)
```

   where:
   - $\mathbf{v}_{\text{design}}$: semantic vector representation of the design proposal  
   - $\mathbf{v}_{\text{patent}}^{(i)}$: semantic vector of the *i*-th closest patent

The similarity score $S$ ranges from 0 to 1, where higher values indicate **closer alignment with existing patent knowledge**, and lower values suggest greater novelty.

---

###  Ref.

Wang, L. *et al.* Improving text embeddings with large language models. *arXiv preprint* arXiv:2401.00368 (2023).
