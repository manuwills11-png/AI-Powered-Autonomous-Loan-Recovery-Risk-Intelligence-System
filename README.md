# 🚀 AI-Powered Autonomous Loan Recovery & Risk Intelligence System

## 🧠 Overview

This project is an AI-driven system designed to help banks and NBFCs **predict, prevent, and manage loan defaults (NPAs)** through intelligent analysis and automated interventions.

Unlike traditional systems that react after default, our solution enables **early detection, personalized communication, and proactive recovery strategies**.

---

## 🚨 Problem Statement

Financial institutions face:

* High loan default rates (NPAs)
* Delayed identification of risky borrowers
* Inefficient, generic recovery methods
* Lack of personalized communication

---

## 💡 Solution

We built a system that:

* Predicts default risk early
* Explains the reasons behind risk
* Suggests optimal recovery actions
* Generates personalized multilingual messages
* Simulates impact of interventions

---

## ⚙️ Key Features

### 🧠 Risk Prediction Engine

* Analyzes:

  * Income vs expenses
  * EMI burden
  * Account balance
  * Missed payments
* Outputs:

  * Risk score (0–100)
  * Risk level (Low / Medium / High)

---

### 🔍 Explainable AI

* Provides clear reasons for risk:

  * Income drop
  * High expenses
  * Low balance
* Builds trust and transparency

---

### ⚡ Smart Intervention Engine

Recommends actions based on risk:

* Low → No action
* Medium → Payment reminder
* High → EMI restructuring

---

### 💬 Multilingual Communication

* Generates personalized messages in:

  * English
  * Tamil
  * Hindi
  * Malayalam

---

### 🧠 Intent Detection

* Classifies users:

  * Genuine (financial difficulty)
  * Risky
  * Intentional defaulter

---

### 🔮 Intervention Simulator

* Shows impact of actions:

  * Example: Risk reduced from 72% → 40%

---

### 🔄 Feedback Loop (Conceptual)

* Tracks effectiveness of interventions
* Improves future recommendations

---

## 🧩 Tech Stack

### Frontend:

* React (Vite)
* Tailwind CSS

### Backend:

* FastAPI (Python)

### Communication:

* REST API (JSON)

---

## 📂 Project Structure

```
project/
├── frontend/   # React app
├── backend/    # FastAPI server
```

---

## 🚀 How to Run

### 1. Clone Repository

```
git clone <repo-url>
cd project
```

---

### 2. Run Backend

```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs on:

```
http://localhost:8000
```

---

### 3. Run Frontend

```
cd frontend
npm install
npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

## 🔗 API Endpoint

### POST `/analyze`

#### Request:

```
{
  "income": 50000,
  "expenses": 30000,
  "emi": 15000,
  "balance": 10000,
  "missed_payments": 1,
  "language": "Tamil"
}
```

#### Response:

```
{
  "risk_score": 72,
  "risk_level": "High",
  "reasons": ["High EMI burden", "Low balance"],
  "action": "Offer EMI restructuring",
  "message": "🇮🇳 Tamil: Hi, we noticed some difficulty...",
  "simulation": {
    "before": 72,
    "after": 40
  }
}
```

---

## 🎯 Impact

* Reduces loan defaults (NPAs)
* Improves recovery efficiency
* Enables early intervention
* Enhances customer engagement
* Supports regional language inclusivity

---

## 🏆 Hackathon Alignment

This project directly addresses:

* **Loan Collection & Recovery Optimization**
* **Regional Language Communication**

---

## 🧨 One-Line Pitch

> “We don’t just predict loan defaults — we prevent them through intelligent, personalized, and explainable AI-driven interventions.”

---

## 👥 Team

* Frontend Developer
* Backend Developer

---

## 📌 Future Scope

* Real bank data integration
* Advanced ML models
* Voice-based communication
* WhatsApp/IVR automation
* Real-time monitoring dashboard

---

## ⚡ Status

✅ MVP Completed
🚀 Demo Ready
🔥 Hackathon Submission Ready

---
