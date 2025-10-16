import os
from dotenv import load_dotenv
from telegram import Bot
import asyncio
import requests
from requests.auth import HTTPBasicAuth

# ------------------------------
# Carrega variáveis do .env
# ------------------------------
load_dotenv()

# --- Telegram ---
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# --- WordPress ---
WP_URL = os.getenv("WP_URL")
WP_USER = os.getenv("WP_USER")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")

# --- Affiliates (exemplo, se precisar no futuro) ---
AMAZON_TAG = os.getenv("AMAZON_TAG")
SHOPEE_AFF_ID = os.getenv("SHOPEE_AFF_ID")

# ------------------------------
# Função assíncrona para enviar mensagem no Telegram
# ------------------------------
bot = Bot(token=TELEGRAM_TOKEN)

async def main_telegram():
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("❌ Token ou Chat ID do Telegram não configurados corretamente no .env")
        return
    try:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="🚀 Bot funcionando no Telegram!")
        print("✅ Mensagem enviada com sucesso no Telegram!")
    except Exception as e:
        print(f"❌ Erro ao enviar mensagem no Telegram: {e}")

# ------------------------------
# Função para criar post de teste no WordPress
# ------------------------------
def post_wordpress():
    if not WP_URL or not WP_USER or not WP_APP_PASSWORD:
        print("❌ WordPress não configurado corretamente no .env")
        return
    try:
        post = {
            "title": "Post de Teste do Bot",
            "content": "Este post foi criado automaticamente pelo bot_bebe.py",
            "status": "draft"  # rascunho, para não publicar direto
        }
        response = requests.post(
            f"{WP_URL}/wp-json/wp/v2/posts",
            json=post,
            auth=HTTPBasicAuth(WP_USER, WP_APP_PASSWORD)
        )
        if response.status_code in [200, 201]:
            print("✅ Post de teste criado com sucesso no WordPress!")
        else:
            print(f"❌ Erro ao criar post no WordPress: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Erro na integração com WordPress: {e}")

# ------------------------------
# Executa os testes
# ------------------------------
if __name__ == "__main__":
    asyncio.run(main_telegram())
    # Descomente a linha abaixo depois de garantir permissões no WP
    # post_wordpress()
