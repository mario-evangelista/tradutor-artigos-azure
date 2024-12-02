# **Tradutor de Artigos Técnicos com Azure AI**

![Azure](https://img.shields.io/badge/Azure-Translator-blue)  
![Python](https://img.shields.io/badge/Python-3.x-blue)  
![License](https://img.shields.io/badge/license-MIT-green)

## **Descrição**
Este projeto utiliza a **Azure Translator API**, parte do Azure Cognitive Services, para traduzir artigos técnicos automaticamente para diversos idiomas. Ele é ideal para profissionais e empresas que precisam traduzir documentos técnicos de forma precisa e eficiente.

---

## **Funcionalidades**
- Tradução de textos em vários idiomas.
- Suporte para arquivos de texto, DOCX e PDFs.
- Fácil integração e personalização.
- Utiliza o serviço de tradução em tempo real do Azure.

---

## **Tecnologias Utilizadas**
- **Azure Cognitive Services** (Translator API)
- **Python 3.x**
- Bibliotecas:
  - `requests` (requisições HTTP)
  - `python-docx` (manipulação de arquivos DOCX)
  - `PyPDF2` (manipulação de PDFs)

---

## **Requisitos**
- Python 3.8 ou superior.
- Conta no Azure com a **Translator API** configurada.
- Dependências do projeto (instaladas via `pip`).

---

## **Instalação**

1. Clone o repositório:
   ```bash
   git clone https://github.com/mario-evangelista/tradutor-artigos-azure.git
   cd tradutor-artigos-azure
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis da API:
   - Edite o arquivo `.env` (exemplo fornecido no repositório):
     ```
     AZURE_API_KEY=SUA_CHAVE_AZURE
     AZURE_ENDPOINT=SEU_ENDPOINT
     AZURE_REGION=SUA_REGIAO
     ```

---

## **Como Usar**

### Tradução de Texto Simples
Edite o arquivo `main.py` e insira o texto a ser traduzido:
```python
artigo = "Seu texto técnico aqui."
idioma_destino = "en"  # Exemplo: traduzir para inglês
```
Execute o script:
```bash
python main.py
```

### Tradução de Arquivos DOCX ou PDF
Para traduzir documentos:
1. Coloque o arquivo na pasta `docs/`.
2. Edite o script para apontar para o arquivo desejado.
3. Execute o script:
   ```bash
   python translate_docx.py
   ```

---

## **Contribuição**
Contribuições são bem-vindas! Sinta-se à vontade para abrir *issues* ou enviar *pull requests*.

---

## **Licença**
Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.

---

## **Contato**
Criado por **Mário Evangelista**  
- LinkedIn: https://www.linkedin.com/in/marioevangelista/ 
- Email: mariojbe@gmail.com
