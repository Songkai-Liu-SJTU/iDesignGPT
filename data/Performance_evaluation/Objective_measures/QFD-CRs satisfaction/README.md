##  QFD-CRs Satisfaction Score

To evaluate how well each design satisfies customer requirements, we compute a weighted average score based on the QFD (Quality Function Deployment) framework:

```math
S = \frac{1}{3} \sum_{j=1}^{3} \left( \sum_{i=1}^{n} w_i \cdot s_i^{(j)} \right)
```

**Note:**
- $w_i$ is the **weight** of customer requirement *i*.
- $s_i^{(j)}$ is the **score** (1, 3, or 5) assigned to the *i*-th requirement in evaluation round *j*.
- The final score $S$ is the **average of three evaluation rounds**.
- A **higher score** indicates **better satisfaction** of customer requirements.

---

###  Ref.

Nahm, Y.-E., Ishikawa, H. & Inoue, M.  New rating methods to prioritize customer requirements in QFD with incomplete customer preferences.  *The International Journal of Advanced Manufacturing Technology* **65**, 1587–1604 (2013).
