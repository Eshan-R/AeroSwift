import time

def process_payment(amount, currency, form_data):
    """
    Simulates a payment process.
    """
    card_number = form_data.get("card_number")
    expiry = form_data.get("expiry")
    cvv = form_data.get("cvv")

    # Simple simulation logic
    if not card_number or len(card_number.replace(" ", "")) < 16:
        return {"success": False, "message": "Invalid Card Number"}
    
    if not cvv or len(cvv) < 3:
        return {"success": False, "message": "Invalid CVV"}

    # In a real app, you'd call a gateway here
    return {"success": True, "transaction_id": "TXN_SIM_12345"}