# TELCO CUSTOMER CHURN ANALYSIS

## 1. Churn Distribution Analysis

### Insight

Out of 7032 customers, 1869 customers churned while 5163 customers remained with the company.

The dataset is moderately imbalanced, with non-churn customers representing the majority of the customer base. This indicates that customer retention is generally strong, but a significant portion of customers still leave the company, making churn prediction an important business problem.

---

## 2. Tenure Months vs Churn Analysis

### Insight

Customers who churned had significantly lower tenure compared to customers who stayed with the company.

The average tenure of churned customers was approximately 18 months, whereas retained customers stayed for approximately 38 months. This indicates that newly acquired customers are more likely to leave, while long-term customers tend to remain loyal.

Tenure was identified as one of the strongest indicators of customer retention.

---

## 3. Monthly Charges vs Churn Analysis

### Insight

Customers with higher monthly charges showed a higher tendency to churn.

The average monthly charges for churned customers were significantly higher than those of retained customers. This suggests that expensive service plans may contribute to customer dissatisfaction and increase churn risk.

Pricing strategy and customer value perception may play an important role in customer retention.

---

## 4. Contract Type vs Churn Analysis

### Insight

Month-to-Month contract customers exhibited the highest churn rate among all contract categories.

Customers with One-Year and Two-Year contracts were significantly less likely to churn, indicating that long-term contracts improve customer retention and customer commitment.

This finding highlights the importance of encouraging customers to move toward longer contract plans.

---

## 5. Payment Method vs Churn Analysis

### Insight

Customers using Electronic Check as their payment method showed the highest churn percentage compared to all other payment methods.

This suggests a strong association between Electronic Check payments and customer attrition. Customers using automatic payment methods such as bank transfer and credit card demonstrated lower churn rates.

This customer segment may require targeted retention strategies.

---

## 6. Internet Service vs Churn Analysis

### Insight

Customers using Fiber Optic internet services experienced the highest churn rate among all internet service categories.

Customers without internet services had the lowest churn rate. This indicates that Fiber Optic customers may have higher service expectations, making them more likely to leave if those expectations are not met.

Improving service quality for Fiber Optic customers could potentially reduce churn.

---

## 7. Online Security vs Churn Analysis

### Insight

Customers without Online Security services churned at a significantly higher rate than customers who subscribed to Online Security.

The analysis suggests that customers using Online Security services perceive greater value from the company and are therefore more likely to remain loyal.

Online Security acts as an important customer retention factor.

---

## 8. Tech Support vs Churn Analysis

### Insight

Customers without Tech Support services exhibited substantially higher churn rates.

Customers who received Tech Support were more likely to remain with the company, indicating that support services play an important role in customer satisfaction and retention.

Providing quality technical support can reduce customer attrition.

---

## 9. Online Backup vs Churn Analysis

### Insight

Customers without Online Backup services showed significantly higher churn behavior compared to customers who subscribed to Online Backup.

Additional value-added services increase customer engagement and improve retention rates.

Online Backup was identified as an important retention-related feature.

---

## 10. Device Protection vs Churn Analysis

### Insight

Customers without Device Protection services demonstrated higher churn rates than customers who subscribed to Device Protection.

This finding suggests that customers utilizing additional protection services are more invested in the company's offerings and are therefore less likely to leave.

Device Protection contributes positively to customer retention.

---

## 11. Paperless Billing vs Churn Analysis

### Insight

Customers using Paperless Billing exhibited a higher churn rate compared to customers who did not use Paperless Billing.

Although Paperless Billing provides convenience, this customer segment displayed greater churn behavior and may require additional retention efforts.

---

## 12. Model Comparison Analysis

### Models Evaluated

1. Logistic Regression
2. K-Nearest Neighbors (KNN)
3. Decision Tree
4. Random Forest
5. AdaBoost
6. Gradient Boosting
7. XGBoost

### Model Performance

* Logistic Regression = 80.67%
* AdaBoost = 80.59%
* Random Forest = 79.82%
* Gradient Boosting = 79.74%
* XGBoost = 78.53%
* Decision Tree = 74.34%
* KNN = 73.70%

### Insight

Multiple machine learning algorithms were evaluated and compared.

Logistic Regression achieved the highest overall accuracy and demonstrated consistent performance across validation and testing datasets.

Therefore, Logistic Regression was selected as the final model for deployment and business interpretation.

---

## 13. Hyperparameter Tuning

### Logistic Regression

Best Parameters:

* C = 0.1
* Penalty = L2

Best Cross Validation Score:

0.8099

### AdaBoost

Best Parameters:

* Learning Rate = 0.5
* Number of Estimators = 300

Best Cross Validation Score:

0.8062

### Insight

GridSearchCV was used to identify the optimal hyperparameters for the top-performing models.

The tuned Logistic Regression model maintained the highest performance and remained the final selected model.

---

## 14. Confusion Matrix Analysis

### Results

True Negatives = 913

False Positives = 120

False Negatives = 151

True Positives = 223

### Insight

The final Logistic Regression model correctly classified 913 non-churn customers and 223 churn customers.

The model demonstrated strong predictive capability while maintaining a balanced performance across both customer classes.

Overall model accuracy was approximately 81%.

---

## 15. Classification Report Analysis

### Results

Accuracy = 80.7%

Class 1 (Churn):

* Precision = 65%
* Recall = 60%
* F1 Score = 62%

### Insight

When the model predicts that a customer will churn, it is correct approximately 65% of the time.

The model successfully identifies approximately 60% of actual churn customers.

The F1 Score demonstrates a balanced trade-off between precision and recall, making the model suitable for churn prediction tasks.

---

## 16. ROC-AUC Analysis

### Results

Logistic Regression ROC-AUC = 0.844

AdaBoost ROC-AUC = 0.845

### Insight

Both Logistic Regression and AdaBoost achieved excellent ROC-AUC scores of approximately 0.84.

This indicates strong capability in distinguishing churning customers from non-churning customers.

Although AdaBoost achieved a marginally higher ROC-AUC score, Logistic Regression was selected due to its higher accuracy, simplicity, and interpretability.

---

## 17. Feature Importance Analysis (Logistic Regression Coefficients)

### Features Increasing Churn Probability

* Fiber Optic Internet Service
* Electronic Check Payment Method
* Paperless Billing
* Multiple Lines
* Senior Citizen

### Features Reducing Churn Probability

* Dependents
* Two-Year Contract
* One-Year Contract
* Online Security
* Tech Support
* Online Backup

### Insight

The Logistic Regression coefficients revealed that customers with Fiber Optic Internet, Electronic Check payments, and Paperless Billing were more likely to churn.

Customers with Dependents, long-term contracts, Online Security, and Tech Support services were significantly less likely to leave the company.

These findings closely aligned with the insights discovered during Exploratory Data Analysis.

---

# Final Business Conclusion

The analysis identified several key factors influencing customer churn.

Customers with Month-to-Month contracts, Fiber Optic Internet services, Electronic Check payment methods, higher monthly charges, and lower tenure were significantly more likely to churn.

On the other hand, customers with Dependents, One-Year or Two-Year contracts, Online Security services, Tech Support services, and longer tenure demonstrated stronger retention behavior.

A comprehensive machine learning pipeline was developed including data cleaning, exploratory data analysis, feature engineering, model comparison, hyperparameter tuning, and performance evaluation.

Among all evaluated algorithms, Logistic Regression achieved the best balance of accuracy, interpretability, and business value.

The final model achieved approximately 81% accuracy and a ROC-AUC score of 0.84, making it a reliable solution for identifying customers at risk of churn and supporting proactive customer retention strategies.
