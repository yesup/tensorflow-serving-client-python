
def callback(future):

    exception = future.exception()

    if exception:
        print "Error: ", exception
        return

    prediction = future.result().outputs['classes']

    print prediction

def doTest(host, port):
    from tensorflow_serving.apis.predict_pb2 import PredictRequest
    from tensorflow_serving.apis.prediction_service_pb2_grpc import PredictionServiceStub
    from grpc import insecure_channel
    from tensorflow.contrib.util import make_tensor_proto
    from tensorflow import float32

    target = "%s:%s"%(host, port)

    print "Sending prediction request to", target, "\n"

    channel = insecure_channel(target)
    stub = PredictionServiceStub(channel)

    request = PredictRequest()
    request.model_spec.name = "campaign"
    request.model_spec.signature_name = ""

    request.inputs["hour"].CopyFrom(make_tensor_proto(3, shape=[1], dtype=float32))
    request.inputs["week"].CopyFrom(make_tensor_proto(5, shape=[1], dtype=float32))

    future = stub.Predict.future(request, 5.0)

    future.add_done_callback(callback)

if __name__ == "__main__":
    from sys import argv, exit

    if argv.__len__() != 3:
        print "Usage: python test.py [host] [port]\n"
        exit(0)

    doTest(argv[1], argv[2])