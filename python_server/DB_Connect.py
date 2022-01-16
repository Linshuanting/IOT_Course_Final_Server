# -*- coding: utf-8 -*-,
# encoding:utf-8
import json
import pymysql
import sys
import importlib

importlib.reload(sys)

db_settings = {
    "host": "192.168.10.130",
    "port": 3306,
    "user": "winuser",
    "password": "winuser",
    "db": "fileDataBase",
    "charset": "utf8"
}

TestData = {
    'goods': 'dcard',
    'price': 50,
    'category': '社群網站',
    'spendTime': '12/20',
    'remark': 'No'
}

'''
DataFormat_example = {
    'goods': 'example',
    'price': 50,
    'category': '社群網站',
    'spendTime': '12/20',
    'remark': 'No'
}

DataControl_example = {
SELECT * FROM people WHERE id > 2;
    'user': 'winuser',
    'table': 'people',   // your table
    'action': 'select',  // select update delete insert
    'id': '*' ,
    'chg_type': 'int',   // varchar or int or NULL
    'chg_name': 'id',
    'chg_ope': '>',
    'chg_detail': '2'
}
'''


class DB():
    def __init__(self):
        self.conn = pymysql.connect(**db_settings)
        return None

    def ToJSON(self, data) -> dict:
        return json.loads(data)

    def ToJSONString(self, data):
        return json.dumps(data)

    def set_User_File(self, user):
        self.USER_FILE = user

    # command 為 sql 指令，回傳時是 json 格式
    def DB_SELECT(self, command) -> dict:

        result = []
        with self.conn.cursor() as cursor:
            cursor.execute(command)
            columns = [column[0] for column in cursor.description]
            for rows in cursor.fetchall():
                result.append(dict(zip(columns, rows)))

            self.conn.commit()

        return result

    def DB_UPDATE(self, ctl):

        if (ctl["int"]):
            command = f'UPDATE  {ctl["table"]} SET {ctl["chg_name"]}={ctl["chg_detail"]}\
                WHERE ID={ctl["id"]}'
        elif (ctl["varchar"]):
            command = f'UPDATE  {ctl["table"]} SET {ctl["chg_name"]}=\'{ctl["chg_detail"]}\'\
                WHERE ID={ctl["id"]}'

        with self.conn.cursor() as cursor:
            cursor.execute(command)
            self.conn.commit()

    def DB_DELETE(self, id):
        command = f'DELETE FROM {self.USER_FILE["table"]} WHERE ID={id}'

        with self.conn.cursor() as cursor:
            cursor.execute(command)
            self.conn.commit()

    def DB_SET_DATA(self, data):

        command = f'INSERT INTO {self.USER_FILE["table"]} (goods, price, category, spendTime, remark) \
            VALUES (\'{data["goods"]}\', {data["price"]}, \'{data["category"]}\' \
            , \'{data["spendTime"]}\', \'{data["remark"]}\')'

        with self.conn.cursor() as cursor:
            cursor.execute(command)
            self.conn.commit()

    def DB_GET_NEW(self):

        command = f'SELECT * FROM {self.USER_FILE["table"]} \
                ORDER BY ID DESC LIMIT 1'

        result = self.DB_SELECT(command)

        return result

    def DB_GET_ALL(self):

        command = f'SELECT * FROM {self.USER_FILE["table"]}'

        result = self.DB_SELECT(command)

        return result

    def DB_GET_UNTIL(self, until_id):

        command = f'SELECT * FROM {self.USER_FILE["table"]} \
                    WHERE ID > {until_id}'

        result = self.DB_SELECT(command)

        return result


if __name__ == '__main__':
    db = DB()
    user = {
        'user': 'people',
        'table': 'people'
    }
    db.set_User_File(user)

    result = db.DB_GET_ALL()
    print(result)
