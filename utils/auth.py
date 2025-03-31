import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_KEY = os.getenv("CLIENT_KEY")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

AUTH_URL = "https://www.tiktok.com/auth/authorize/"
TOKEN_URL = "https://open-api.tiktok.com/oauth/access_token/"

def get_auth_url():
    """
    Gera a URL de autenticação para o usuário conceder permissões ao app.
    """
    return f"{AUTH_URL}?client_key={CLIENT_KEY}&response_type=code&scope=user.info.basic,user.video.list&redirect_uri={REDIRECT_URI}&state=random_state"

def get_access_token(auth_code):
    """
    Troca o código de autorização pelo token de acesso.
    """
    payload = {
        "client_key": CLIENT_KEY,
        "client_secret": CLIENT_SECRET,
        "code": auth_code,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI
    }

    
    
    response = requests.post(TOKEN_URL, json=payload)
    data = response.json()

    print("Response Status:", response.status_code)
    print("Response JSON:", response.json())
    
    if "data" in data and "access_token" in data["data"]:
        return data["data"]["access_token"]
    
    return None
