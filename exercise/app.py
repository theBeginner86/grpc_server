import grpc
import order_pb2
import order_pb2_grpc

import time
from concurrent import futures


class OrderServicer(order_pb2_grpc.OrderServiceServicer):
    def Create(self, request, context):
        request_value = {
            'id': request.id,
            'created_by': request.created_by,
            'status': request.status,
            'created_at': request.created_at,
            'equipment': request.equipment
        }
        print(request_value)
        return order_pb2.OrderMessage(**request_value)

    def Get(self, request, context):
        first_order = order_pb2.OrderMessage(
            id='101',
            created_by='jake',
            status=order_pb2.OrderMessage.Status.QUEUED,
            created_at='2021-09-12',
            equipment=[
                order_pb2.OrderMessage.Equipment.KEYBOARD
            ]
        )

        second_order = order_pb2.OrderMessage(
            id='102',
            created_by='tyler',
            status=order_pb2.OrderMessage.Status.PROCESSING,
            created_at='2021-09-12',
            equipment=[
                order_pb2.OrderMessage.Equipment.KEYBOARD,
                order_pb2.OrderMessage.Equipment.MONITOR
            ]
        )

        response = order_pb2.OrderMessageList()
        response.orders.extend([first_order, second_order])
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
order_pb2_grpc.add_OrderServiceServicer_to_server(OrderServicer(), server)

print('Server starting at 5001...')
server.add_insecure_port('[::]:5001')
server.start()

try :
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
