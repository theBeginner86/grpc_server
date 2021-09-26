import grpc
import order_pb2
import order_pb2_grpc

print("Sending request to Server......")

channel = grpc.insecure_channel('localhost:5001')
stub = order_pb2_grpc.OrderServiceStub(channel)

order = order_pb2.OrderMessage(
    id='20mic0102',
    created_by='Pranav Singh',
    status='COMPLETED',
    created_at='14/11/2002',
    equipment=[
        'MOUSE', 'KEYBOARD'
    ]
)

response_to_create_order = stub.Create(order)
print(response_to_create_order)
