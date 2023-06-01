# exceltopostgresql

A model to automatically save your local excel file (xlsx,xls,csv) onto your postgresql database

# Introduction

This package help to convert your excel files (xlsx,xls,csv) to postgresql database.

# Installation

exceltopostgresql can be installed as:

```
pip install exceltopostgresql
```

# Dependency

👍 [pandas](https://pandas.pydata.org/)

👍 [psycopg2](https://pypi.org/project/psycopg2/)

👍 [sqlalchemy](https://www.sqlalchemy.org/)

# QuickStart

```
import exceltosqlserver as ep
# generate the class instance

# STEP One, prepare your input pareameters

yourFile  = "test01.xls"  # available for xlsx, xls,csv
yourUsrID = ""
yourPWD   = ""
yourDBname= ""
rename_table = ""
	# "": save your file name as table name onto posgtresql
	# or
	# customize your table, like: "test"

# get your local host name
# this will return your local computer name for your sql server database
host_name = ep.hostname
or
host_name = "localhost"

# get your local ip address
# this will return your local ip address (if your sql server can be accessed by DNS)
ip = ep.local_ip

# you need to change your host if needed, dns: local ip address
#yourHostORip  = "localhost"
# yourHostORip  = host_name
yourHostORip  = ip


# STEP Two  convert your data to sql server
ep.exceltoDBtable(yourFile,yourHostORip,yourUsrID,yourPWD,yourDBname,save2tableName)
```

```
output:
Successfully load excel data...
Secessfully connected to SQL Server...
Secessfully saved 'yourtable' to Posggresql...
```

# API Reference

exceltopostgresql.exceltoDBtable(`filePath, host_ip="", usrID ="", pwd="", database_name="", port= "5432", rename_table=""`)

```
Args:
            filePath (str): [path of your input file name]
            host_ip (bool, optional): [description]. Defaults to "".
            usrID (bool, optional): [description]. Defaults to "".
            pwd (bool, optional): [description]. Defaults to "".
            database_name (bool, optional): [description]. Defaults to "".
            port (str, optional): [description]. Defaults to "5432".
            save2tableName (bool, optional): [description]. Defaults to "".
```
