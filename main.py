from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import random

app = FastAPI(title="Fraud Agent API")


class OTPRequest(BaseModel):
    customer_name: str
    customer_id: str
    otp: str


@app.post("/verify-otp")
def verify_otp(data: OTPRequest):

    print("VERIFY OTP CALLED")
    print(f"Customer Name: {data.customer_name}")
    print(f"Customer ID: {data.customer_id}")
    print(f"OTP: {data.otp}")

    if str(data.otp).strip() == "123456":
        return {
            "success": True,
            "verified": True,
            "status": "success",
            "result": "success",
            "message": "OTP verified"
        }

    return {
        "success": False,
        "verified": False,
        "status": "failed",
        "result": "failed",
        "message": "Invalid OTP"
    }


class FreezeCardRequest(BaseModel):
    customer_name: str
    card_last_four: str
    card_type: str
    reason: str


@app.post("/freeze-card")
def freeze_card(data: FreezeCardRequest):

    reference_id = f"CARD-{random.randint(10000,99999)}"

    return {
        "success": True,
        "status": "success",
        "reference_id": reference_id,
        "message": "Card frozen successfully"
    }


class FraudTicketRequest(BaseModel):
    customer_name: str
    fraud_type: str
    risk_level: str
    summary: str


@app.post("/create-ticket")
def create_ticket(data: FraudTicketRequest):

    ticket_id = f"FRD-{random.randint(100000,999999)}"

    return {
        "success": True,
        "status": "success",
        "ticket_id": ticket_id,
        "created_at": str(datetime.now())
    }


@app.post("/webhook")
async def webhook(data: dict):

    print("WEBHOOK RECEIVED")
    print(data)

    return {
        "status": "received"
    }


@app.get("/")
def home():
    return {
        "message": "Fraud Agent Backend Running"
    }