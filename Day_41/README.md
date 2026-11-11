# Day 41 — Dimensionality Reduction with PCA

## Learning Objectives

- Understand dimensionality reduction.
- Understand Principal Component Analysis (PCA).
- Learn about principal components and explained variance.
- Apply PCA using Scikit-learn.
- Visualize high-dimensional data in two dimensions.
- Combine PCA with K-Means clustering.

## Topics Covered

1. Introduction to dimensionality
2. Reasons for dimensionality reduction
3. Principal Component Analysis
4. Variance and principal components
5. Feature standardization
6. PCA with Scikit-learn
7. Explained variance ratio
8. Cumulative explained variance
9. Automatic component selection
10. Data reconstruction and reconstruction error

## Files

- `41_dimensionality_reduction_pca.ipynb` — lesson and practical exercises

## Libraries

- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## Practical Work

- Loaded the Iris dataset.
- Standardized the original features.
- Reduced four dimensions to two using PCA.
- Visualized the principal components.
- Calculated explained and cumulative variance.
- Experimented with automatic component selection.
- Reconstructed data and calculated reconstruction error.

## Key Takeaways

- Dimensionality refers to the number of features.
- PCA transforms original features into principal components.
- Principal components capture variance in descending order.
- Standardization is important when features have different scales.
- Explained variance helps determine how many components to retain.
- PCA can simplify data but may also discard useful information.

## GitHub

```bash
git add Day_41/
git commit -m "Complete Day 41 dimensionality reduction with PCA"
git push
```
