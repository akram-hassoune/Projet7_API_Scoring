FROM python:3.12-slim

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    build-essential \
    awscli \
 && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers source dans le conteneur
COPY . /app

RUN apt-get install -y build-essential
RUN pip install --upgrade pandas shap
RUN pip install -r packages.txt
# Exposer le port sur lequel votre application écoute
EXPOSE 8080

# Commande par défaut pour démarrer l'application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
