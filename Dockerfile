
FROM mysql:latest

RUN pip install mysql-connector-python

RUN pip install flask

COPY mysqlpython.py /

CMD ./mysqlpython.py
