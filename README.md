# 🧠 Machine Learning Project — Student Exam Performance Prediction

Welcome to the **MachineLearning** repository — a complete end-to-end Machine Learning project built using Python and Flask.  
This project predicts **student exam performance** based on multiple factors like gender, parental education level, lunch type, and test preparation course completion.


## 🎯 Problem Statement
The goal of this project is to predict the **student’s exam score** based on other influencing variables.  
It helps to understand how a student's performance is affected by factors such as:
- Gender  
- Ethnicity  
- Parental level of education  
- Lunch type  
- Test preparation course  


## 📊 Dataset
- **Dataset Source:** [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)  
- **Dataset Size:** 1000 rows × 8 columns  
- **Target Variable:** `math_score` (or final exam score)  


## 🚀 Project Workflow

1. **Data Collection & Cleaning**  
   - Load raw data from CSV  
   - Handle missing values, duplicates, and data types  
   - Explore unique values and summary statistics  

2. **Exploratory Data Analysis (EDA)**  
   - Visualize data distributions and relationships  
   - Perform univariate, bivariate, and multivariate analysis  

3. **Data Transformation & Normalization**  
   - Convert categorical variables using **OneHotEncoder**  
   - Apply **Z-Score Normalization** for scaling  

4. **Model Training & Evaluation**  
   Implemented and compared multiple regression models:
   - Linear Regression  
   - Ridge & Lasso Regression  
   - K-Nearest Neighbors (KNN)  
   - Decision Tree  
   - Random Forest  
   - XGBoost  
   - CatBoost  
   - AdaBoost  

   Evaluated using metrics:
   - Mean Absolute Error (MAE)  
   - Mean Squared Error (MSE)  
   - Root Mean Squared Error (RMSE)  
   - R² Score  

5. **Model Deployment (Flask App)**  
   - A user-friendly Flask web interface for real-time prediction.  
   - Users can input parameters like gender, lunch type, parental education, etc.  
   - The trained model predicts the expected exam performance instantly.


## 🧩 Technologies Used
- Language - Python 3.8
- Framework - Flask
- Data Handling - Pandas, NumPy 
- Visualization - Matplotlib, Seaborn 
- Machine Learning - Scikit-learn, XGBoost, CatBoost
- Frontend - HTML, CSS
- Version Control - Git, GitHub


## 💻 How to Run the Project

### 🧩 Prerequisites
- Python 3.8
- pip (or conda)  
- Git  

### ⚙️ Setup
1. Clone the repository
    - git clone https://github.com/Mystery-glitch/MachineLearning.git
    - cd MachineLearning
2. Create virtual environment (optional)
3. Install dependencies - pip install -r requirements.txt
4. Run the Flask app - python app.py
5. Open your browser and go to http://127.0.0.1:5000/predictdata
