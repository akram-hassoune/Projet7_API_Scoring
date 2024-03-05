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

