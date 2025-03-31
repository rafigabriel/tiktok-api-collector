import requests
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
BASE_URL = "https://open-api.tiktok.com/"

def get_user_info():
    """
    Obtém informações públicas do usuário autenticado.
    """
    url = f"{BASE_URL}user/info/"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

    response = requests.get(url, headers=headers)
    return response.json()

def get_user_videos():
    """
    Obtém a lista de vídeos públicos do usuário autenticado.
    """
    url = f"{BASE_URL}video/list/"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

    response = requests.get(url, headers=headers)
    return response.json()
