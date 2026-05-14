from concurrent import futures
import sys
from pathlib import Path

import grpc

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from shared.generated import fraud_pb2
from shared.generated import fraud_pb2_grpc


class FraudService(
    fraud_pb2_grpc.FraudServiceServicer
):

    def CheckFraud(self, request, context):

        risk_score = 0.15

        if request.amount > 5000:
            risk_score = 0.92

        return fraud_pb2.FraudResponse(
            risk_score=risk_score,
            high_risk=risk_score > 0.8,
            reason="High amount detected"
        )


def serve():

    server = grpc.server(
        futures.ThreadPoolExecutor(
            max_workers=10
        )
    )

    fraud_pb2_grpc.add_FraudServiceServicer_to_server(
        FraudService(),
        server
    )

    server.add_insecure_port(
        "[::]:50051"
    )

    server.start()

    print("Fraud gRPC service running on 50051")

    server.wait_for_termination()


if __name__ == "__main__":
    serve()
