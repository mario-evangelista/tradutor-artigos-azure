import os
from translate_docx import traduzir_arquivo_docx
import requests

# Configurações da API do Azure
AZURE_API_KEY = os.getenv("AZURE_API_KEY", "SUA_CHAVE_AZURE")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT", "SEU_ENDPOINT")
AZURE_REGION = os.getenv("AZURE_REGION", "SUA_REGIAO")

# Função para traduzir texto simples
def traduzir_texto(texto, idioma_destino):
    url = f"{AZURE_ENDPOINT}/translate?api-version=3.0&to={idioma_destino}"
    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_API_KEY,
        "Ocp-Apim-Subscription-Region": AZURE_REGION,
        "Content-Type": "application/json",
    }
    body = [{"text": texto}]
    
    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        traducoes = response.json()
        return traducoes[0]["translations"][0]["text"]
    else:
        raise Exception(f"Erro: {response.status_code} - {response.text}")

# Função principal
def main():
    print("Selecione uma opção:")
    print("1. Traduzir texto simples")
    print("2. Traduzir arquivo DOCX")
    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        texto = input("Digite o texto que deseja traduzir: ")
        idioma_destino = input("Digite o idioma de destino (ex: 'en' para inglês): ")
        try:
            traducao = traduzir_texto(texto, idioma_destino)
            print("\nTexto traduzido:")
            print(traducao)
        except Exception as e:
            print(f"Erro ao traduzir texto: {e}")

    elif opcao == "2":
        caminho_entrada = input("Digite o caminho do arquivo DOCX de entrada: ")
        caminho_saida = input("Digite o caminho do arquivo DOCX de saída: ")
        idioma_destino = input("Digite o idioma de destino (ex: 'en' para inglês): ")
        try:
            traduzir_arquivo_docx(caminho_entrada, caminho_saida, idioma_destino)
        except Exception as e:
            print(f"Erro ao traduzir arquivo: {e}")
    else:
        print("Opção inválida. Saindo do programa.")

# Ponto de entrada
if __name__ == "__main__":
    main()
