import socket
import pymysql
import json
from DB_Login import DB_LOGIN
from DB_Connect import DB

HOST = '0.0.0.0'
PORT = 3308


class myServer():
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.USER_DB = DB_LOGIN()
        self.DATA_DB = DB()

    def runServer(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f'start bind in port {PORT}')
        server.bind((HOST, PORT))
        server.listen(10)

        while True:
            conn, addr = server.accept()
            print(f'Connected by {addr}')

            # 獲取資料身分，看資料是誰傳的
            data = str(conn.recv(1024), encoding='utf-8')
            print(json.loads(data))

            # 回傳收到資料
            serverMessage = 'Server Get Request!'
            conn.send(serverMessage.encode('utf-8'))

            # 設定資料讀取或寫入
            dataList = self.getDataFromClient(json.loads(data))

            # 輸出資料給客戶端
            if (json.loads(data)['identity'] == "client"):
                conn.send(json.dumps(dataList).encode('utf-8'))

            # conn.sendall(serverMessage.encode())
            conn.close()

    def saveDataToDB(self, ctl, data):

        self.USER_DB.set_userName(ctl['user'])
        user_file = self.USER_DB.get_User_Table_File()
        self.DATA_DB.set_User_File(user_file)

        self.DATA_DB.DB_SET_DATA(data)

        return

    def getDataFromDB(self, ctl):

        self.USER_DB.set_userName(ctl['user'])
        user_file = self.USER_DB.get_User_Table_File()
        self.DATA_DB.set_User_File(user_file)

        if (str(ctl['action']).isdigit()):
            if (ctl['action'] >= 0):
                data = self.DATA_DB.DB_GET_UNTIL(ctl['action'])
            else:
                print("ERROR HAPPENED: Number is not in range")

            return data
        elif (ctl['action'] == -1):
            data = self.DATA_DB.DB_GET_ALL()

            return data
        else:
            print("ERROR HAPPENED: Not Number")
            return None

    def getDataFromClient(self, data):

        if data["identity"] == "raspberryPi":

            # User file and Action
            # {
            #     "identity": "raspberryPi"
            #     'user': 'amam',
            #     'action': 'action'
            #     'goods': ...
            # }

            ctl = {
                'user': data['user'],
                'action': data['action']
            }

            # Data
            data = {
                'goods': data['goods'],
                'price': data['price'],
                'category': data['category'],
                'spendTime': data['spendTime'],
                'remark': data['remark']
            }

            self.saveDataToDB(ctl, data)

            return None

        elif data["identity"] == "client":

            # User file and Action
            ctl = {
                'user': data['user'],
                'action': data['action']
            }

            dataList = self.getDataFromDB(ctl)

            return dataList

        else:
            print(f"ERROR HAPPENED: {data}")


if __name__ == '__main__':
    server = myServer(HOST, PORT)
    server.runServer()
