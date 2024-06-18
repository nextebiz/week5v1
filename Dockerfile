FROM python:latest

COPY . .

RUN pip install -r req.txt

ENTRYPOINT python main.py