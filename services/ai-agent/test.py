from fraud_client import check_fraud

expense = {
    "employee_name": "Yuan Li",
    "amount": 8000,
    "category": "Travel"
}

result = check_fraud(expense)

print(result)