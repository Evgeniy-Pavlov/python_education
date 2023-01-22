FROM python:3.9-buster
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD uvicorn main:app --host=0.0.0.0 --port=8000
EXPOSE 8000/tcp
