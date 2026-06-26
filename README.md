# AI-on-cloud-Sagemaker
# ☁️ AI on Cloud using AWS SageMaker

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)

---

# 📌 Project Overview

**AI on Cloud using AWS SageMaker** is an end-to-end Machine Learning project developed to predict customer churn using the **IBM Telco Customer Churn Dataset**.

The project follows an industry-inspired Machine Learning workflow, including:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Model Training
- Model Evaluation
- Scikit-learn Pipeline
- REST API Development using FastAPI
- Interactive Streamlit Dashboard
- SQLite Database Integration
- AWS SageMaker Deployment Architecture (Conceptual)

Although the implementation runs entirely on a local machine, the project architecture is designed to mirror how it can be deployed using **AWS SageMaker**.

---

# 🎯 Project Objectives

- Build a complete Machine Learning pipeline.
- Compare multiple classification algorithms.
- Select the best-performing model.
- Deploy the model through a FastAPI REST API.
- Create an interactive Streamlit web application.
- Store prediction history in SQLite.
- Demonstrate how the same workflow maps to AWS SageMaker.

---

# 🚀 Features

- ✅ Data Cleaning & Preprocessing
- ✅ Exploratory Data Analysis (EDA)
- ✅ Feature Engineering
- ✅ Machine Learning Model Comparison
- ✅ Logistic Regression
- ✅ Random Forest
- ✅ Gradient Boosting
- ✅ XGBoost
- ✅ Scikit-learn Pipeline
- ✅ FastAPI Backend
- ✅ Streamlit Frontend
- ✅ SQLite Prediction History
- ✅ Local Architecture Diagram
- ✅ AWS SageMaker Architecture Diagram

---

# 🛠 Tech Stack

## Programming Language

- Python 3.11

## Machine Learning

- Scikit-learn
- XGBoost
- Pandas
- NumPy

## Backend

- FastAPI
- Pydantic

## Frontend

- Streamlit

## Database

- SQLite
- SQLAlchemy

## Data Visualization

- Matplotlib
- Seaborn

## Version Control

- Git
- GitHub

---

# 📂 Project Structure

```text
AI-on-cloud-Sagemaker/
│
├── app/
│   ├── app.py
│   ├── api_client.py
│   ├── ui_components.py
│   └── utils.py
│
├── artifacts/
│   ├── churn_pipeline.pkl
│   ├── X_test.pkl
│   └── y_test.pkl
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   ├── architecture/
│   │   ├── local_architecture.png
│   │   └── aws_architecture.png
│   │
│   └── screenshots/
│       ├── dashboard_home.png
│       ├── prediction_result.png
│       ├── prediction_history.png
│       └── fastapi_docs.png
│
├── reports/
│
├── src/
│   ├── api/
│   ├── data/
│   ├── database/
│   └── models/
│
├── predictions.db
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 📊 Dataset

**Dataset:** IBM Telco Customer Churn Dataset

### Dataset Information

- Total Records: **7,043**
- Features: **20**
- Target Variable: **Churn**
- Problem Type: **Binary Classification**

### Objective

Predict whether a customer is likely to churn based on demographic information, subscribed services, billing details, and contract information.

---

# 🤖 Machine Learning Workflow

```text
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Engineering
      │
      ▼
Train/Test Split
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Best Model Selection
      │
      ▼
Scikit-learn Pipeline
      │
      ▼
FastAPI Backend
      │
      ▼
Streamlit Dashboard
```

---

# 🏆 Machine Learning Models

The following models were trained and evaluated:

- Logistic Regression
- Random Forest
- Gradient Boosting
- XGBoost

## Best Model

**Logistic Regression**

### Model Performance

| Metric | Score |
|---------|--------|
| Accuracy | 80.55% |
| Precision | 65.72% |
| Recall | 55.88% |
| F1 Score | 60.40% |
| ROC-AUC | 0.8416 |

---

# 🌐 REST API Endpoints

| Method | Endpoint | Description |
|----------|----------------|------------------------------|
| GET | `/` | Home Endpoint |
| GET | `/health` | Health Check |
| POST | `/predict` | Predict Customer Churn |
| GET | `/history` | View Prediction History |

---

# ☁ Local vs AWS SageMaker

| Local Implementation | AWS Equivalent |
|----------------------|----------------|
| VS Code | SageMaker Studio |
| train.py | SageMaker Training Job |
| Scikit-learn Pipeline | SageMaker Model Artifact |
| FastAPI API | SageMaker Endpoint (or custom inference service) |
| SQLite | Amazon RDS |
| Local Storage | Amazon S3 |
| Streamlit | Amazon EC2 / AWS Amplify |

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Resh2509/AI-on-cloud-Sagemaker.git
```

Navigate to the project folder

```bash
cd AI-on-cloud-Sagemaker
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Application

## Start FastAPI

```bash
python -m uvicorn src.api.main:app --reload
```

Open Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Start Streamlit

```bash
streamlit run app/app.py
```

---

# 💾 Prediction Storage

Every prediction generated by the application is stored in an SQLite database.

Stored information includes:

- Prediction Result
- Prediction Probability
- Risk Level
- Timestamp

The prediction history can be viewed through:

```
GET /history
```

or directly from the Streamlit dashboard.

---

# 🔮 Future Improvements

- Docker Containerization
- CI/CD Pipeline
- Automated Model Retraining
- Model Monitoring
- Cloud Deployment using AWS SageMaker
- User Authentication
- PostgreSQL / Amazon RDS Integration
- Real-time Model Monitoring

---

# 👩‍💻 Author

## Reshma R

**B.Tech – Artificial Intelligence and Data Science**

🔗 GitHub: https://github.com/Resh2509

🚀 Exploring New Technologies

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
