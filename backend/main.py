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


# ── Real translations ──────────────────────────────────────────

MESSAGES = {
    "English": {
        "Low": (
            "Dear Customer, your loan account is in good standing. "
            "Thank you for your timely payments. Keep up the excellent financial discipline!"
        ),
        "Medium": (
            "Dear Customer, we noticed some irregularities in your repayment pattern. "
            "Please ensure your EMI of ₹{emi} is paid on time to avoid penalties. "
            "Contact us at 1800-XXX-XXXX if you need assistance."
        ),
        "High": (
            "Dear Customer, your loan account requires immediate attention. "
            "Your current repayment difficulty may lead to serious penalties. "
            "We strongly recommend contacting our recovery team at 1800-XXX-XXXX "
            "to discuss EMI restructuring options and avoid legal action."
        ),
    },
    "Tamil": {
        "Low": (
            "அன்புள்ள வாடிக்கையாளரே, உங்கள் கடன் கணக்கு நல்ல நிலையில் உள்ளது. "
            "சரியான நேரத்தில் தவணை செலுத்தியதற்கு நன்றி. "
            "இந்த நிதி ஒழுக்கத்தை தொடர்ந்து பின்பற்றுங்கள்!"
        ),
        "Medium": (
            "அன்புள்ள வாடிக்கையாளரே, உங்கள் தவணை செலுத்துதலில் சில தாமதங்கள் கவனிக்கப்பட்டன. "
            "அபராதங்களை தவிர்க்க ₹{emi} தவணையை சரியான நேரத்தில் செலுத்துங்கள். "
            "உதவிக்கு 1800-XXX-XXXX என்ற எண்ணில் தொடர்பு கொள்ளுங்கள்."
        ),
        "High": (
            "அன்புள்ள வாடிக்கையாளரே, உங்கள் கடன் கணக்கு உடனடி கவனிப்பு தேவைப்படுகிறது. "
            "தற்போதைய நிலை தொடர்ந்தால் சட்ட நடவடிக்கை எடுக்கப்படலாம். "
            "தவணை மறுசீரமைப்பு விருப்பங்களை பற்றி விவாதிக்க "
            "1800-XXX-XXXX என்ற எண்ணில் உடனடியாக தொடர்பு கொள்ளுங்கள்."
        ),
    },
    "Hindi": {
        "Low": (
            "प्रिय ग्राहक, आपका ऋण खाता अच्छी स्थिति में है। "
            "समय पर भुगतान के लिए धन्यवाद। "
            "इस वित्तीय अनुशासन को बनाए रखें!"
        ),
        "Medium": (
            "प्रिय ग्राहक, आपके पुनर्भुगतान में कुछ अनियमितताएं देखी गई हैं। "
            "जुर्माने से बचने के लिए कृपया अपनी ₹{emi} की EMI समय पर चुकाएं। "
            "सहायता के लिए 1800-XXX-XXXX पर संपर्क करें।"
        ),
        "High": (
            "प्रिय ग्राहक, आपके ऋण खाते पर तत्काल ध्यान देने की आवश्यकता है। "
            "वर्तमान स्थिति गंभीर दंड और कानूनी कार्रवाई का कारण बन सकती है। "
            "EMI पुनर्गठन के लिए हमारी रिकवरी टीम से "
            "1800-XXX-XXXX पर तुरंत संपर्क करें।"
        ),
    },
    "Malayalam": {
        "Low": (
            "പ്രിയ ഉപഭോക്താവേ, നിങ്ങളുടെ ലോൺ അക്കൗണ്ട് നല്ല നിലയിലാണ്. "
            "കൃത്യസമയത്ത് അടച്ചതിന് നന്ദി. "
            "ഈ സാമ്പത്തിക അച്ചടക്കം തുടരുക!"
        ),
        "Medium": (
            "പ്രിയ ഉപഭോക്താവേ, നിങ്ങളുടെ തിരിച്ചടവിൽ ചില ക്രമക്കേടുകൾ ശ്രദ്ധിക്കപ്പെട്ടു. "
            "പിഴ ഒഴിവാക്കാൻ ₹{emi} EMI കൃത്യസമയത്ത് അടക്കുക. "
            "സഹായത്തിന് 1800-XXX-XXXX എന്ന നമ്പറിൽ ബന്ധപ്പെടുക."
        ),
        "High": (
            "പ്രിയ ഉപഭോക്താവേ, നിങ്ങളുടെ ലോൺ അക്കൗണ്ടിന് അടിയന്തര ശ്രദ്ധ ആവശ്യമാണ്. "
            "നിലവിലെ സ്ഥിതി തുടർന്നാൽ നിയമ നടപടി ഉണ്ടായേക്കാം. "
            "EMI പുനഃക്രമീകരണ ഓപ്ഷനുകൾ ചർച്ച ചെയ്യാൻ "
            "1800-XXX-XXXX-ൽ ഉടനടി ബന്ധപ്പെടുക."
        ),
    },
}

