from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc
from grpc import insecure_channel
from tensorflow.contrib.util import make_tensor_proto

