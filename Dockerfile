FROM python:3.9-slim

# Mettre à jour le système d'exploitation et installer les dépendances nécessaires
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    build-essential \
    awscli \
 && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers source dans le conteneur
COPY . /app

# Installer les dépendances Python
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel votre application écoute
EXPOSE 8080

# Commande par défaut pour démarrer l'application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
