from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import random

app = FastAPI(title="Fraud Agent API")

# --------------------
# OTP Verification
# --------------------

class OTPRequest(BaseModel):
    customer_name: str
    customer_id: str
    otp: str

@app.post("/verify-otp")
def verify_otp(data: OTPRequest):

    if data.otp == "123456":
        return {
            "status": "success",
            "message": "OTP verified",
            "customer": data.customer_name
        }

    return {
        "status": "failed",
        "message": "Invalid OTP"
    }


# --------------------
# Freeze Card
# --------------------

class FreezeCardRequest(BaseModel):
    customer_name: str
    card_last_four: str
    card_type: str
    reason: str

@app.post("/freeze-card")
def freeze_card(data: FreezeCardRequest):

    reference_id = f"CARD-{random.randint(10000,99999)}"

    return {
        "status": "success",
        "reference_id": reference_id,
        "message": "Card frozen successfully"
    }


# --------------------
# Fraud Ticket
# --------------------

class FraudTicketRequest(BaseModel):
    customer_name: str
    fraud_type: str
    risk_level: str
    summary: str

@app.post("/create-ticket")
def create_ticket(data: FraudTicketRequest):

    ticket_id = f"FRD-{random.randint(100000,999999)}"

    return {
        "status": "success",
        "ticket_id": ticket_id,
        "created_at": str(datetime.now())
    }


# --------------------
# Webhook Endpoint
# --------------------

@app.post("/webhook")
async def webhook(data: dict):
    print("Webhook received:", data)

    return {
        "status": "received"
    }


# --------------------
# Home
# --------------------

@app.get("/")
def home():
    return {
        "message": "Fraud Agent Backend Running"
    }