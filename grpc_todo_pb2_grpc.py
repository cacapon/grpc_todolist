# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import grpc_todo_pb2 as grpc__todo__pb2


class GrpcTODOStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetTodoCommand = channel.unary_unary(
        '/GrpcTODO/GetTodoCommand',
        request_serializer=grpc__todo__pb2.CommandRequest.SerializeToString,
        response_deserializer=grpc__todo__pb2.CommandResponse.FromString,
        )
    self.InputMode = channel.unary_unary(
        '/GrpcTODO/InputMode',
        request_serializer=grpc__todo__pb2.MessageRequest.SerializeToString,
        response_deserializer=grpc__todo__pb2.MessageResponse.FromString,
        )
    self.SelectMode = channel.unary_unary(
        '/GrpcTODO/SelectMode',
        request_serializer=grpc__todo__pb2.MessageRequest.SerializeToString,
        response_deserializer=grpc__todo__pb2.MessageResponse.FromString,
        )
    self.SelectModeDecision = channel.unary_unary(
        '/GrpcTODO/SelectModeDecision',
        request_serializer=grpc__todo__pb2.DecisionRequest.SerializeToString,
        response_deserializer=grpc__todo__pb2.MessageResponse.FromString,
        )


class GrpcTODOServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetTodoCommand(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InputMode(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SelectMode(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SelectModeDecision(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GrpcTODOServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetTodoCommand': grpc.unary_unary_rpc_method_handler(
          servicer.GetTodoCommand,
          request_deserializer=grpc__todo__pb2.CommandRequest.FromString,
          response_serializer=grpc__todo__pb2.CommandResponse.SerializeToString,
      ),
      'InputMode': grpc.unary_unary_rpc_method_handler(
          servicer.InputMode,
          request_deserializer=grpc__todo__pb2.MessageRequest.FromString,
          response_serializer=grpc__todo__pb2.MessageResponse.SerializeToString,
      ),
      'SelectMode': grpc.unary_unary_rpc_method_handler(
          servicer.SelectMode,
          request_deserializer=grpc__todo__pb2.MessageRequest.FromString,
          response_serializer=grpc__todo__pb2.MessageResponse.SerializeToString,
      ),
      'SelectModeDecision': grpc.unary_unary_rpc_method_handler(
          servicer.SelectModeDecision,
          request_deserializer=grpc__todo__pb2.DecisionRequest.FromString,
          response_serializer=grpc__todo__pb2.MessageResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'GrpcTODO', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
