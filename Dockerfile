FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir streamlit

COPY . .

EXPOSE 8000 8501

CMD uvicorn app:app --host 0.0.0.0 --port 8000 & \
    streamlit run frontend.py --server.port 8501 --server.address 0.0.0.0