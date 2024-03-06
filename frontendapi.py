import streamlit as st
import pandas as pd
import requests

# Fonction pour récupérer la liste des IDs clients depuis l'API
def get_client_ids():
    response = requests.get("http://13.60.6.135:8080/client_ids/")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Erreur lors de la récupération des IDs clients")

                                  
# Fonction pour récupérer les informations client et de prêt à partir de l'API
def get_client_info(client_id):
    # Appeler l'API pour obtenir les informations client
    response_client_info = requests.get(f"http://13.60.6.135:8080/client_info/{client_id}")
    client_info = response_client_info.json()["client_info"]

    # Appeler l'API pour obtenir les informations de prêt
    response_pret_info = requests.get(f"http://13.60.6.135:8080/client_pret/{client_id}")
    pret_info = response_pret_info.json()["client_pret"]

    return client_info, pret_info

# Fonction pour récupérer la prévision de défaut à partir de l'API
def get_default_prediction(client_id):
    # Appeler l'API pour obtenir la prévision de défaut
    response_default_prediction = requests.get(f"http://13.60.6.135:8080/client_scores/{client_id}")
    default_prediction = response_default_prediction.json()["score_client"]
    return default_prediction

# Titre de l'application
st.title("Informations sur le client")

# Sélection de l'ID client
client_ids = get_client_ids()
selected_client_id = st.selectbox("Sélectionnez un client:", client_ids)

# Bouton pour afficher les informations
if st.button("Afficher les informations"):
    # Récupérer les informations client et de prêt
    client_info, pret_info = get_client_info(selected_client_id)
    # Afficher les informations client dans un tableau coloré
    st.subheader("Informations client")
    st.dataframe(pd.DataFrame.from_dict(client_info).style.set_table_styles([{
        'selector': 'td',
        'props': [('background-color', '#7FFFD4')] # Couleur de fond des cellules
    }]))
    # Afficher les informations de prêt dans un tableau coloré
    st.subheader("Informations de prêt")
    st.dataframe(pd.DataFrame.from_dict(pret_info).style.set_table_styles([{
        'selector': 'td',
        'props': [('background-color', '#FFA07A')] # Couleur de fond des cellules
    }]))

    # Récupérer la prévision de défaut
    default_prediction = get_default_prediction(selected_client_id)
    # Afficher la prévision de défaut
    st.subheader("Prévision de défaut")
    st.write(f"Le client a une probabilité de défaut de : {default_prediction}%")
