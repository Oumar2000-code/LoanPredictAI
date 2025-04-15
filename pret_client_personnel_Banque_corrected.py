
import os
os.system("pip install joblib")

import streamlit as st
import pandas as pd
import joblib

# Chargement du modèle entraîné
model = joblib.load('modele_random_forest.pkl')

def predict_personal_loan(input_data):
    """Effectue une prédiction avec le modèle."""
    prediction = model.predict(input_data)
    return prediction[0]

def main():
    st.title("Prédiction de prêt personnel")
    st.write("Veuillez entrer les informations du client.")

    id_client = st.number_input("ID", min_value=0, value=1)
    age = st.number_input("Âge", min_value=18, max_value=100, value=30)
    experience = st.number_input("Expérience", min_value=0, value=5)
    income = st.number_input("Revenu annuel", min_value=0, value=50000)
    zip_code = st.number_input("Code Postal", min_value=0, value=10000)
    family = st.number_input("Taille de la famille", min_value=1, max_value=4, value=2)
    ccavg = st.number_input("Moyenne des dépenses sur les cartes de crédit", min_value=0.0, value=1000.0)
    education = st.selectbox("Niveau d'éducation", [1, 2, 3])
    mortgage = st.number_input("Montant de l'hypothèque", min_value=0, value=0)
    securities_account = st.selectbox("Compte de titres", [0, 1])
    cd_account = st.selectbox("Compte de dépôt à terme", [0, 1])
    online = st.selectbox("Services bancaires en ligne", [0, 1])
    creditcard = st.selectbox("Carte de crédit", [0, 1])

    input_data = pd.DataFrame({
        'ID': [id_client],
        'Age': [age],
        'Experience': [experience],
        'Income': [income],
        'ZIP Code': [zip_code],
        'Family': [family],
        'CCAvg': [ccavg],
        'Education': [education],
        'Mortgage': [mortgage],
        'Securities Account': [securities_account],
        'CD Account': [cd_account],
        'Online': [online],
        'CreditCard': [creditcard]
    })

    if st.button("Prédire"):
        prediction = predict_personal_loan(input_data)
        if prediction == 1:
            st.success("✅ Le client est susceptible de souscrire un prêt personnel.")
        else:
            st.error("❌ Le client n'est pas susceptible de souscrire un prêt personnel.")

if __name__ == '__main__':
    main()
