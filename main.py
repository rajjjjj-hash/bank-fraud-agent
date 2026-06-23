from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import random

app = FastAPI(title="Fraud Agent API")

# ==========================
# OTP Verification
# ==========================

class OTPRequest(BaseModel):
    customer_name: Optional[str] = None
    customer_id: Optional[str] = None
    otp: str

@app.post("/verify-otp")
def verify_otp(data: OTPRequest):

    print("========== VERIFY OTP CALLED ==========")
    print(f"Customer Name : {data.customer_name}")
    print(f"Customer ID   : {data.customer_id}")
    print(f"OTP           : {data.otp}")
    print("========================================")

    if str(data.otp).strip() == "123456":
        return {
            "success": True,
            "verified": True,
            "status": "success",
            "result": "success",
            "message": "OTP verified successfully"
        }

    return {
        "success": False,
        "verified": False,
        "status": "failed",
        "result": "failed",
        "message": "Invalid OTP. Please try again."
    }

# ==========================
# Freeze Card
# ==========================

class FreezeCardRequest(BaseModel):
    customer_name: Optional[str] = None
    card_last_four: Optional[str] = None
    card_type: Optional[str] = None
    reason: Optional[str] = None

@app.post("/freeze-card")
def freeze_card(data: FreezeCardRequest):

    reference_id = f"CARD-{random.randint(10000, 99999)}"

    print("========== FREEZE CARD CALLED ==========")
    print(f"Customer : {data.customer_name}")
    print(f"Card     : {data.card_type} ending {data.card_last_four}")
    print(f"Reason   : {data.reason}")
    print(f"Ref ID   : {reference_id}")
    print("=========================================")

    return {
        "success": True,
        "status": "success",
        "reference_id": reference_id,
        "message": "Card frozen successfully"
    }

# ==========================
# Fraud Ticket
# ==========================

class FraudTicketRequest(BaseModel):
    customer_name: Optional[str] = None
    fraud_type: Optional[str] = None
    risk_level: Optional[str] = None
    summary: Optional[str] = None

@app.post("/create-ticket")
def create_ticket(data: FraudTicketRequest):

    ticket_id = f"FRD-{random.randint(100000, 999999)}"

    print("========== CREATE TICKET CALLED ==========")
    print(f"Customer   : {data.customer_name}")
    print(f"Fraud Type : {data.fraud_type}")
    print(f"Risk Level : {data.risk_level}")
    print(f"Ticket ID  : {ticket_id}")
    print("==========================================")

    return {
        "success": True,
        "status": "success",
        "ticket_id": ticket_id,
        "created_at": str(datetime.now())
    }

# ==========================
# Webhook
# ==========================

@app.post("/webhook")
async def webhook(data: dict):

    print("========== WEBHOOK RECEIVED ==========")
    print(data)
    print("=======================================")

    return {"status": "received"}

# ==========================
# Home
# ==========================

@app.get("/")
def home():
    return {"message": "Fraud Agent Backend Running"}