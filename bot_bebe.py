# Importando todas as nossas ferramentas mágicas
import telegram
import asyncio
import os
from dotenv import load_dotenv

# O bot abre o cofre .env e lê TUDO o que está guardado lá
load_dotenv()

# O bot pega cada segredo pelo nome, sem nunca ver o conteúdo
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
MEU_CHAT_ID = os.getenv("CHAT_ID")
WP_USER = os.getenv("WP_USER")
WP_PASSWORD = os.getenv("WP_PASSWORD")

MENSAGEM = "Teste de segurança finalizado! Todas as minhas senhas estão seguras no cofre. ✅"

# O resto do código continua o mesmo
async def enviar_mensagem():
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    await bot.send_message(chat_id=MEU_CHAT_ID, text=MENSAGEM)
    print("Mensagem 100% segura enviada com sucesso!")
    print(f"Pronto para conectar ao WordPress como o usuário: {WP_USER}")

if __name__ == "__main__":
    print("Iniciando o bot em modo de segurança total...")
    asyncio.run(enviar_mensagem())
    print("Trabalho finalizado.")