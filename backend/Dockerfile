FROM python:3.9

WORKDIR /backend

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 8000

COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi"]