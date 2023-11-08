# Apontamentos

### Model's metrics and their meanings
- **Precison:** rate of false positives (it's inverse). Higher precision, lower rate of false-positives
-  **Recal:** Ratio of True positives. 
- **F1-Score:** It's an harmonic mean of precision and recall. it provides a balance between the 2 other metrics. Helpful when one metric is more critical than the other
- **Confusin matrix:** Matrix (2x2) which informs us on true-positive, flase-positive, false-negative adn false-positive prediciton
- **Mean Accuracy:** Overall performance across multiple cross-validation folds. Doesn't dive deep and doens't differentiate between false positives and false negatives
- **Standard Ddeviation:** it measures the variability or spread of the accuracy. A lower standard deviation means that the model's performance is relatevely more consistent across diferent subsets of data.