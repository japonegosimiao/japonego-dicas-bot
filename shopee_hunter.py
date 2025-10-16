import asyncio
from playwright.async_api import async_playwright

# O endereço do nosso "terreno de caça"
URL_SHOPEE = "https://shopee.com.br/ofertas-relampago"

async def visitar_shopee_como_humano():
    print("Iniciando o caçador da Shopee (em modo 'humano')...")
    
    async with async_playwright() as p:
        navegador = await p.chromium.launch(headless=True)
        contexto = await navegador.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            viewport={'width': 1920, 'height': 1080}
        )
        pagina = await contexto.new_page()
        
        print(f"Navegando para: {URL_SHOPEE}")
        
        try:
            await pagina.goto(URL_SHOPEE, wait_until="domcontentloaded", timeout=60000)
            print("Página carregada. Procurando pelo botão de cookies...")

            # --- A MÁGICA DE HOJE ---
            # 1. Definimos o "endereço" do botão de aceitar cookies
            cookie_button_selector = "button.shopee-button-solid.shopee-button-solid--primary"
            
            # 2. Esperamos o botão aparecer (damos até 10 segundos)
            await pagina.wait_for_selector(cookie_button_selector, timeout=10000)
            
            # 3. Clicamos no botão
            await pagina.click(cookie_button_selector)
            print("Botão de cookies encontrado e clicado!")
            
            # 4. Damos um tempinho para a página recarregar após o clique
            await pagina.wait_for_timeout(3000) # espera 3 segundos

            # 5. Agora sim, pegamos o título da página REAL
            titulo_da_pagina = await pagina.title()
            
            print("\n--- RESULTADO ---")
            print(f"O título da página real é: '{titulo_da_pagina}'")
            
            # Bônus: Vamos tirar um novo screenshot para provar a vitória
            await pagina.screenshot(path="screenshot_shopee_vitoria.png")
            print("Screenshot 'screenshot_shopee_vitoria.png' salvo!")

        except Exception as e:
            print(f"\nDEU RUIM! Ocorreu um erro: {e}")
            await pagina.screenshot(path="screenshot_shopee_erro.png")
            print("Screenshot de erro salvo.")

        finally:
            await navegador.close()
            print("Navegador fechado.")


if __name__ == "__main__":
    asyncio.run(visitar_shopee_como_humano())   






