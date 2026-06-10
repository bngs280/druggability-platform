FROM continuumio/miniconda3

WORKDIR /app

COPY . /app

RUN pip install \
fastapi \
uvicorn \
pandas \
numpy \
scikit-learn \
xgboost \
joblib

CMD ["uvicorn",
"src.api.main:app",
"--host",
"0.0.0.0",
"--port",
"8080"]