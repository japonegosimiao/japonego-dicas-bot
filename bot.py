# Importando TODOS os nossos livros de mágica
import os
from dotenv import load_dotenv
import asyncio
import telegram
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

# O bot abre o cofre .env e lê TUDO
load_dotenv()

# Pegando TODAS as nossas credenciais do cofre
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
MEU_CHAT_ID = os.getenv("CHAT_ID")
WP_URL = "https://japonegodicas.com/xmlrpc.php"
WP_USER = os.getenv("WP_USER")
WP_PASSWORD = os.getenv("WP_PASSWORD")


# --- MÁGICA 1: A RECEITA PARA POSTAR NO WORDPRESS ---
def postar_no_wordpress():
    print("Iniciando a postagem no WordPress...")
    try:
        client = Client(WP_URL, WP_USER, WP_PASSWORD)
        
        post = WordPressPost()
        post.title = "Bot Adolescente: Teste de Fusão!"
        post.content = "Este post foi criado E notificado no Telegram pelo mesmo robô! A máquina está evoluindo! 🤖"
        post.post_status = 'publish'
        
        post_id = client.call(NewPost(post))
        
        print(f"Post criado com sucesso no WordPress! ID do post: {post_id}")
        return post_id # Devolve o ID do post para a gente usar depois
    except Exception as e:
        print(f"DEU RUIM! Erro ao postar no WordPress: {e}")
        return None # Devolve "Nada" se deu erro

# --- MÁGICA 2: A RECEITA PARA NOTIFICAR NO TELEGRAM ---
async def notificar_telegram(mensagem):
    print("Iniciando notificação no Telegram...")
    try:
        bot = telegram.Bot(token=TELEGRAM_TOKEN)
        await bot.send_message(chat_id=MEU_CHAT_ID, text=mensagem)
        print("Notificação enviada com sucesso no Telegram!")
    except Exception as e:
        print(f"DEU RUIM! Erro ao notificar no Telegram: {e}")

# --- O GRANDE CHEFE QUE ORQUESTRA TUDO ---
if __name__ == "__main__":
    # 1. O Chefe manda a Mágica 1 trabalhar
    novo_post_id = postar_no_wordpress()
    
    # 2. O Chefe verifica se a Mágica 1 teve sucesso
    if novo_post_id:
        # Se teve sucesso, o Chefe prepara a mensagem para a Mágica 2
        mensagem_telegram = f"NOVO POST NO SITE! 📢\n\nAcabei de publicar um novo post de teste! O ID dele é {novo_post_id}. A fusão foi um sucesso!"
        
        # 3. O Chefe manda a Mágica 2 trabalhar
        asyncio.run(notificar_telegram(mensagem_telegram))
    else:
        print("A publicação no site falhou. Portanto, nenhuma notificação foi enviada.")
        
    print("\n--- Processo de Fusão Finalizado ---")