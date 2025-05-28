from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)
CORS(app)

@app.route('/agendar', methods=['POST'])
def agendar():
    data = request.get_json()
    nome = data.get("nome")
    email_cliente = data.get("emailCliente")
    horario = data.get("horario")

    corpo = f"Novo agendamento:\n\nNome: {nome}\nE-mail: {email_cliente}\nHorário: {horario}"

    remetente = "jotaprxdx19@gmail.com"
    senha = "tnog asiu tekm jdkg"  # Use senha de app do Gmail
    destinatario = "flawlexx00@gmail.com"

    msg = MIMEText(corpo)
    msg["Subject"] = "Novo Agendamento"
    msg["From"] = remetente
    msg["To"] = destinatario

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg.as_string())
        server.quit()
        return jsonify({"mensagem": "E-mail enviado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
