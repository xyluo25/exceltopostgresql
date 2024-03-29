import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

try:
    # if have requirements.txt file inside the folder
    with open("requirements.txt", "r", encoding="utf-8") as f:
        modules_needed = [i.strip() for i in fh.readlines()]
except Exception:
    modules_needed = []

setuptools.setup(
    name="exceltopostgresql",
    version="0.2.4",
    author="Xiangyong Luo",
    author_email="rochemay@163.com",
    description="This package help convert your excel files (xlsx,xls,csv) to Postgresql Database.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Xiangyongluo/exceltopostgresql",


    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',

    install_requires=modules_needed,
    packages=setuptools.find_packages(),
    include_package_data=True,

    package_data={'': ['*.txt', '*.xls', '*.xlsx', '*.csv'],
                  "test_data": ['*.txt']}
)
