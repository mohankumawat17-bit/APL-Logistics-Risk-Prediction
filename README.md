# 🚚 APL Logistics — Late Delivery Risk Prediction

## Project Overview
Machine Learning based system to predict late delivery risk in global supply chain operations **before shipment begins**.

Built as part of **Unified Mentor Data Analyst Internship** | May 2026

**Live Dashboard:** [Click Here](https://apl-logistics-risk-prediction-2iswovrzbdj5mtpnffjjcn.streamlit.app/)

---

## Problem Statement
- 54.8% of APL Logistics orders are delivered late
- Reactive approach = high operational cost
- No system to flag high-risk orders proactively

---

## Solution
Predictive ML system that assigns each order a **Late Delivery Risk Score (0–1)** and classifies it into:
- 🟢 Low Risk — Probability 0.0 to 0.4
- 🟡 Medium Risk — Probability 0.4 to 0.6
- 🔴 High Risk — Probability 0.6 to 1.0

---

## Project Structure

```
APL_Logistics_Project/
├── 01_data_preprocessing.ipynb   # Data cleaning, encoding, feature engineering
├── 02_model_training.ipynb       # Logistic Regression, Random Forest, XGBoost
├── 03_risk_scoring.ipynb         # Risk scoring, feature importance
├── app.py                        # Streamlit dashboard
├── requirements.txt              # Python dependencies
├── model_comparison.png          # Model performance chart
├── risk_distribution.png         # Risk category distribution
├── feature_importance.png        # Top features driving delay
├── risk_scores.csv               # Order-level risk scores
└── high_risk_orders.csv          # High risk orders list
```

---

## Dataset

| Attribute | Value |
|---|---|
| Total Records | 1,80,519 |
| Total Features | 40 (original) → 113 (after encoding) |
| Target Variable | Late_delivery_risk (0 = On Time, 1 = Late) |
| Late Deliveries | 98,977 (54.8%) |
| Markets Covered | LATAM, Europe, Pacific Asia, USCA, Africa |

---

## Models Trained

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---|---|---|---|---|
| Logistic Regression | 69.34% | 83.54% | 54.62% | 66.06% | 73.82% |
| Random Forest | 68.70% | 75.91% | 62.53% | 68.57% | 74.99% |
| **XGBoost ✅** | **69.83%** | **82.83%** | **56.46%** | **67.15%** | **76.46%** |

> XGBoost selected as final model based on highest ROC-AUC score.

---

## Risk Classification Results

| Category | Orders | Percentage | Action |
|---|---|---|---|
| 🟢 Low Risk | 14,970 | 41.5% | Standard processing |
| 🟡 Medium Risk | 8,550 | 23.7% | Monitor closely |
| 🔴 High Risk | 12,584 | 34.9% | Immediate intervention |

---

## Key Findings
- Scheduled shipment duration is **#1 risk driver** (60.96% feature importance)
- Transfer payment orders carry higher delay risk (6.61% importance)
- North Africa and West Asia show elevated regional delay patterns
- Standard Class shipping (59.7% of orders) correlates strongly with late delivery
- 18.7% of orders are loss-making — indicating fulfillment inefficiencies
- **12,584 High Risk orders** identified requiring immediate operational attention

---

## Important Note — Data Leakage
Initial models showed 97%+ accuracy due to data leakage features (`Delivery Status`, `Days for shipping real`). These features are unavailable before shipment and were removed. Final model accuracy of ~70% represents genuine predictive capability on future unseen orders.

---

## Tech Stack
![Python](https://img.shields.io/badge/Python-3.14-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0-green)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-latest-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-3.2-red)
![Streamlit](https://img.shields.io/badge/Streamlit-latest-ff4b4b)

- **Data Processing:** Python, Pandas, NumPy
- **Machine Learning:** Scikit-learn, XGBoost
- **Visualization:** Matplotlib, Seaborn
- **Dashboard:** Streamlit
- **IDE:** VS Code

---

## Project Deliverables
- ✅ 3 Jupyter Notebooks (Preprocessing, Training, Risk Scoring)
- ✅ Streamlit Web Dashboard
- ✅ Research Paper (PDF)
- ✅ Executive Summary (PDF)

---

## Author

**Mohan Lal Kumawat**
MCA + BCA | 8+ Years Operations Experience
Unified Mentor Data Analyst Internship
📧 mohankumawat17@gmail.com
📱 9782388664
