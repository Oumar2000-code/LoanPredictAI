# 📊 LoanPredictAI – Application de Prédiction de Prêt Personnel

**LoanPredictAI** est une application intelligente qui utilise un modèle de machine learning (Random Forest) pour prédire si un client est susceptible de souscrire un prêt personnel. Développée avec Streamlit, elle propose une interface simple et intuitive pour les institutions financières, les fintechs ou les analystes de crédit.

---

## ✨ Fonctionnalités

- Saisie des informations client via formulaire interactif
- Prédiction automatique basée sur un modèle Random Forest
- Interface Web facile à utiliser
- Messages de résultat clairs (accepté ou refusé)
- Prête à être déployée (localement ou sur Streamlit Cloud)

---

## 🧠 Technologies utilisées

- Python
- Scikit-learn
- Joblib
- Pandas
- Streamlit

---

## 🚀 Installation locale

1. Clonez le dépôt :
```bash
git clone https://github.com/votre-utilisateur/loan-predict-ai.git
cd loan-predict-ai
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Lancez l'application :
```bash
streamlit run pret_client_personnel_Banque_corrected.py
```

---

## 🌐 Déploiement sur [Streamlit Cloud](https://streamlit.io/cloud)

1. Créez un nouveau projet sur Streamlit Cloud
2. Uploadez les fichiers :
   - `pret_client_personnel_Banque_corrected.py`
   - `modele_random_forest.pkl`
   - `requirements.txt`
3. Configurez le fichier principal dans les paramètres du projet
4. Lancez l’app directement depuis le navigateur

---

## 🧪 Exemple d’utilisation

L’utilisateur remplit les champs du formulaire :
- Âge : 30
- Revenu annuel : 50,000
- Carte de crédit : Oui
- Compte de titres : Non
- etc.

👉 L’application affiche :  
**✅ Le client est susceptible de souscrire un prêt personnel.**

---

## 👨‍💻 Auteur

Développé par **Oumar Koulibaly**  
📧 Email : coulibalyoumara2000@gmail.com

---

## 📁 Structure du projet

```
📦 loan-predict-ai/
│
├── pret_client_personnel_Banque_corrected.py    # Application Streamlit
├── modele_random_forest.pkl                     # Modèle ML sauvegardé
├── requirements.txt                             # Dépendances Python
└── README.md                                     # Ce fichier
```
