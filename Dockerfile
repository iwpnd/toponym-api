FROM python:3.7

RUN pip install fastapi uvicorn
RUN pip install git+https://github.com/iwpnd/toponym.git

EXPOSE 80

COPY ./toponym_api/app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
