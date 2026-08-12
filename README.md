# Curriculum-Industry Skill Feature Store Using Feast

## Student Details

**Name:** Harshini Vemula  
**Register Number:** 231FA04A87 
**Section:** 09

---

## Problem Statement

The curriculum-industry skill-gap problem focuses on identifying the difference between the skills developed by students through their academic curriculum and the skills expected by industry.

This project converts a curriculum-industry skill-gap dataset into a simple Feast-based feature store. The feature store is used for historical feature retrieval, machine-learning model training, feature materialization, online feature retrieval, and final prediction.

---

## Objective

The main objectives of this project are:

1. Perform feature engineering on a curriculum-industry skill-gap dataset.
2. Create a Feast entity.
3. Create a Feast data source.
4. Create a Feast FeatureView.
5. Register the features using `feast apply`.
6. Retrieve historical features.
7. Materialize features into the online store.
8. Retrieve features from the online store.
9. Use Feast features in a machine-learning model.
10. Document the complete implementation.

---

# Dataset

The dataset contains **800 student records**.

## Number of Skills

The dataset contains 15 student skill features:

1. Programming
2. DSA
3. DBMS
4. Computer Networks
5. Operating Systems
6. Web Development
7. Data Analytics
8. AI/ML
9. Cloud Computing
10. Cybersecurity
11. Problem Solving
12. Aptitude
13. Communication
14. Teamwork
15. Git/GitHub

## Dataset Columns

The dataset contains the following columns:

- `Student_ID`
- `event_timestamp`
- `Programming`
- `DSA`
- `DBMS`
- `Computer_Networks`
- `Operating_Systems`
- `Web_Development`
- `Data_Analytics`
- `AI_ML`
- `Cloud_Computing`
- `Cybersecurity`
- `Problem_Solving`
- `Aptitude`
- `Communication`
- `Teamwork`
- `Git_GitHub`
- `technical_skill_average`
- `programming_problem_solving`
- `data_ai_average`
- `cloud_security_average`
- `soft_skill_average`
- `overall_skill_average`
- `Overall_Industry_Gap`
- `Curriculum_Alignment_Score`
- `Industry_Alignment_Score`
- `Skill_Gap_Category`

## Target

The target variable is:

`Skill_Gap_Category`

The target contains three categories:

- Low Gap
- Medium Gap
- High Gap

## Dataset Creation

The original dataset from the previous activity was not available in the current environment. Therefore, an 800-student dataset was recreated for this Feast implementation.

The skill scores were generated on a 0–100 scale. The engineered features were calculated using the feature-engineering formulas used in the project.

The dataset was then converted into Parquet format for use as the Feast offline data source.

---

# Feature Engineering

Feature engineering was performed to create meaningful aggregated features from the original student skill scores.

## 1. technical_skill_average

This feature represents the average technical skill level of a student.

It is calculated using:

- Programming
- DSA
- DBMS
- Computer Networks
- Operating Systems
- Web Development
- Data Analytics
- AI/ML
- Cloud Computing
- Cybersecurity

```text
technical_skill_average =
mean of the 10 technical skills



2. programming_problem_solving

This feature represents the combined programming and problem-solving strength of a student.

It is calculated as:

programming_problem_solving =
mean(Programming, DSA, Problem_Solving)
3. data_ai_average

This feature represents the student's combined Data Analytics and AI/ML strength.

data_ai_average =
mean(Data_Analytics, AI_ML)
4. cloud_security_average

This feature represents the student's combined Cloud Computing and Cybersecurity strength.

cloud_security_average =
mean(Cloud_Computing, Cybersecurity)
5. soft_skill_average

This feature represents the student's soft-skill strength.

It is calculated using:

Communication
Teamwork
soft_skill_average =
mean(Communication, Teamwork)
6. overall_skill_average

This feature represents the overall skill level of a student.

It is calculated as the average of all 15 skill features.

7. overall_industry_gap

This feature represents the estimated difference between the student's industry-oriented skills and the expected industry skill level.

A higher value represents a larger estimated industry skill gap.

8. curriculum_alignment_score

This feature represents how well the student's skills align with the curriculum-oriented skill profile.

The value is represented on a 0–100 scale.

9. industry_alignment_score

This feature represents how well the student's skills align with industry-oriented skills.

The value is represented on a 0–100 scale.

Feast Architecture
                 Original Dataset
                       |
                       v
              Feature Engineering
                       |
                       v
             Parquet Offline Data
                       |
                       v
                Feast FeatureView
                       |
              +--------+--------+
              |                 |
              v                 v
    Historical Features    Materialization
              |                 |
              v                 v
       Model Training      Online Store
                                |
                                v
                         Online Retrieval
                                |
                                v
                            Prediction
Feast Implementation
1. Entity

The Feast entity is:

student_id

It uniquely identifies each student in the feature store.

The entity is used as the join key for retrieving features.

2. Data Source

The Feast data source is the Parquet file:

data/student_features.parquet

The timestamp field used by Feast is:

event_timestamp

The Parquet file acts as the local offline feature data source.

3. FeatureView

The FeatureView is:

student_skill_features

The FeatureView contains the 15 original skill features and the engineered features.

The FeatureView contains the following 24 Feast features:

Programming
DSA
DBMS
Computer_Networks
Operating_Systems
Web_Development
Data_Analytics
AI_ML
Cloud_Computing
Cybersecurity
Problem_Solving
Aptitude
Communication
Teamwork
Git_GitHub
technical_skill_average
programming_problem_solving
data_ai_average
cloud_security_average
soft_skill_average
overall_skill_average
overall_industry_gap
curriculum_alignment_score
industry_alignment_score
4. Offline Store

The offline feature data is stored in Parquet format.

The offline store is used for:

Storing historical feature values
Historical feature retrieval
Preparing training data for machine-learning models
5. Online Store

The project uses a local SQLite online store.

The online store contains materialized feature values and is used for online feature retrieval during prediction.

6. Feature Registration

The Feast entities and FeatureView were registered using:

feast apply

The command successfully created:

Feast project
student_id entity
student_skill_features FeatureView
SQLite feature table
7. Historical Feature Retrieval

Historical features were retrieved using:

store.get_historical_features()

The historical features were retrieved from the Feast offline data source.

These features were then used for machine-learning model training.

8. Machine-Learning Model

A Decision Tree Classifier was used as the machine-learning model.

The model was trained using the historical Feast features.

The target variable was:

Skill_Gap_Category

The dataset was divided into:

80% training data
20% testing data
9. Materialization

Feast materialization was performed to load historical feature values into the SQLite online store.

The materialization process successfully completed for the available feature data.

The materialization range was:

2025-01-01 00:00:00
to
2025-02-03 08:00:00
10. Online Feature Retrieval

Online features were retrieved using:

store.get_online_features()

The features were retrieved for:

student_id = S0001

The retrieved online features were then passed to the trained machine-learning model.

