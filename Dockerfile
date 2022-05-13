FROM python

RUN pip3 install requests
WORKDIR "/app"
COPY reqtotaltime.py .
ENV site=http://www.google.com
ENV times=5

RUN pip install beautifulsoup4
CMD ["python3", "reqtotaltime.py"]
