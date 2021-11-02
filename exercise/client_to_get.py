import grpc
import order_pb2
import order_pb2_grpc

channel = grpc.insecure_channel('localhost:5002')
stub = order_pb2_grpc.OrderServiceStub(channel)

response = stub.Get(order_pb2.Empty())
print(response)
