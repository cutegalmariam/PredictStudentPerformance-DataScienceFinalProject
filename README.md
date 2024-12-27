# Predict Student Performance - Data Science Final Project

## **Objective**

The goal of this project is to predict secondary school students' final grades (**G3**) based on various factors such as study time, parental education, and lifestyle choices (e.g., alcohol consumption). By analyzing and visualizing the data, we aim to uncover key insights and develop a predictive model for student performance.

---

## **Overview**

This project uses a dataset of student performance to:

- Conduct exploratory data analysis (EDA) to understand the key factors influencing academic outcomes.
- Train machine learning models to predict students' final grades (**G3**).
- Visualize feature importance to identify the most significant predictors of student success.

---
## **Key Analyses**

1. **Correlation Analysis**
    
    - Explore the relationship between **study time** and **G3**.
    - Analyze how the number of **failures** impacts final grades.
2. **Parental Influence**
    
    - Investigate how **Medu** (mother’s education) and **Fedu** (father’s education) affect students' academic performance.
3. **Demographic Comparisons**
    
    - Compare academic performance based on:
        - **Gender (sex)**
        - **Urban vs. Rural residence (address)**

---
## **Dataset**

**Source**: [Student Performance Data on Kaggle](https://www.kaggle.com/datasets/devansodariya/student-performance-data)  
The dataset was collected through a survey of students enrolled in a math course in secondary schools in Singapore. It contains various socio-economic and academic attributes of the students.

---


## **Project Workflow**

### **1. Data Loading and Preprocessing**

- Load the dataset from `Data/Maths.xlsx`.
- Clean and preprocess the data (e.g., encoding categorical variables, handling missing values).

### **2. Exploratory Data Analysis (EDA)**

- Visualize the dataset to understand relationships between variables.
- Insights are derived from correlations, distribution plots, and comparative analyses.

### **3. Model Training**

- Train two models:
    - **Linear Regression** for interpretable predictions.
    - **Random Forest** for feature importance and robust predictions.
- Evaluate model performance.

### **4. Visualization**

- Visualize feature importance to highlight the factors most critical for predicting **G3**.

---

## **Charts and Insights**

1. **Study Time vs. G3**
    
    - A scatter plot showing a positive correlation between study time and final grades. Students who dedicate more time to studying tend to perform better.
2. **Failures vs. G3**
    
    - A boxplot reveals that students with higher numbers of failures generally achieve lower final grades, highlighting the cumulative impact of academic challenges.
3. **Parental Education (Medu, Fedu) vs. G3**
    
    - Bar charts demonstrate that students with more educated parents (higher Medu and Fedu scores) tend to achieve better grades.
4. **Gender and Address Impact**
    
    - Comparative plots show differences in performance:
        - **Gender**: Insights into whether male or female students perform better.
        - **Urban vs. Rural**: Analyze how living location influences academic outcomes.


---
## **Requirements**

### **Setup**

To run the project, install the dependencies using `requirements.txt`:

bash

Copy code

`pip install -r requirements.txt`

### **Dependencies**

- **Python 3.8+**
- Libraries:
    - pandas
    - numpy
    - scikit-learn
    - seaborn
    - matplotlib
    - pillow

---

## **How to Run**

1. Clone the repository:
    
    `git clone https://github.com/cutegalmariam/PredictStudentPerformance-DataScienceFinalProject.git`
    
2. Navigate to the project directory:
    
    `cd PredictStudentPerformance-DataScienceFinalProject`
    
3. Run the main script:
    
    `python main.py`
    

---

## **Conclusion**

This project provides a comprehensive analysis of factors influencing students’ academic performance and demonstrates the use of machine learning to make accurate predictions. The insights can help educators and policymakers design interventions to improve educational outcomes.
