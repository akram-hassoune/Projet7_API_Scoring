







class PredictionPipeline:
    def __init__(self):
        

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