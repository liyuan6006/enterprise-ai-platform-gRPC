import grpc
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from shared.generated import fraud_pb2
from shared.generated import fraud_pb2_grpc


channel = grpc.insecure_channel(
    "localhost:50051"
)

stub = fraud_pb2_grpc.FraudServiceStub(
    channel
)


def check_fraud(expense):

    request = fraud_pb2.FraudRequest(
        employee_name=expense["employee_name"],
        amount=expense["amount"],
        category=expense["category"]
    )

    response = stub.CheckFraud(request)

    return {
        "risk_score": response.risk_score,
        "high_risk": response.high_risk,
        "reason": response.reason
    }
