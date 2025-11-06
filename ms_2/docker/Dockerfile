FROM python:3.10-slim

WORKDIR /app

COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

EXPOSE 8000

ENV A2T_MODEL_PATH=""
ENV T2S_MODEL_PATH=""

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]