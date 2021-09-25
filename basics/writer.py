import grpc
import item_pb2_grpc
import item_pb2

print("Sending requests to the gRPC server....")

channel = grpc.insecure_channel('localhost:5001')
stub = item_pb2_grpc.ItemServiceStub(channel)

item = item_pb2.ItemMessage(
    name="iPhone 13",
    brand_name='Apple',
    id=930,
    weight=4.5
)

response = stub.Create(item)
print(response)
