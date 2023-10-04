"""The client py file for the application"""
import grpc
import calculator_pb2 as pb2
import calculator_pb2_grpc as pb2_grpc
from concurrent.futures import ThreadPoolExecutor


class CalculatorServicer(pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.a + request.b 
        return pb2.AddResponse(result = result)
    
def server():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    server()