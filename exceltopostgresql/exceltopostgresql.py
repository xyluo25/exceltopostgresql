# -*- coding:utf-8 -*-
##############################################################
# Created Date: Friday, December 3rd 2021
# Contact Info: luoxiangyong01@gmail.com
# Author/Copyright: Mr. Xiangyong Luo
##############################################################


import sqlalchemy
import psycopg2
import pandas as pd
import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)


class exceltoDBtable:
    """This is a model to automatically save your local excel file (xlsx,xls,csv) onto your postgresql database
        define inputs variables

        Args:
            filePath (str): [path of your input file name]
            host_ip (bool, optional): [description]. Defaults to False.
            usrID (bool, optional): [description]. Defaults to False.
            pwd (bool, optional): [description]. Defaults to False.
            database_name (bool, optional): [description]. Defaults to False.
            port (str, optional): [description]. Defaults to "5432".
            save2tableName (bool, optional): [description]. Defaults to False.

        Raises:
            Exception: [if the inputs in not correct then raise exceptions]
        """
    
    def __init__(self,filePath,host_ip=False,usrID =False,pwd=False,database_name=False,port:str= "5432",save2tableName=False):
        
        if not any([host_ip,database_name,usrID,pwd]):
            raise Exception("Partially inputs, please check your inputs...")
        else:
            self.filePath = filePath
            self.host_ip = host_ip
            self.database_name=database_name
            self.usrID = usrID
            self.pwd = pwd
            self.port = port
            self.save2tableName = save2tableName
            
        self.postgresql_cur()
        self.readData()
        self.save2database()
        
        
    def postgresql_cur(self):
        db_url = f"postgresql+psycopg2://{self.usrID}:{self.pwd}@{self.host_ip}:{self.port}/{self.database_name}"
        self.engine = sqlalchemy.create_engine(db_url)

    def readData(self) -> "DataFrame":
        if self.filePath.split(".")[-1] in ["xlsx","xls"]:
            self.file_data = pd.read_excel(self.filePath)
            print("Successfully load excel data...")
        elif self.filePath.split(".")[-1] in ["csv"]:
            self.file_data = pd.read_csv(self.filePath)
            print("Successfully load csv data...")
        else:
            raise Exception("Unable to load input file...")
    
    def save2database(self) ->"DataFrame to database":
        # specificy the table name
        if self.save2tableName:
            tableName = self.save2tableName
        else:
            if "/" in self.filePath:
                tableName = self.filePath.split("/")[-1].split(".")[0]
            else:
                tableName = self.filePath.split(".")[0]
                
        # using pandas to save table to database
        try:
            self.file_data.to_sql(tableName,con=self.engine)
            print("Successfully save %s into database..."%tableName)
        except Exception as e:
            raise Exception(e)