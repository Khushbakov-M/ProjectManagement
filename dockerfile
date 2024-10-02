FROM python:3.12

WORKDIR /projectmanager

COPY requirements.txt /projectmanager/

RUN apt-get update && apt-get install -y apturl

RUN pip install --no-cache-dir -r requirements.txt

COPY . /projectmanager/

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]