FROM python:3.12-slim

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN RUN apt-get install -y build-essential
RUN pip install --upgrade pandas shap
RUN pip install -r packages.txt

# Exposez le port sur lequel votre application écoute
EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
