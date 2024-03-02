# exceltopostgresql

Automatically save your local excel files (xlsx,xls,csv) onto Postgresql database

# Introduction

This package help to convert your excel files (xlsx,xls,csv) to postgresql database.

# Installation

exceltopostgresql can be installed as:

```python
pip install exceltopostgresql
```

# Dependency

👍 [pandas](https://pandas.pydata.org/)

👍 [psycopg2](https://pypi.org/project/psycopg2/)

👍 [sqlalchemy](https://www.sqlalchemy.org/)

# QuickStart

```python
import exceltopostgresql as ep
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


# STEP Two connect to postgresql server and load your input data
ep.exceltoDBtable(yourFile,yourHostORip,yourUsrID,yourPWD,yourDBname,save2tableName)

# STEP Three, save loaded data onto postgresql
ep.save2db()

```


```
output:
Successfully load excel data...
Secessfully connected to postgresql...
Secessfully saved 'yourtable' to Postgresql...
```

# API Reference

exceltopostgresql.ExcelToDB(`filePath, host_ip="", usrID ="", pwd="", database_name="", port= "5432", rename_table=""`)

```
Args:
            filePath (str): [path of your input file name]
            host_ip (bool, optional): the ip of your host machine. Defaults to "".
            usrID (bool, optional): user id of your postgresql database. Defaults to "".
            pwd (bool, optional): password of your postgresql database. Defaults to "".
            database_name (bool, optional): the exact database name you want your data save to. Defaults to "".
            port (str, optional): the postgresql port. Defaults to "5432".
            rename_table (bool, optional): rename your input table.
                if "", will use exact the same table name of your input file. Defaults to "".
```
