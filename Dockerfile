FROM python:3.6-slim
RUN apt-get update
ADD /app /app
WORKDIR /app
RUN pip3 install -r requirements.txt 
ENV MESSAGE = "OpsLyft, Simplify DevOps For Every Software Team In The World"
EXPOSE 5090
CMD ["python3","app.py"]