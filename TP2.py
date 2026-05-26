# TP2 - Application Streamlit
# Laure de Baynast de Septfontaines

# Objectif : Visualiser des données CSV en 2D ou 3D
# Lien de la page :

# Question 3 : cahrgement des librairies
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px


#Titres
st.title("TP2 Application")
st.subheader("Laure de Baynast")
 
# Question 4 : demander le nom de l'utilisateur et le saluer
nom = st.text_input("Entrez votre nom")
if nom:
    st.success(f"Bonjour, {nom}!")

# Question 5 : chargement de fichier
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")
df = pd.read_csv(uploaded_file)
st.dataframe(df.head())

# Question 6 : selectbox pour que l'utilisateur puisse choisir entre 2D et 3D
st.subheader("Choix du mode de visualisation : 2D ou 3D")
mode = st.selectbox("Choisir le type de graphique :",options=["2D", "3D"], index=0)  

# Question 7 : liste des colonnes numériques 
colonnes = df.select_dtypes(include="number").columns.tolist()
 
# Question 8 : choix 2D -> selection de 2 colonnes et affichage du graph
if mode == "2D":
    st.subheader("Graph 2D")
    colonne_x = st.selectbox("Colonne X :", colonnes)
    colonne_y = st.selectbox("Colonne Y :", colonnes)
    st.line_chart(data=df, x=col_x, y=col_y)

