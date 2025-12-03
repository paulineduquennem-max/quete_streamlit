# Import des bibliothèque
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Variables qui stockent les Dataframe
df_flights = sns.load_dataset('flights')
df_tips = sns.load_dataset('tips')
df_iris = sns.load_dataset('iris')

# Variables qui stockent les colonnes sous formes de liste pour chaque df
list_col_flight = df_flights.columns.to_list()
list_col_tips = df_tips.columns.to_list()
list_col_iris = df_iris.columns.to_list()

# Titre principal de l'application
st.title("Manipulation de données et création de graphiques")

# Sélection des datasets
select_dataset = st.selectbox("Quel dataset veux-tu utiliser ?",
             ['flights', 'tips', 'iris'])

# Conditions pour afficher le dataframe du dataset sélectionner par l'utilisateur
if select_dataset == 'flights':
    df = df_flights
elif select_dataset == 'tips' :
    df = df_tips
else : 
    df = df_iris

# Afficher le datframe sous forme de tableau propre dans streamlit
st.dataframe(df)

# Sélection des colonnes comme axe X
if select_dataset == 'flights' :
    x = st.selectbox("Choisissez la colonne X :",
                             list_col_flight)
elif select_dataset == 'tips' :
    x = st.selectbox("Choisissez la colonne X :",
                             list_col_tips)
else :
    x = st.selectbox("Choisissez la colonne X :",
                             list_col_iris)

# Sélection des colonnes comme axe Y
if select_dataset == 'flights' :
    y = st.selectbox("Choisissez la colonne Y :",
                             list_col_flight)
elif select_dataset == 'tips' :
    y = st.selectbox("Choisissez la colonne Y :",
                             list_col_tips)
else :
    y = st.selectbox("Choisissez la colonne Y :",
                             list_col_iris)

# Sélection des graphiques
select_graph = st.selectbox("Quel graphique veux-tu utiliser ?", 
                            ["scatter_chart","line_chart", "bar_chart"])

# Conditions qui détermine les graphes
if select_graph == "bar_chart":
    sns.barplot(df, x= x, y= y) # Crée un graphique barplot
    st.pyplot(plt.gcf())
elif select_graph == "scatter_chart":
    sns.scatterplot(df, x= x, y= y) # Crée un graphique scatterplot
    st.pyplot(plt.gcf())
elif select_graph == "line_chart":
    sns.lineplot(df, x= x, y= y) # Crée un graphique lineplot
    st.pyplot(plt.gcf())

# Affichage de la case à cocher pour afficher la matrice de corrélation
coche = st.checkbox(label = "Afficher la matrice de corrélation")

# Calcul de la corrélation pour la matrice
corr= df.corr(numeric_only = True)

# Affichage de la matrice
if coche == True:
    sns.heatmap(corr, vmin = -1, vmax= 1, annot= True, cmap= "Spectral")
    st.pyplot(plt.gcf())
