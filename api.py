"""
execution de l'api : uvicorn api:app --reload
"""

import numpy as np
import pandas as pd
from PIL import Image
import pickle
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import seaborn as sns
import shap
from pandas import to_numeric
from fastapi import FastAPI
from typing import List, Dict, Any
import numpy as np
import io





app = FastAPI()

@app.get("/")
def greet():
    return {"message": "bonjours"}


# ====================================================================
# VARIABLES STATIQUES
# ====================================================================
# Répertoire de sauvegarde du meilleur modèle
FILE_BEST_MODELE = 'resources/modele/best_model.pickle'
# Répertoire de sauvegarde des dataframes nécessaires au dashboard
# Test set brut original
FILE_APPLICATION_TEST = 'resources/data/application_test.pickle'
# Test set pré-procédé
FILE_TEST_SET = 'resources/data/test_set.pickle'
# Dashboard
FILE_DASHBOARD = 'resources/data/df_dashboard.pickle'
# Client
FILE_CLIENT_INFO = 'resources/data/df_info_client.pickle'
FILE_CLIENT_PRET = 'resources/data/df_pret_client.pickle'
# 10 plus proches voisins du train set
FILE_VOISINS_INFO = 'resources/data/df_info_voisins.pickle'
FILE_VOISIN_PRET = 'resources/data/df_pret_voisins.pickle'
FILE_VOISIN_AGG = 'resources/data/df_voisin_train_agg.pickle'
FILE_ALL_TRAIN_AGG = 'resources/data/df_all_train_agg.pickle'
# Shap values
FILE_SHAP_VALUES = 'resources/data/shap_values.pickle'

# ====================================================================
# VARIABLES GLOBALES
# ====================================================================
group_val1 = ['AMT_ANNUITY',
              'BUREAU_CURRENT_CREDIT_DEBT_DIFF_MIN',
              'BUREAU_CURRENT_CREDIT_DEBT_DIFF_MEAN',
              'BUREAU_CURRENT_DEBT_TO_CREDIT_RATIO_MEAN',
              'INST_PAY_AMT_INSTALMENT_SUM']

group_val2 = ['CAR_EMPLOYED_RATIO', 'CODE_GENDER',
              'CREDIT_ANNUITY_RATIO', 'CREDIT_GOODS_RATIO',
              'YEAR_BIRTH', 'YEAR_ID_PUBLISH',
              'EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3',
              'EXT_SOURCE_MAX', 'EXT_SOURCE_SUM',
              'FLAG_OWN_CAR',
              'INST_PAY_DAYS_PAYMENT_RATIO_MAX',
              'POS_CASH_NAME_CONTRACT_STATUS_ACTIVE_SUM',
              'PREV_APP_INTEREST_SHARE_MAX']

group_val3 = ['AMT_ANNUITY_MEAN',
              'BUREAU_CURRENT_CREDIT_DEBT_DIFF_MIN_MEAN',
              'BUREAU_CURRENT_CREDIT_DEBT_DIFF_MEAN_MEAN',
              'BUREAU_CURRENT_DEBT_TO_CREDIT_RATIO_MEAN_MEAN',
              'INST_PAY_AMT_INSTALMENT_SUM_MEAN']

group_val4 = ['CAR_EMPLOYED_RATIO_MEAN', 'CODE_GENDER_MEAN',
              'CREDIT_ANNUITY_RATIO_MEAN', 'CREDIT_GOODS_RATIO_MEAN',
              'YEAR_BIRTH_MEAN', 'YEAR_ID_PUBLISH_MEAN',
              'EXT_SOURCE_1_MEAN', 'EXT_SOURCE_2_MEAN', 'EXT_SOURCE_3_MEAN',
              'EXT_SOURCE_MAX_MEAN', 'EXT_SOURCE_SUM_MEAN',
              'FLAG_OWN_CAR_MEAN',
              'INST_PAY_DAYS_PAYMENT_RATIO_MAX_MEAN',
              'POS_CASH_NAME_CONTRACT_STATUS_ACTIVE_SUM_MEAN',
              'PREV_APP_INTEREST_SHARE_MAX_MEAN']

# ====================================================================
# CHARGEMENT DES DONNEES
# ====================================================================


# Chargement du modèle et des différents dataframes
# Optimisation en conservant les données non modifiées en cache mémoire
# @st.cache(persist = True)

