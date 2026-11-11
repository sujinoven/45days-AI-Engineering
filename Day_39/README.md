# Day 39 — Model Evaluation, Cross-Validation and Hyperparameter Tuning

## Learning Objectives

- Understand model evaluation and overfitting.
- Calculate classification metrics.
- Understand train/test splitting and cross-validation.
- Tune hyperparameters using GridSearchCV and RandomizedSearchCV.
- Compare machine learning models.

## Topics Covered

1. Training and testing performance
2. Overfitting and underfitting
3. Accuracy, precision, recall and F1 score
4. Confusion matrix and classification report
5. Stratified K-fold cross-validation
6. Decision tree hyperparameters
7. GridSearchCV
8. RandomizedSearchCV
9. Model comparison

## Files

- `39_model_evaluation_tuning.ipynb` — lesson and practical exercises

## Libraries

- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## Practical Work

- Trained a baseline decision tree.
- Evaluated classification performance.
- Used cross-validation.
- Tuned a decision tree with GridSearchCV.
- Tuned a random forest with RandomizedSearchCV.
- Compared models on a separate test set.

## Key Takeaways

- Training accuracy alone does not establish model quality.
- Cross-validation helps estimate performance more reliably.
- Hyperparameters influence model behavior.
- Grid search tests specified combinations; randomized search samples combinations.
- Keep the test set separate until final evaluation.

## GitHub

```bash
git add Day_39/
git commit -m "Complete Day 39 model evaluation and tuning"
git push
```
