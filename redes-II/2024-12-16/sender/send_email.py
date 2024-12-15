import smtplib

# Configuração do servidor SMTP
SMTP_HOST = 'postfix'  # Nome do container ou localhost se for no host
SMTP_PORT = 1026  # Porta configurada no Docker Compose
SMTP_USER = 'user'
SMTP_PASSWORD = 'password'

# Configuração do email
FROM_EMAIL = 'user@example.com'
TO_EMAIL = 'destinatario@example.com'
MESSAGE = """\
Subject: Teste de Email
Olá, este é um email de teste enviado pelo servidor Postfix.
"""

try:
    # Conectar ao servidor SMTP
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        print("Entrei no WITH")
        server.starttls()  # Se TLS for configurado
        server.login(SMTP_USER, SMTP_PASSWORD)
        print("Conectado ao servidor SMTP...")
        server.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
        print("Email enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar email: {e}")
