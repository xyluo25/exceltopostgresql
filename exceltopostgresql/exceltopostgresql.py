# -*- coding:utf-8 -*-
##############################################################
# Created Date: Friday, December 3rd 2021
# Contact Info: luoxiangyong01@gmail.com
# Author/Copyright: Mr. Xiangyong Luo
##############################################################


import socket

import pandas as pd
import psycopg2
import sqlalchemy
from pyufunc import func_running_time

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)


class ExcelToDB:
    """This is a model to automatically save your local excel file (xlsx,xls,csv) to your Postgresql Database
        define inputs variables

        Args:
            filePath (str): [path of your input file name]
            host_ip (bool, optional): the ip of your host machine. Defaults to "".
            usrID (bool, optional): user id of your postgresql database. Defaults to "".
            pwd (bool, optional): password of your postgresql database. Defaults to "".
            database_name (bool, optional): the exact database name you want your data save to. Defaults to "".
            port (str, optional): the postgresql port. Defaults to "5432".
            rename_table (bool, optional): rename your input table.
                if "", will use exact the same table name of your input file. Defaults to "".

        Raises:
            Exception: [if the inputs in not correct then raise exceptions]: Partially inputs, please check your inputs...
        """

    def __init__(self,
                 filePath: str,
                 host_ip: str = "",
                 usrID: str = "",
                 pwd: str = "",
                 database_name: str = "",
                 port: str = "5432",
                 rename_table: str = ""):

        if not any([host_ip, database_name, usrID, pwd]):
            raise Exception("Partially inputs, please check your inputs...")

        self.filePath = filePath
        self.host_ip = host_ip
        self.database_name = database_name
        self.usrID = usrID
        self.pwd = pwd
        self.port = port
        self.rename_table = rename_table

        self.postgresql_cur()
        self.readData()
        self.save2database()

    def postgresql_cur(self):
        db_url = f"postgresql+psycopg2://{self.usrID}:{self.pwd}@{self.host_ip}:{self.port}/{self.database_name}"
        self.engine = sqlalchemy.create_engine(db_url)

    def readData(self) -> None:
        if self.filePath.split(".")[-1] in ["xlsx", "xls"]:
            self.file_data = pd.read_excel(self.filePath)
            print("Successfully load excel data...")
        elif self.filePath.split(".")[-1] in ["csv"]:
            self.file_data = pd.read_csv(self.filePath)
            print("Successfully load csv data...")
        else:
            raise Exception("Unable to load input file...")

    @func_running_time
    def save2database(self) -> None:
        # specify the table name
        if self.rename_table:
            tableName = self.rename_table
        elif "/" in self.filePath:
            tableName = self.filePath.split("/")[-1].split(".")[0]
        else:
            tableName = self.filePath.split(".")[0]

        # using pandas to save table to database
        try:
            self.file_data.to_sql(tableName, con=self.engine)
            print("Successfully save %s into Postgresql Database..." % tableName)
        except Exception as e:
            raise Exception(e) from e