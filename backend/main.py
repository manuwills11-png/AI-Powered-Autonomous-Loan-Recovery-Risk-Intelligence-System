from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Literal

app = FastAPI(title="AI Loan Risk & Recovery System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class LoanInput(BaseModel):
    income: float
    expenses: float
    emi: float
    balance: float
    missed_payments: int
    language: Literal["English", "Tamil", "Hindi", "Malayalam"] = "English"


@app.post("/analyze")
def analyze_loan(data: LoanInput):
    # --- Risk Calculation ---
    savings = data.income - data.expenses
    risk = 0
    reasons = []

    if savings < 0:
        risk += 30
        reasons.append("Expenses exceed income — negative savings detected.")

    if data.emi > data.income * 0.4:
        risk += 25
        reasons.append("EMI exceeds 40% of income — high debt-to-income ratio.")

    if data.balance < data.emi:
        risk += 20
        reasons.append("Account balance is insufficient to cover the next EMI.")

    if data.missed_payments > 0:
        risk += 25
        reasons.append(f"{data.missed_payments} missed payment(s) on record.")

    risk = min(risk, 100)

    # --- Risk Level ---
    if risk <= 30:
        risk_level = "Low"
    elif risk <= 60:
        risk_level = "Medium"
    else:
        risk_level = "High"

    # --- Action Engine ---
    action_map = {
        "High": "Offer EMI restructuring",
        "Medium": "Send payment reminder",
        "Low": "No action needed",
    }
    action = action_map[risk_level]

    # --- Message Generation ---
    base_message = (
        "Hi, we noticed some difficulty in repayments. "
        "You can avoid penalties by paying your EMI on time. "
        "Let us know if you need help."
    )
    prefix_map = {
        "Tamil": "[Tamil] ",
        "Hindi": "[Hindi] ",
        "Malayalam": "[Malayalam] ",
        "English": "",
    }
    message = prefix_map[data.language] + base_message

    # --- Simulation ---
    reduction = risk * 0.30 if risk_level == "High" else risk * 0.10
    new_risk = max(0, risk - reduction)

    return {
        "risk_score": risk,
        "risk_level": risk_level,
        "reasons": reasons,
        "action": action,
        "message": message,
        "simulation": {
            "before": risk,
            "after": round(new_risk, 2),
        },
    }
