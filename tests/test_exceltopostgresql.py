# -*- coding:utf-8 -*-
##############################################################
# Created Date: Monday, February 26th 2024
# Contact Info: luoxiangyong01@gmail.com
# Author/Copyright: Mr. Xiangyong Luo
##############################################################


import pytest
from exceltopostgresql import ExcelToDB

import sqlalchemy
import psycopg2
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))


def test_excel_to_db_postgresql_cur():
    # Test case 1: Valid database URL
    excel_to_db = ExcelToDB("path/to/file.xlsx", "localhost", "user", "password", "database")
    excel_to_db._postgresql_cur()
    assert excel_to_db.engine is not None


def test_excel_to_db_read_data():
    # Test case: Load csv data
    excel_to_db = ExcelToDB("datasets/example_1.cvs", "localhost", "user", "password", "database")

    with pytest.raises(Exception) as exec_info:
        excel_to_db._readData()
    assert "Unable to load input file" in str(exec_info.value)


def test_excel_to_db_read_data_2():
    # Test case: Load xlsx data
    excel_to_db = ExcelToDB("./datasets/example_1.csv", "localhost", "user", "password", "database")
    excel_to_db._readData()
    assert excel_to_db.file_data is not None
