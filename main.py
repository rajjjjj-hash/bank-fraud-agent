from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import random

app = FastAPI(title="Fraud Agent API")

# ==========================
# OTP Verification
# ==========================

@app.post("/verify-otp")
async def verify_otp(request: Request):

    # Accept data from ANY format Bolna sends
    body = {}
    try:
        body = await request.json()
    except Exception:
        pass

    # Also check query params and form data
    params = dict(request.query_params)
    body = {**params, **body}  # body overrides params

    otp = str(body.get("otp", "")).strip()
    customer_name = body.get("customer_name", "")
    customer_id = body.get("customer_id", "")

    print("========== VERIFY OTP CALLED ==========")
    print(f"Raw body     : {body}")
    print(f"Customer Name: {customer_name}")
    print(f"Customer ID  : {customer_id}")
    print(f"OTP          : {otp}")
    print("========================================")

    if otp == "123456":
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
        "message": "Invalid OTP"
    }

# ==========================
# Freeze Card
# ==========================

@app.post("/freeze-card")
async def freeze_card(request: Request):

    body = {}
    try:
        body = await request.json()
    except Exception:
        pass

    params = dict(request.query_params)
    body = {**params, **body}

    reference_id = f"CARD-{random.randint(10000, 99999)}"

    print("========== FREEZE CARD CALLED ==========")
    print(f"Raw body : {body}")
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

@app.post("/create-ticket")
async def create_ticket(request: Request):

    body = {}
    try:
        body = await request.json()
    except Exception:
        pass

    params = dict(request.query_params)
    body = {**params, **body}

    ticket_id = f"FRD-{random.randint(100000, 999999)}"

    print("========== CREATE TICKET CALLED ==========")
    print(f"Raw body  : {body}")
    print(f"Ticket ID : {ticket_id}")
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
async def webhook(request: Request):

    body = {}
    try:
        body = await request.json()
    except Exception:
        pass

    print("========== WEBHOOK RECEIVED ==========")
    print(body)
    print("=======================================")

    return {"status": "received"}

# ==========================
# Home
# ==========================

@app.get("/")
def home():
    return {"message": "Fraud Agent Backend Running"}