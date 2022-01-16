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

userTable_setting = {
    "host": "192.168.10.130",
    "port": 3306,
    "user": "winuser",
    "password": "winuser",
    "db": "userTable",
    "charset": "utf8"
}

userTableName = "USER_DATA"
userArg1 = "myUSER"
userArg2 = "myTABLE"


class DB_USER_TABLE():
    def __init__(self):

        self.user_conn = pymysql.connect(**userTable_setting)
        self.db_conn = pymysql.connect(**db_settings)
        return None

    def get_user_table(self, user_name):

        command = f"select * from {userTableName} where {userArg1} = '{user_name}';"

        tableName = self.db_select(command)

        if (self.is_table_exist(tableName)):
            print(f"{tableName} exist")
            return tableName[0][userArg2]
        else:
            self.create_table(user_name)
            print(f"{user_name}: table create")
            return user_name

    def create_table(self, table_name):

        if (table_name == None):
            return

        cmd = f"CREATE TABLE {table_name} (ID int NOT NULL AUTO_INCREMENT,\
            goods varchar(20), price int(40), category varchar(20),\
            spendTime varchar (30), remark varchar(50), PRIMARY KEY(ID));"

        with self.db_conn.cursor() as cursor:
            cursor.execute(cmd)
            self.db_conn.commit()

        cmd = f"INSERT INTO {userTableName} ({userArg1}, {userArg2}) \
            VALUES (\'{table_name}\', \'{table_name}\');"

        with self.user_conn.cursor() as cursor:
            cursor.execute(cmd)
            self.user_conn.commit()

        pass

    def is_table_exist(self, table_name_list):

        if not table_name_list:
            return False

        cmd = f"SHOW TABLES LIKE '{table_name_list[0]['myTABLE']}';"

        print(cmd)
        if (self.db_select(cmd) != None):
            return True
        else:
            return False

    def db_select(self, command) -> dict:
        result = []
        with self.user_conn.cursor() as cursor:
            cursor.execute(command)
            columns = [column[0] for column in cursor.description]
            for rows in cursor.fetchall():
                result.append(dict(zip(columns, rows)))

            self.user_conn.commit()

        return result

    def db_delete_user(self, username):

        # 刪除資料庫用戶資料
        cmd = f"DELETE FROM {userTableName} WHERE {userArg1}='{username}'"
        with self.user_conn.cursor() as cursor:
            cursor.execute(cmd)
            self.user_conn.commit()
        print("delete user successful")

        # 刪除用戶表格
        cmd = f"DROP TABLE {username}"
        with self.db_conn.cursor() as cursor:
            cursor.execute(cmd)
            self.db_conn.commit()
        print("delete user data successful~")

        pass

    def db_insert(self, table_name):

        cmd = f"INSERT INTO {userTableName} ({userArg1}, {userArg2}) \
            VALUES (\'{table_name}\', \'{table_name}\');"

        with self.user_conn.cursor() as cursor:
            cursor.execute(cmd)
            self.user_conn.commit()

        print("Insert successful")

    def run(self):
        pass

    def show_json(self, myfile):
        print(json.dumps(myfile, sort_keys=True))
        pass


if __name__ == '__main__':
    db = DB_USER_TABLE()
    # db.db_insert('people')
    # db.db_delete_user('people')
    name = db.get_user_table('people')
    print(name)
