FROM python:3.9
WORKDIR /smssync
COPY ./requirements.txt /smssync/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /smssync/requirements.txt
COPY ./api /smssync/api
WORKDIR /smssync/api
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]