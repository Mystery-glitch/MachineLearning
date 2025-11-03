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
Language - Python 3.8
Framework - Flask
Data Handling - Pandas, NumPy 
Visualization - Matplotlib, Seaborn 
Machine Learning - Scikit-learn, XGBoost, CatBoost
Frontend - HTML, CSS
Version Control - Git, GitHub


## ⚙️ Project Structure
MachineLearning/
│
├── notebook/ # Jupyter notebooks for EDA and experimentation
│ ├── EDA.ipynb
│ ├── Model.ipynb
│ ├── stud.csv
│
├── src/ # Source code for ML pipeline
│ ├── components/ # Data ingestion, transformation, and model training
│ │ ├── data_ingestion.py
│ │ ├── data_transformation.py
│ │ └── model_trainer.py
│ │
│ ├── pipeline/ # Pipeline scripts for training & prediction
│ │ ├── predict_pipeline.py
│ │ └── init.py
│ │
│ ├── utils.py # Utility functions
│ ├── exception.py # Custom exception handling
│ ├── logger.py # Logging utilities
│ └── init.py
│
├── templates/ # HTML templates for Flask app
│ ├── home.html
│ └── index.html
│
├── static/ # Static assets (CSS, images)
│ └── style.css
│
├── app.py # Flask app entry point
├── application.py # Secondary app configuration
├── requirements.txt # Dependencies
├── setup.py # Setup script
├── .gitignore # Ignored files
└── README.md # Project documentation