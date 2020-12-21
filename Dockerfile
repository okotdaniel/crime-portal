FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /crime-portal
COPY requirements.txt /crime-portal/
RUN pip install -r requirements.txt
COPY . /crime-portal/