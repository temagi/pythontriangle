FROM python:3.8

WORKDIR /code

copy . .

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]