import asyncio
from playwright.async_api import async_playwright

URL_OFERTAS = "https://www.amazon.com.br/ofertas"

async def cacar_ofertas_completas_da_amazon():
    print("Iniciando o caçador da Amazon (com mira completa)...")
    
    async with async_playwright() as p:
        navegador = await p.chromium.launch(headless=True)
        pagina = await navegador.new_page()
        
        print(f"Navegando para: {URL_OFERTAS}")
        await pagina.goto(URL_OFERTAS, wait_until="domcontentloaded", timeout=60000)
        
        card_selector = "div[data-testid='product-card']"
        await pagina.wait_for_selector(card_selector, timeout=30000)
        print("Ofertas detectadas! Iniciando a extração completa de dados...")
        
        cards_de_produto = await pagina.query_selector_all(card_selector)
        
        print(f"Encontrados {len(cards_de_produto)} produtos na página!")
        
        for card in cards_de_produto:
            try:
                # --- CAÇANDO O TÍTULO ---
                titulo_elemento = await card.query_selector("span.a-truncate-cut")
                titulo = await titulo_elemento.inner_text() if titulo_elemento else "Título não encontrado"

                # --- CAÇANDO O LINK ---
                link_elemento = await card.query_selector("a[data-testid='product-card-link']")
                link_parcial = await link_elemento.get_attribute('href') if link_elemento else ""
                link_completo = link_parcial if link_parcial.startswith('http') else f"https://www.amazon.com.br{link_parcial}"

                # --- CAÇANDO O PREÇO ---
                preco_inteiro_el = await card.query_selector("span.a-price-whole")
                preco_fracao_el = await card.query_selector("span.a-price-fraction")
                
                preco = "Preço não encontrado"
                if preco_inteiro_el and preco_fracao_el:
                    preco_inteiro = await preco_inteiro_el.inner_text()
                    preco_fracao = await preco_fracao_el.inner_text()
                    preco = f"R$ {preco_inteiro}{preco_fracao}"

                # --- CAÇANDO A IMAGEM ---
                imagem_elemento = await card.query_selector("img.ProductCardImage-module__image_SU6C7KYJpko3vQ2fK7Kf")
                url_imagem = await imagem_elemento.get_attribute('src') if imagem_elemento else "Imagem não encontrada"

                
                print("\n--- OFERTA COMPLETA ENCONTRADA ---")
                print(f"Título: {titulo.strip()}")
                print(f"Preço: {preco}")
                print(f"Link: {link_completo}")
                print(f"Imagem: {url_imagem}")

            except Exception as e:
                print(f"Erro ao processar um card: {e}")

        await navegador.close()

if __name__ == "__main__":
    asyncio.run(cacar_ofertas_completas_da_amazon())