def load():
    try:
        # Import du dataframe des informations des traits stricts du client
        with open(FILE_CLIENT_INFO, 'rb') as df_info_client:
            df_info_client = pickle.load(df_info_client)
            
        # Import du dataframe des informations sur le prêt du client
        with open(FILE_CLIENT_PRET, 'rb') as df_pret_client:
            df_pret_client = pickle.load(df_pret_client)
            
        # Import du dataframe des informations des traits stricts des voisins
        with open(FILE_VOISINS_INFO, 'rb') as df_info_voisins:
            df_info_voisins = pickle.load(df_info_voisins)
            
        # Import du dataframe des informations sur le prêt des voisins
        with open(FILE_VOISIN_PRET, 'rb') as df_pret_voisins:
            df_pret_voisins = pickle.load(df_pret_voisins)

        # Import du dataframe des informations sur le dashboard
        with open(FILE_DASHBOARD, 'rb') as df_dashboard:
            df_dashboard = pickle.load(df_dashboard)

        # Import du dataframe des informations sur les voisins aggrégés
        with open(FILE_VOISIN_AGG, 'rb') as df_voisin_train_agg:
            df_voisin_train_agg = pickle.load(df_voisin_train_agg)

        # Import du dataframe des informations sur les voisins aggrégés
        with open(FILE_ALL_TRAIN_AGG, 'rb') as df_all_train_agg:
            df_all_train_agg = pickle.load(df_all_train_agg)

        # Import du dataframe du test set nettoyé et pré-procédé
        with open(FILE_TEST_SET, 'rb') as df_test_set:
            test_set = pickle.load(df_test_set)

        # Import du dataframe du test set brut original
        with open(FILE_APPLICATION_TEST, 'rb') as df_application_test:
            application_test = pickle.load(df_application_test)

        # Import du dataframe du test set brut original
        with open(FILE_SHAP_VALUES, 'rb') as shap_values:
            shap_values = pickle.load(shap_values)

        # Import du meilleur modèle lgbm entrainé
        with open(FILE_BEST_MODELE, 'rb') as model_lgbm:
            best_model = pickle.load(model_lgbm)
            
    except Exception as e:
        # Gérer les exceptions ici
        print(f"Une erreur s'est produite pendant le chargement des données : {e}")
        return None

    return df_info_client, df_pret_client, df_info_voisins, df_pret_voisins, \
        df_dashboard, df_voisin_train_agg, df_all_train_agg, test_set, \
            application_test, shap_values, best_model

df_info_client, df_pret_client, df_info_voisins, df_pret_voisins, df_dashboard, df_voisin_train_agg, df_all_train_agg, test_set, application_test, shap_values, best_model = load()


"""
{
    "data": (
        df_info_client, 
        df_pret_client, 
        df_info_voisins, 
        df_pret_voisins, 
        df_dashboard, 
        df_voisin_train_agg, 
        df_all_train_agg, 
        test_set, 
        application_test, 
        shap_values, 
        best_model
    )
}
Il s'agit d'un tuple contenant tous les objets que vous avez chargés à partir de la fonction load().
 Chaque objet peut être un DataFrame, un tableau NumPy, un modèle entraîné, etc., 
 selon ce que vous avez chargé dans la fonction load(). 
 Vous pouvez ensuite accéder à chaque objet individuellement à partir de la clé "data" de la réponse de l'API.

"""
@app.get("/client_ids/")
def get_client_ids() -> List[int]:
    # Récupérer la liste des ID clients présents dans df_info_client
    client_ids = df_info_client['SK_ID_CURR'].tolist()
    return client_ids
    

# Endpoint pour obtenir les informations spécifiques d'un client
@app.get("/client_info/{client_id}")
def get_client_info(client_id: int) -> Dict[str, Any]:
    # Récupérer les informations spécifiques du client en fonction de l'ID client
    client_info = df_info_client[df_info_client['SK_ID_CURR'] == client_id].iloc[:, :].to_dict()
    # Vérifier si le client existe
    if len(client_info) == 0:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"client_info": client_info}

# Endpoint pour obtenir les informations Prèt client
@app.get("/client_pret/{client_id}")
def get_client_info(client_id: int) -> Dict[str, Any]:
    # Récupérer les informations spécifiques du client en fonction de l'ID client
    client_pret = df_pret_client[df_pret_client['SK_ID_CURR'] == client_id].iloc[:, :].to_dict()
    # Vérifier si le client existe
    if len(client_pret) == 0:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"client_pret": client_pret}


# Endpoint pour obtenir les scores du client et de ses voisins
@app.get("/client_scores/{client_id}")
def get_client_scores(client_id: int) -> Dict[str, Any]:
    # Sélection des variables du client
    X_test = test_set[test_set['SK_ID_CURR'] == client_id]
    # Score des prédictions de probabilités
    y_proba = best_model.predict_proba(X_test.drop('SK_ID_CURR', axis=1))[:, 1]
    # Score du client en pourcentage arrondi et nombre entier
    score_client = int(np.rint(y_proba * 100))

    # Score moyen des 10 plus proches voisins du test set en pourcentage
    score_moy_voisins_test = int(np.rint(df_dashboard[
        df_dashboard['SK_ID_CURR'] == client_id]['SCORE_10_VOISINS_MEAN_TEST'] * 100))

    # Pourcentage de clients voisins défaillants dans l'historique des clients
    pourc_def_voisins_train = int(np.rint(df_dashboard[
        df_dashboard['SK_ID_CURR'] == client_id]['%_NB_10_VOISINS_DEFAILLANT_TRAIN']))

    # Pourcentage de clients voisins défaillants prédits parmi les nouveaux clients
    pourc_def_voisins_test = int(np.rint(df_dashboard[
        df_dashboard['SK_ID_CURR'] == client_id]['%_NB_10_VOISINS_DEFAILLANT_TEST']))

    # Retourner les scores sous forme de réponse JSON
    return {
        "score_client": score_client,
        "score_moy_voisins_test": score_moy_voisins_test,
        "pourc_def_voisins_train": pourc_def_voisins_train,
        "pourc_def_voisins_test": pourc_def_voisins_test
    }