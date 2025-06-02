from reportlab.pdfgen import canvas
import json
import base64

def lambda_handler(event, context):
    data = json.loads(event['body'])

    nome = data.get("nome", "Sem Nome")
    itens = data.get("itens", [])

    buffer = "/tmp/nota_fiscal.pdf"
    c = canvas.Canvas(buffer)
    c.drawString(100, 800, f"Cliente: {nome}")
    y = 750
    total = 0

    for item in itens:
        descricao = item.get("descricao", "")
        valor = item.get("valor", 0)
        c.drawString(100, y, f"{descricao}: R$ {valor}")
        y -= 20
        total += valor

    c.drawString(100, y - 20, f"Total: R$ {total}")
    c.save()

    with open(buffer, "rb") as f:
        pdf_bytes = f.read()

    pdf_base64 = base64.b64encode(pdf_bytes).decode("utf-8")

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"pdf_base64": pdf_base64})
    }
