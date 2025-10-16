import os
import requests
from dotenv import load_dotenv

# Caminho absoluto do arquivo .env
dotenv_path = r"C:\Users\lucas\Desktop\japonego-dicas-bot\.env"
load_dotenv(dotenv_path)

WORDPRESS_URL =   # Coloque seu domínio aqui
WORDPRESS_USER =                      # Seu usuário admin
WORDPRESS_APP_PASSWORD =  # Senha de aplicativo

print("WORDPRESS_URL:", WORDPRESS_URL)
print("WORDPRESS_USER:", WORDPRESS_USER)
print("WORDPRESS_APP_PASSWORD:", WORDPRESS_APP_PASSWORD)

api_url = f"{WORDPRESS_URL}/wp-json/wp/v2/posts"

# Dados do post de teste
post_data = {
    "title": "🚀 Post de teste do bot",
    "content": "Se você está vendo isso no WordPress, a integração funcionou ✅",
    "status": "publish"
}

# Faz a requisição autenticada
response = requests.post(
    api_url,
    auth=(WORDPRESS_USER, WORDPRESS_APP_PASSWORD),
    json=post_data
)

if response.status_code == 201:
    print("✅ Post criado com sucesso no WordPress!")
    print("📎 Link:", response.json().get("link"))
else:
    print(f"❌ Erro ao criar post no WordPress: {response.status_code}")
    print(response.text)
