# Import des bibliothèques
import streamlit as st
import pandas as pd
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

#Données des utilisateurs
df_users = pd.read_csv('donnees_utilisateurs - Feuille 1.csv', sep=",")
df_users = df_users.set_index('name') # Definis name comme index, pour ensuite transformer le df en dictionnaire adapté pour authenticator
dict_users = df_users.to_dict(orient= 'index') # Crée un dictionnaire 
donnees_des_comptes = {"usernames" : dict_users} # Je crée le dict imbriqué adapté à Authenticator
authenticator = Authenticate(donnees_des_comptes,
                             "cookie name",
                             "cookie key",
                             30)
# Afficher le formulaire de connexion
authenticator.login()

# Affichage du contenu en focntion des conditions
if st.session_state["authentication_status"]:
    with st.sidebar : 
        st.title(f"Bienvenue sur votre session !")
        authenticator.logout("Déconnexion")

        # Création du menu qui va afficher les choix dans la sidebar
        selection = option_menu(
                    menu_title= f"Que souhaitez vous explorer aujourd'hui ?",
                    options = ["Accueil", "Album photos du chat"])
    # Affichage en focntion du choix de l'utilisateurs dans le menu
    if selection == "Accueil":
        st.title("Bienvenue sur la page d'accueil")
        st.image("https://matouchic.com/wp-content/uploads/2025/10/Votre-relation-au-chat.-jadore-les-chats.-mais-chez-les-autres.-Cest-moins-de-resp.png")
    elif selection == "Album photos du chat":
        st.title("Bienvenue dans l'album photos du chat !")
        # Création des 3 colonnes pour les images de chat
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://www.agria.fr/imagevault/publishedmedia/yvuhg1sunwp0mcp4jfvj/Orange_cat_laying_indoor.jpg")
            st.image("https://media.istockphoto.com/id/509911366/fr/photo/dr%C3%B4le-chat-rire.jpg?s=612x612&w=0&k=20&c=P3N21UroqM94KkR_hQyfL8uQssIj1uqIz_ESyBEFM90=")
        with col2:
            st.image("https://postersdenosregions.fr/cdn/shop/files/Chat_Chaton_Mignon_Tout_est_sous_controle_Affiche_Poster_Ski_Drole_Humour_Humoristique.jpg?v=1726953899&width=480")
        with col3:
            st.image("https://img.freepik.com/photos-premium/chat-drole-lunettes-soleil-chat-lunettes-mur-ensoleille-propre-bleu-clair-animaux-droles-fete-vacances-voyage-concept-ete_90380-2622.jpg?semt=ais_hybrid&w=740&q=80")
            st.image("https://img.freepik.com/photos-gratuite/portrait-gros-plan-beau-chat_23-2149214419.jpg?semt=ais_hybrid&w=740&q=80")

elif st.session_state["authentication_status"] is False:
    st.error("Le nom de l'utiliateur ou le mot de passe sont incorrect")
elif st.session_state["authentication_status"] is None : 
    st.warning("Les champs nom d'utilisateur et mot de passe doivent être remplis")



