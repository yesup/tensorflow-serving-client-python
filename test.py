
def doTest(host, port):
    from tensorflow_serving.apis.predict_pb2 import PredictRequest
    from tensorflow_serving.apis.prediction_service_pb2_grpc import PredictionServiceStub
    from grpc import insecure_channel, StatusCode
    from tensorflow.contrib.util import make_tensor_proto, make_ndarray
    from tensorflow import float32

    target = "%s:%s"%(host, port)

    print "Sending prediction request to", target, "\n"

    channel = insecure_channel(target)
    stub = PredictionServiceStub(channel)

    request = PredictRequest()
    request.model_spec.name = "campaign"
    request.model_spec.signature_name = ""

    request.inputs["hour"].CopyFrom(make_tensor_proto(6, shape=[1], dtype=float32))
    request.inputs["week"].CopyFrom(make_tensor_proto(5, shape=[1], dtype=float32))
    request.inputs["sid"].CopyFrom(make_tensor_proto("47320", shape=[1]))
    request.inputs["sspid"].CopyFrom(make_tensor_proto("3", shape=[1]))
    request.inputs["country"].CopyFrom(make_tensor_proto("DK", shape=[1]))
    request.inputs["os"].CopyFrom(make_tensor_proto("6", shape=[1]))
    request.inputs["domain"].CopyFrom(make_tensor_proto("video9.in", shape=[1]))
    request.inputs["isp"].CopyFrom(make_tensor_proto("Tele Danmark", shape=[1]))
    request.inputs["browser"].CopyFrom(make_tensor_proto("4", shape=[1]))
    request.inputs["type"].CopyFrom(make_tensor_proto("site", shape=[1]))
    request.inputs["lat"].CopyFrom(make_tensor_proto(35000, shape=[1], dtype=float32))
    request.inputs["lon"].CopyFrom(make_tensor_proto(105000, shape=[1], dtype=float32))
    request.inputs["connectiontype"].CopyFrom(make_tensor_proto("2", shape=[1]))
    request.inputs["devicetype"].CopyFrom(make_tensor_proto("1", shape=[1]))
    request.inputs["donottrack"].CopyFrom(make_tensor_proto("0", shape=[1]))
    request.inputs["userid"].CopyFrom(make_tensor_proto("984273063", shape=[1]))
    request.inputs["ua"].CopyFrom(make_tensor_proto("Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; Redmi Note 3 Build/LMY47V) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.8.855 U3/0.8.0 Mobile Safari/534.30", shape=[1]))

    (result, status) = stub.Predict.with_call(request)

    if status.code() != StatusCode.OK:
        print "call failed", status
        return

    predictions = make_ndarray(result.outputs["classes"])

    if predictions.size == 0:
        print "no predition replied"
        return

    cidIndex = predictions[0]
    print "Server predict with index", cidIndex

if __name__ == "__main__":
    from sys import argv, exit

    if argv.__len__() != 3:
        print "Usage: python test.py [host] [port]\n"
        exit(0)

    doTest(argv[1], argv[2])