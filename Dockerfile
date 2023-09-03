FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir ./image_api
WORKDIR /image_api
COPY . /image_api
RUN pip install -r requirements.txt