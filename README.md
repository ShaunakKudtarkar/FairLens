# FairLens

FairLens is an interactive AI fairness platform designed to detect, visualize, and mitigate bias in machine learning models using an intuitive human-first interface.

---

## 🚀 Features

* 📊 Data Auditing (detect imbalance & skew)
* ⚖️ Bias Detection (Statistical Parity, Disparate Impact)
* 🛠 Mitigation Techniques (Reweighing, SMOTE, Threshold tuning)
* 🤖 Model Training Simulation
* 🔍 Explainability (SHAP & LIME)
* 📈 Fairness vs Accuracy Tradeoff Visualization
* 📄 Report Generation

---

## 🏗 Architecture

Frontend (HTML/CSS/JS) → Flask API → ML + Fairness Engine

---

## 🖥️ Tech Stack

### Frontend

* HTML, CSS, JavaScript
* Chart.js

### Backend

* Python (Flask)
* Pandas, NumPy
* Scikit-learn
* SHAP, LIME

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fairlens-ai-bias-detection.git
cd fairlens-ai-bias-detection
```

### 2. Backend setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### 3. Frontend setup

Open `frontend/index.html` in your browser

---

## 📡 API Endpoints

| Endpoint | Method | Description            |
| -------- | ------ | ---------------------- |
| /upload  | POST   | Upload dataset         |
| /bias    | POST   | Compute bias metrics   |
| /train   | POST   | Train ML model         |
| /explain | POST   | SHAP/LIME explanations |

---

## 📊 Sample Dataset

Located in `backend/data/sample.csv`

---

## 📌 Future Improvements

* Real-time deployment monitoring
* Dashboard authentication
* Cloud deployment (AWS/GCP)
* Integration with AIF360

---

## 👨‍💻 Author

Shaunak Kudtarkar

---

## 📜 License

MIT License
