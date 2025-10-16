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

# --- Exemplo de afiliados ---
AMAZON_TAG = os.getenv("AMAZON_TAG")
SHOPEE_AFF_ID = os.getenv("SHOPEE_AFF_ID")

# ------------------------------
# Função assíncrona para enviar mensagem no Telegram
# ------------------------------
bot = Bot(token=TELEGRAM_TOKEN)

async def enviar_telegram(text):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("❌ Token ou Chat ID do Telegram não configurados corretamente no .env")
        return
    try:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=text)
        print("✅ Mensagem enviada com sucesso no Telegram!")
    except Exception as e:
        print(f"❌ Erro ao enviar mensagem no Telegram: {e}")

# ------------------------------
# Função para criar post no WordPress
# ------------------------------
def criar_post_wordpress(title, content, status="draft"):
    if not WP_URL or not WP_USER or not WP_APP_PASSWORD:
        print("❌ WordPress não configurado corretamente no .env")
        return
    try:
        post_data = {
            "title": title,
            "content": content,
            "status": status
        }
        response = requests.post(
            f"{WP_URL}/wp-json/wp/v2/posts",
            json=post_data,
            auth=HTTPBasicAuth(WP_USER, WP_APP_PASSWORD)
        )
        if response.status_code in [200, 201]:
            print(f"✅ Post criado com sucesso no WordPress!\n📎 Link: {response.json().get('link')}")
        else:
            print(f"❌ Erro ao criar post no WordPress: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Erro na integração com WordPress: {e}")

# ------------------------------
# Executa testes
# ------------------------------
if __name__ == "__main__":
    texto_telegram = "🚀 Bot funcionando! Teste de mensagem no Telegram e WP."
    asyncio.run(enviar_telegram(texto_telegram))

    # Descomente para criar post de teste no WordPress
    criar_post_wordpress(
        title="Post de Teste do Bot",
        content="Este post foi criado automaticamente pelo bot."
    )
