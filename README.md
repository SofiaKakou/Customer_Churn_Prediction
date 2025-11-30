# Customer_Churn_Prediction

<h1 align="center">
  <br>
  📊 Customer Churn Prediction Thesis Project
  <br>
</h1>

<h4 align="center">
  A machine learning–based analysis for predicting customer churn across multiple industries (telecom, banking, e-commerce), using Python, Scikit-Learn, XGBoost, and interactive dashboard tools.
</h4>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python">
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-yellow?logo=scikitlearn">
  <img src="https://img.shields.io/badge/XGBoost-Model-orange">
  <img src="https://img.shields.io/badge/Google-Colab-green?logo=googlecolab">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit">
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#project-structure">Project Structure</a> •
  <a href="#key-features">Key Features</a> •
  <a href="#datasets">Datasets</a> •
  <a href="#tools--technologies">Tools</a> •
  <a href="#results--insights">Results</a> •
  <a href="#dashboard">Dashboard</a> •
  <a href="#installation--usage">Installation</a>
</p>

---

## 📌 Overview

This repository contains my final-year thesis project focused on **predicting customer churn** using machine learning techniques and comparing patterns across **multiple industries**.

The project includes:

- Full data pipeline: data exploration → cleaning → feature engineering → modeling  
- Multiple ML models: Logistic Regression, Random Forest, XGBoost  
- Model explainability using SHAP  
- Industry comparison (bank, telecom, e-commerce)  
- Interactive dashboard for exploring insights  

This work demonstrates both technical and analytical skills for real-world data science roles.

---

## Project Structure

```plaintext
Thesis_Project/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── final/
│
├── notebooks/
│   ├── 01-data-exploration.ipynb
│   ├── 02-data-cleaning.ipynb
│   ├── 03-eda.ipynb
│   ├── 04-feature-engineering.ipynb
│   ├── 05-modelling.ipynb
│   └── 06-shap-dashboard.ipynb
│
├── dashboard/
│   ├── app.py
│   └── visuals/
│
├── docs/
│   ├── data-dictionary/
│   ├── supervisor-notes/
│   └── report-drafts/
│
├── outputs/
│   ├── charts/
│   ├── model-metrics/
│   └── shap/
│
└── README.md


---

## ⭐ Key Features

- **Multi-industry churn prediction** (banking, telecom, e-commerce)  
- **End-to-end ML pipeline** built with Python  
- **Exploratory Data Analysis (EDA)** with visualizations  
- **Advanced ML models** (Random Forest, XGBoost)  
- **Model explainability** using SHAP  
- **Interactive dashboard** built with Streamlit or Power BI  
- **Business insights & recommendations** included  

---

## 📚 Datasets

All datasets are sourced from publicly available resources such as **Kaggle**.

| Industry | Source | Size | Target |
|---------|--------|------|--------|
| Telecom | Kaggle | ~7k rows | Churn |
| Banking | Kaggle | ~10k rows | Exited / Churn |
| E-commerce | Kaggle or UCI | varies | Cancellation / Churn |

*(Full information in `/docs/data-dictionary/`.)*

---

## 🛠️ Tools & Technologies

- **Python** (Pandas, NumPy)
- **Machine Learning:** Scikit-Learn, XGBoost  
- **Visualization:** Matplotlib, Seaborn  
- **Explainability:** SHAP  
- **Dashboard:** Streamlit / Power BI / Tableau  
- **Environment:** Google Colab  
- **Version control:** GitHub  

---

## 📈 Results & Insights

This section will be updated as the project progresses.

Planned results include:

- Best-performing churn model per industry  
- Feature importance analysis  
- SHAP global & local explanations  
- Industry comparison metrics  
- Business recommendations  

---

## 🖥️ Dashboard

The interactive dashboard (Streamlit or Power BI) will include:

- Churn overview  
- Feature importance panels  
- Interactive filters  
- Multi-industry comparison  
- Prediction explorer  

---

## 🚀 Installation & Usage

To clone and run the project:

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/customer-churn-thesis-project

# Navigate to repository
cd customer-churn-thesis-project

# (Optional) Install dependencies if running locally
pip install -r requirements.txt

