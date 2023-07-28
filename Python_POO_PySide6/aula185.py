# Enviando e-mails com o python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from string import Template
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Caminho arquivo HTML
CAMINHO_HTML = Path(__file__).parent / 'aula185.html'

# dados do remetente e detinatário

remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

# configuraões SMTP

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smptp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem de texto
with CAMINHO_HTML.open('r') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='João')

# Transformar nossa mensagem em MIMEMultipart

mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Assunto do e-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smptp_username, smtp_password)
    server.send_message(mime_multipart)
    print('Email enviado com sucesso!')
