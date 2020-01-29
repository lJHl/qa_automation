# -*- coding: utf-8 -*-
import mysql.connector
import pandas as pd
import logging


class DBWorker:
    def __init__(self, host, user, password, database):
        self.mydb = None
        self.cursor = None
        self.host = host
        self.user = user
        self.passwd = password
        self.database = database
        
        self.logger = logging.getLogger()
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 3)
        pd.set_option('display.width', 250)
        pd.set_option('display.max_colwidth', 150)

    def connect(self):
        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.database
        )
        self.cursor = self.mydb.cursor()

    def disconnect(self):
        self.cursor.close()
        self.mydb.close()

    def execute_exp(self, imp):
        self.cursor.execute(imp)
        return self.cursor.fetchall()

    def log(self, text):
        self.logger.info(pd.DataFrame(text))
