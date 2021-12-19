

FROM python:3-slim

RUN pip install mysql-connector-python

RUN pip install flask

COPY mysql_with_webserver.py /

CMD ["/mysql_with_webserver.py"]
