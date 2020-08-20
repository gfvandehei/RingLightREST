FROM bitnami/python

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY RingLightAPI/ ./RingLightAPI/
COPY app.py .
COPY setup.py .
COPY config.ini .

RUN ls

RUN pip install -e .

CMD ["python", "./app.py", "./config.ini"]