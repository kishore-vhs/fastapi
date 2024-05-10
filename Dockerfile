FROM python:3.11
LABEL app="BOTO3 with FastAPI"
MAINTAINER author="hemasivakishore@gmail.com"
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt \
    && python --version
COPY main.py main.py
EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]