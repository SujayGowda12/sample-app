FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /home/ec2-user/sample-app/logs
RUN chmod 777 /home/ec2-user/sample-app/logs

COPY . .

EXPOSE 5000

CMD ["python", "sample_app.py"]

