"""The client py script for the application"""
import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)
    
    request = calculator_pb2.AddRequest(a=10, b=20)
    response = stub.Add(request)
    
    print("Result: ", response.result)
    

if __name__ == "__main__":
    run()