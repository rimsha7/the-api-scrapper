FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy only what is needed
COPY api_scrapper.py .

# create output folder inside container
RUN mkdir -p /app/output

CMD ["python", "-u", "api_scrapper.py"]