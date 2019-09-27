from concurrent import futures
import time

import grpc
import grpc_todo_pb2
import grpc_todo_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class GrpcTODOServer(grpc_todo_pb2_grpc.GrpcTODOServicer):
    def __init__(self):
        self.data_index = 0

    def GetTodoCommand(self, request, context):
        print('get command:{}'.format(request.cmd))
        if request.cmd == 'show':
            return grpc_todo_pb2.CommandResponse(res=self._cmd_show())
        if request.cmd == 'add':
            return grpc_todo_pb2.CommandResponse(res=self._cmd_add(),input_mode=True)
        if request.cmd == 'done':
            return grpc_todo_pb2.CommandResponse(res=self._data_ck(),select_mode=True)
        if request.cmd == 'undone':
            return grpc_todo_pb2.CommandResponse(res=self._data_ck(),select_mode=True)
        if request.cmd == 'delete':
            return grpc_todo_pb2.CommandResponse(res=self._data_ck(),select_mode=True)

        return grpc_todo_pb2.CommandResponse(res=self._cmd_usage())


    def _cmd_show(self):
        # 保存しているリストをクライアントに表示します。
        with open('data.csv',mode='r') as csv:
            return csv.read()

    def _cmd_add(self):
        # リストに新しいTODOを追加します。
        # 入力画面に移行し、そこで入力したタイトルをTODOとして保存します。
        return '追加するタイトルを入力してください'

    def _data_ck(self):
        # done,undone,delete実行時,data.csvが空だったら動作させなくする。
        with open('data.csv',mode='r') as csv:
            data = csv.readlines()

        if len(data) == 0:
            return 'データがありません'
        else :
            return ''

    def _cmd_usage(self):
        # デフォルト
        # 使い方を表示します。
        usage = (
            '[使い方]\nコマンドを入力して、TODOの操作を行ってください。\n\n'
            '[コマンド一覧]\n'
            'show:現在のTODOを表示します。\n'
            'add:TODOに追加します。\n'
            'done:選択したTODOを完了済みにします。\n'
            'undone:選択したTODOを見完了にします。\n'
            'delete:選択したTODOを削除します。\n\n'
            '[addについて]\n'
            'addコマンド後、入力画面に移行します。\n'
            'タイトルを入力後、Enterを押せば登録完了です。\n\n'
            '[選択画面について]\n'
            'done,undone,deleteに関してはコマンド入力後選択画面に移行します。\n'
            'wキーとsキーで選択後、Enterを押してください。\n\n'
        )
        return usage
    def _select_mode():
        # w,sで動かす選択画面に以降します。
        # Enterを押されたリストを返します。
        pass

    def InputMode(self, request, context):
        ret_mes = 'TODOリストに登録しました:{}'.format(request.mes)
        with open('data.csv',mode='a') as csv:
            csv.write(request.mes + ',Undone\n')
        return grpc_todo_pb2.MessageResponse(res=ret_mes)

    def SelectMode(self, request, context):
        with open('data.csv',mode='r') as csv:
            data = csv.readlines()
        
        if len(data) == 0:
            res = 'データがありません'
            return grpc_todo_pb2.MessageResponse(res=res)

        if request.mes == 'up':
            self.data_index -= 1
        
        if request.mes == 'down':
            self.data_index += 1

        if self.data_index >= len(data) -1:
            self.data_index = len(data) -1

        if self.data_index <= 0:
            self.data_index = 0

        return grpc_todo_pb2.MessageResponse(res=data[self.data_index])
    
    def SelectModeDecision(self, request, context):
        # 対象のデータを書き換え、csvに保存します。
        cmd_mes = {
            'done':'完了に',
            'undone':'未完了に',
            'delete':'削除'
            }

        with open('data.csv',mode='r') as csv:
            data = csv.readlines()
            for i,row in enumerate(data):
                if request.mes in row:
                    if request.cmd == 'done':
                        data[i] = data[i].replace('Undone','Done')
                        ret_data = data[i].split(',')[0]
                    if request.cmd == 'undone':
                        data[i] = data[i].replace('Done','Undone')
                        ret_data = data[i].split(',')[0]
                    if request.cmd == 'delete':
                        ret_data = data.pop(i).split(',')[0]

        with open('data.csv',mode='w') as csv:
            csv.writelines(data)
            ret_mes = '{}を{}しました。'.format(ret_data,cmd_mes[request.cmd])
            return grpc_todo_pb2.MessageResponse(res=ret_mes)
            
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_todo_pb2_grpc.add_GrpcTODOServicer_to_server(GrpcTODOServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()
