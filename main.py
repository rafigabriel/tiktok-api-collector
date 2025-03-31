from utils.auth import get_auth_url, get_access_token
from utils.api_calls import get_user_info, get_user_videos
import json

def main():
    print("=== TikTok Scraper ===")
    
    # Se precisar autenticar, gere a URL para login
    auth_url = get_auth_url()
    print(f"Acesse esta URL para autorizar o app: {auth_url}")
    
    auth_code = input("Insira o código de autorização gerado pelo TikTok: ")
    token = get_access_token(auth_code)
    
    if token:
        print(f"Token de acesso obtido: {token}")
    
    # Obtendo dados do usuário
    user_info = get_user_info()
    print("\n[INFO USUÁRIO]:", json.dumps(user_info, indent=4))
    
    # Obtendo vídeos do usuário
    user_videos = get_user_videos()
    print("\n[LISTA DE VÍDEOS]:", json.dumps(user_videos, indent=4))

if __name__ == "__main__":
    main()
