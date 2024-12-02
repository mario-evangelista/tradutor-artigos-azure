import requests

# Configurações da API
key = "SUA_CHAVE_AZURE"
endpoint = "SEU_ENDPOINT_AZURE"
region = "REGIAO_DO_RECURSO"  # Exemplo: "brazilsouth"

# Função de Tradução
def traduzir_texto(texto, idioma_destino):
    url = f"{endpoint}/translate?api-version=3.0&to={idioma_destino}"
    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Ocp-Apim-Subscription-Region": region,
        "Content-Type": "application/json"
    }
    body = [{"text": texto}]
    
    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        traducoes = response.json()
        return traducoes[0]["translations"][0]["text"]
    else:
        return f"Erro: {response.status_code} - {response.text}"

# Exemplo de Uso
artigo_original = """
Azure AI é uma plataforma poderosa para desenvolvimento de soluções baseadas em inteligência artificial.
"""
idioma_para_traduzir = "en"  # Código ISO para inglês
traducao = traduzir_texto(artigo_original, idioma_para_traduzir)
print("Tradução:", traducao)
