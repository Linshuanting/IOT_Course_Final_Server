# -*- coding: utf-8 -*-,
# encoding:utf-8
import json
import pymysql
import sys
import importlib
from DB_USER import DB_USER_TABLE
from DB_Connect import DB

importlib.reload(sys)


class DB_LOGIN():

    def __init__(self):
        self.db_user = DB_USER_TABLE()
        pass

    def set_userName(self, username):
        self.username = username
        pass

    def set_userFile(self, name):

        User_File = {
            'user': self.username,
            'table': name
        }
        return User_File

    def get_User_Table_File(self):

        tableName = self.db_user.get_user_table(self.username)
        File = self.set_userFile(tableName)

        return File


if __name__ == '__main__':
    db = DB_LOGIN()
    db.set_userName('people')
    print(db.get_User_Table_File())
