import socket
import json

HOST = '192.168.10.130'
PORT = 3308


class myClient():
    def __init__(self):
        pass

    def sendData(self, data):

        # 送出資料到server
        cmd = data
        self.server.send(cmd.encode('utf-8'))

    def getData(self):

        # server 確認收到回傳ACK
        data = self.server.recv(1024)
        print("server send : %s " % (data.decode()))

        return data

    def connectServer(self):

        print('connect start')
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((HOST, PORT))
        print('connect successful')

    def run(self):

        self.connectServer()

        yourdata = {
            # 這裡需要將樹梅派讀出的資料寫入
            # 範例格式如下:
            'identity': "raspberryPi",
            'user': 'people',
            'action': 'POST',
            'goods': 'driver',
            'price': 40,
            'category': '水果',
            'spendTime': '12/27',
            'remark': 'driver pie'
        }

        self.sendData(json.dumps(yourdata))

        # Server 接收到後，會回傳確認鍵
        data = self.getData()
        print(data)


if __name__ == '__main__':
    cli = myClient()
    cli.run()
