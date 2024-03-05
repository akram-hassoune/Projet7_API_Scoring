# Projet7_API_Scoring 

- OpenClassrooms - Parcours data scientist - Projet n°7

## Implémentez un modèle de scoring (prêt bancaire)
une société financière, nommée "Prêt à dépenser", qui propose des crédits à la consommation pour des personnes ayant peu ou pas du tout d'historique de prêt.
L’entreprise souhaite mettre en œuvre un outil de “scoring crédit” pour calculer la probabilité qu’un client rembourse son crédit, puis classifie la demande en crédit accordé ou refusé. Elle souhaite donc développer un algorithme de classification en s’appuyant sur des sources de données variées (données comportementales, données provenant d'autres institutions financières, etc.)

## Source

[Source](https://www.kaggle.com/c/home-credit-default-risk/data)

## Boîte à outils



## Mission
- Construire un modèle de scoring qui donnera une prédiction sur la probabilité de faillite d'un client de façon automatique.
- Définir la stratégie d’élaboration d’un modèle d’apprentissage supervisé et sélectionner et entraîner des modèles adaptés à une problématique métier afin de réaliser une analyse prédictive.
- Évaluer les performances des modèles d’apprentissage supervisé selon différents critères (scores, temps d'entraînement, etc.) en adaptant les paramètres afin de choisir le modèle le plus performant pour la problématique métier.
- Définir et mettre en œuvre un pipeline d’entraînement des modèles, avec centralisation du stockage des modèles et formalisation des résultats et mesures des différentes expérimentations réalisées, afin d’industrialiser le projet de Machine Learning.
- Concevoir et assurer un déploiement continu d'un moteur d’inférence (modèle de prédiction encapsulé dans une API) sur une plateforme Cloud afin de permettre à des applications de réaliser des prédictions via une requête à l’API.
- Définir et mettre en œuvre une stratégie de suivi de la performance d’un modèle en production et en assurer la maintenance afin de garantir dans le temps la production de prédictions performantes.

## L'API Scoring 

- Permettre de visualiser le score et l’interprétation de ce score pour chaque client de façon intelligible pour une personne non experte en data science.
- Permettre de visualiser des informations descriptives relatives à un client (via un système de filtre).
- Permettre de visualiser des informations descriptives relatives au prèt d'un client (via un système de filtre).

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/akram-hassoune/Projet7_API_Scoring
```
### STEP 01- Creation d'environement virtual du project 

```bash
python -m venv env
```

```bash
source env/Scripts/activate
```


### STEP 02- installer les requirements
```bash
pip install -r requirements.txt
```


```bash
# Lencement  run de l'api
uvicorn api:app --reload
```

Now,
```bash
open up you local host and port
```

# Déploiement AWS-CICD avec Github Actions

## 1. Connexion à la console AWS.

## 2. Création d'un utilisateur IAM pour le déploiement

    # avec un accès spécifique

    1. Accès EC2 : Il s'agit d'une machine virtuelle.

    2. ECR : Registre de conteneurs élastiques pour sauvegarder votre image Docker dans AWS.


    # Description : À propos du déploiement

    1. Construire une image Docker du code source.

    2. Pousser votre image Docker vers ECR.

    3. Lancer votre EC2.

    4. Tirer votre image depuis ECR dans EC2.

    5. Lancer votre image Docker dans EC2.

    # Politique :

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess

## 3. Création du dépôt ECR pour stocker/sauvegarder l'image Docker
    - Enregistrer l'URI : 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

## 4. Création de la machine EC2 (Ubuntu)

## 5. Ouvrir EC2 et installer Docker sur la machine EC2 :

    # optionnel

    sudo apt-get update -y

    sudo apt-get upgrade
    
    # requis

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

# 6. Configuration d'EC2 en tant que runner auto-hébergé :
    paramètres > actions > runner > nouveau runner auto-hébergé > choisir le système d'exploitation > exécuter ensuite les commandes une par une

# 7. Configuration des secrets Github :

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app

## À propos de MLflow
MLflow

 - C'est de qualité de production
 - Suivre toutes vos expériences
 - Enregistrement et étiquetage de votre modèle

## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)



