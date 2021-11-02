import item_pb2
import item_pb2_grpc
import grpc

import time
from concurrent import futures


class ItemService(item_pb2_grpc.ItemServiceServicer):
    def Create(self, request, context):

        request_value = {
            'name': request.name,
            'brand_name': request.brand_name,
            'id': int(request.id),
            'weight': request.weight
        }
        print(request_value)

        return item_pb2.ItemMessage(**request_value)


server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
item_pb2_grpc.add_ItemServiceServicer_to_server(ItemService(), server)


print('Server (basics) starting on port 5001')
server.add_insecure_port('[::]:5001')
server.start()
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
