# Função Lambda – Gerador de PDF

Esta função AWS Lambda recebe um JSON com informações de um cliente e seus produtos, gera um PDF com esses dados e retorna o conteúdo do PDF em **Base64**.

---

## Como Testar a Função

### 1 Enviando a Requisição

Use o **Postman** (ou qualquer outro cliente HTTP) para fazer um **POST** para a URL da função Lambda:

** URL da função Lambda:**
```
https://jkbdouhtmsipekvi3fdwoytvvi0wkcmw.lambda-url.us-east-2.on.aws/
```

** Exemplo de configuração no Postman:**
[![Configuração Postman](https://prnt.sc/gHt1K-CNcw-i)](https://prnt.sc/gHt1K-CNcw-i)

**Configuração da requisição:**

- Método: `POST`
- Aba **Body**:
  - Selecione a opção `raw`
  - Escolha o tipo `JSON` (ícone à direita)
  - Cole e edite o seguinte JSON conforme necessário:

```json
{
  "nome": "Teste",
  "itens": [
    { "descricao": "PlayStation 5", "valor": 4700 },
    { "descricao": "Controle DualSense", "valor": 540 }
  ]
}
```

---

### 2 Decodificando o PDF

Após enviar a requisição, a resposta trará um objeto JSON com um campo `pdf_base64`.

**Exemplo de resposta:**
```json
{
  "pdf_base64": "JVBERi0xLjcKJcfs..."
}
```

Copie **todo o conteúdo** entre aspas (`"`) e acesse o site abaixo para converter esse código em um arquivo PDF.

** Site para conversão:**
[https://base64.guru/converter/decode/pdf](https://base64.guru/converter/decode/pdf)

- Cole o conteúdo no campo em branco.
- Clique em **"Decode Base64 to PDF"**.
- Baixe ou visualize o PDF gerado.

** Exemplo do site:**
[![Exemplo site](https://prnt.sc/nD_3LRRLyDBZ)](https://prnt.sc/nD_3LRRLyDBZ)

---

## i Observações

- **⚠️ Atenção:** Certifique-se de copiar **apenas** o valor de `pdf_base64`, sem aspas nem chaves.
- O conteúdo PDF é gerado dinamicamente com base nos dados enviados via JSON.
- A função está hospedada na AWS com uma URL pública para testes temporários.
