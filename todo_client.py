import grpc
import grpc_todo_pb2
import grpc_todo_pb2_grpc

from getch import GetCh
from subprocess import call

def input_mode():
    # addコマンドの後
    mes = input('>>>')
    call('clear')
    return mes 

def select_mode():
    # listを選択できる状態
    key_list = {
    119: 'up',  # winddows用のキー配置
    115: 'down',# winddows用のキー配置
    13 : 'enter'# winddows用のキー配置
    }

    return key_list.get(ord(GetCh.getch()))


if __name__ == "__main__":
    with grpc.insecure_channel('localhost:50051') as ch:
        stub = grpc_todo_pb2_grpc.GrpcTODOStub(ch)
        while True:
            cmd = input('CLIなTODOです。何をしますか？ (qキーでおしまい)\n>>>')
            call('clear')
            if cmd == 'q':
                break
            res = stub.GetTodoCommand(grpc_todo_pb2.CommandRequest(cmd=cmd))
            if res.res == 'データがありません':
                print(res.res)
                continue

            if res.select_mode is True:
                res_s_mode = ''
                print('listを選択してください。(w:↑ s:↓ Enter:決定)')
                while True:
                    mes = select_mode()
                    call('clear')
                    if mes == 'up' or mes == 'down':
                        show_list = stub.GetTodoCommand(grpc_todo_pb2.CommandRequest(cmd='show')) 
                        print(show_list.res)
                        res_s_mode = stub.SelectMode(grpc_todo_pb2.MessageRequest(mes=mes))
                        print('>>>' + res_s_mode.res.rstrip())
                    if mes == 'enter':
                        if res_s_mode != '':
                            res_s_mode = stub.SelectModeDecision(grpc_todo_pb2.DecisionRequest(cmd=cmd,mes=res_s_mode.res))
                            show_list = stub.GetTodoCommand(grpc_todo_pb2.CommandRequest(cmd='show')) 
                            print(show_list.res)
                            print(res_s_mode.res)
                            break
                        else:
                            print('listを選択してください。(w:↑ s:↓ Enter:決定)')
            if res.input_mode is True:
                print(res.res)
                mes = input_mode()
                res = stub.InputMode(grpc_todo_pb2.MessageRequest(mes=mes))

            print(res.res)
