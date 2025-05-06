##  Axiom 1 – Coupling Analysis via DSM Matrix

To assess the degree of interdependency among functional modules, we use a normalized coupling metric derived from the Design Structure Matrix (DSM):

```math
C = \frac{1}{n} \sum_{i=1}^{n} \left( \frac{\text{Internal Connections of Module } i}{\text{Total Possible Connections}} \right)
```

**Where:**
- *n* is the number of functional modules.  
- *C* is the **normalized coupling coefficient**, ranging from **0% to 100%**.

> **Note:** Higher values of $C$ indicate **stronger coupling** between modules, which may hinder modularity and increase system complexity.

---

###  Ref.

Fazeli, H. R. & Peng, Q.  Generation and evaluation of product concepts by integrating extended axiomatic design, quality function deployment and design structure matrix. *Advanced Engineering Informatics* **54**, 101716 (2022).