REASONS = {
    "English": {
        "negative_savings": "Expenses exceed income — negative savings detected.",
        "high_emi_ratio":   "EMI exceeds 40% of income — high debt-to-income ratio.",
        "low_balance":      "Account balance is insufficient to cover the next EMI.",
        "missed_payments":  "{n} missed payment(s) on record.",
    },
    "Tamil": {
        "negative_savings": "செலவுகள் வருமானத்தை மீறுகின்றன — எதிர்மறை சேமிப்பு கண்டறியப்பட்டது.",
        "high_emi_ratio":   "தவணை வருமானத்தின் 40% ஐ தாண்டுகிறது — அதிக கடன்-வருமான விகிதம்.",
        "low_balance":      "கணக்கு இருப்பு அடுத்த தவணையை ஈடுகட்ட போதுமானதாக இல்லை.",
        "missed_payments":  "பதிவில் {n} தவறிய தவணை(கள்) உள்ளன.",
    },
    "Hindi": {
        "negative_savings": "खर्च आय से अधिक है — नकारात्मक बचत पाई गई।",
        "high_emi_ratio":   "EMI आय के 40% से अधिक है — उच्च ऋण-आय अनुपात।",
        "low_balance":      "खाता शेष अगली EMI को कवर करने के लिए अपर्याप्त है।",
        "missed_payments":  "रिकॉर्ड पर {n} चूका हुआ भुगतान है।",
    },
    "Malayalam": {
        "negative_savings": "ചെലവുകൾ വരുമാനത്തെ കവിയുന്നു — നെഗറ്റീവ് സേവിംഗ്സ് കണ്ടെത്തി.",
        "high_emi_ratio":   "EMI വരുമാനത്തിന്റെ 40% കവിയുന്നു — ഉയർന്ന കടം-വരുമാന അനുപാതം.",
        "low_balance":      "അടുത്ത EMI ഉൾക്കൊള്ളാൻ അക്കൗണ്ട് ബാലൻസ് അപര്യാപ്തമാണ്.",
        "missed_payments":  "റെക്കോർഡിൽ {n} മിസ്സ്ഡ് പേയ്‌മെന്റ്(കൾ) ഉണ്ട്.",
    },
}

ACTIONS = {
    "English":   {"High": "Offer EMI restructuring",   "Medium": "Send payment reminder",   "Low": "No action needed"},
    "Tamil":     {"High": "EMI மறுசீரமைப்பு வழங்கவும்", "Medium": "தவணை நினைவூட்டல் அனுப்பவும்", "Low": "நடவடிக்கை தேவையில்லை"},
    "Hindi":     {"High": "EMI पुनर्गठन की पेशकश करें", "Medium": "भुगतान अनुस्मारक भेजें",        "Low": "कोई कार्रवाई आवश्यक नहीं"},
    "Malayalam": {"High": "EMI പുനഃക്രമീകരണം വാഗ്ദാനം ചെയ്യുക", "Medium": "പേയ്‌മെന്റ് റിമൈൻഡർ അയക്കുക", "Low": "നടപടി ആവശ്യമില്ല"},
}


@app.post("/analyze")
def analyze_loan(data: LoanInput):
    lang = data.language
    savings = data.income - data.expenses
    risk = 0
    reason_keys = []

    if savings < 0:
        risk += 30
        reason_keys.append("negative_savings")

    if data.emi > data.income * 0.4:
        risk += 25
        reason_keys.append("high_emi_ratio")

    if data.balance < data.emi:
        risk += 20
        reason_keys.append("low_balance")

    if data.missed_payments > 0:
        risk += 25
        reason_keys.append("missed_payments")

    risk = min(risk, 100)

    if risk <= 30:
        risk_level = "Low"
    elif risk <= 60:
        risk_level = "Medium"
    else:
        risk_level = "High"

    # Build translated reasons
    r_map = REASONS.get(lang, REASONS["English"])
    reasons = []
    for key in reason_keys:
        text = r_map[key]
        if key == "missed_payments":
            text = text.replace("{n}", str(data.missed_payments))
        reasons.append(text)

    # Translated action
    action = ACTIONS.get(lang, ACTIONS["English"])[risk_level]

    # Translated message with EMI filled in
    message = MESSAGES.get(lang, MESSAGES["English"])[risk_level]
    message = message.replace("{emi}", f"{int(data.emi):,}")

    # Simulation
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
