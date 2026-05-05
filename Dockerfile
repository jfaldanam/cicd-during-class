FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY model.pkl .
COPY src.py .

ENTRYPOINT ["python", "src.py"]
CMD ["predict", "--help"]
