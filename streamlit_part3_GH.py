import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
from pathlib import Path


accounts= {'usernames': {}}
BASE_DIR = Path(__file__).resolve().parent
df_accounts = pd.read_csv(BASE_DIR / "accounts.csv")
for index, row in df_accounts.iterrows():
    username= row['name']
    accounts['usernames'][username]= row.to_dict()

authenticator = Authenticate(
    accounts,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

authenticator.login()

def accueil():
    st.header("Bienvenue sur ma page", text_alignment= 'center')
    st.image('https://www.delcampe.net/static/img_large/auction/001/924/435/545_001.jpg', use_container_width=True)

def page_chat():
    st.header("Bienvenue dans l'album de mon chat", text_alignment= 'center')
    col1, col2, col3= st.columns(3)
    with col1:
        st.image('https://png.pngtree.com/png-clipart/20250122/original/pngtree-funny-cat-in-suit-cartoon-animal-illustration-png-image_20118607.png', use_container_width=True)
    with col2:
        st.image('https://img4.dhresource.com/webp/m/0x0/f3/albu/km/j/31/332813c0-3157-4f9f-bdd5-bf5cf301be75.jpg')
    with col3:
        st.image('https://i.redd.it/kujjtj1dy29c1.jpeg')
if st.session_state["authentication_status"]:
    with st.sidebar:
        authenticator.logout("Déconnexion")
        st.text(f'Bienvenue {st.session_state["name"]}')
        selection= option_menu(
            menu_title= None,
            options= ['🤩 Accueil','🐱 Les photos de mon chat']
        ) 
    if selection== '🤩 Accueil':
        accueil()
    elif selection== '🐱 Les photos de mon chat':
        page_chat()

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
