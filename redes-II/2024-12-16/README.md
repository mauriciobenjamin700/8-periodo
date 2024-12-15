# Envio de emails entre containers usando PostFix

Para este caso, estaremos usando a imagem boky/postfix para criar o servidor

## Informações sobre boky/postfix

A imagem Docker do Postfix (nesse caso, `boky/postfix`) é usada para criar e configurar rapidamente um servidor de emails baseado no Postfix. Ela é popular para cenários em que você precisa de um SMTP relay ou um servidor de envio de emails dentro de um ambiente de contêineres.

### **Objetivo da Imagem `boky/postfix`**

1. **Servidor SMTP (Postfix)**:
   - A imagem fornece um servidor SMTP completo usando o Postfix.
   - Pode ser usado para enviar emails diretamente ou como relay para um servidor SMTP externo.

2. **Configuração Simples**:
   - A imagem simplifica a configuração do Postfix, permitindo ajustes rápidos por meio de variáveis de ambiente.

3. **Flexibilidade**:
   - Pode funcionar tanto como um relay (repassando emails para outro servidor) quanto como um servidor SMTP "autônomo".

4. **Uso Comum**:
   - Testes de envio de emails em ambientes de desenvolvimento.
   - Relay de mensagens de outras aplicações ou containers.

---

### **Principais Variáveis de Ambiente**
A imagem suporta diversas variáveis de ambiente para configurar o servidor. Aqui estão as mais importantes:

1. **Configuração Básica**:
   - `ALLOWED_NETWORKS`: Define as redes autorizadas a usar o servidor SMTP.
     - Exemplo: `0.0.0.0/0` permite acesso de qualquer rede.
   - `SMTP_SERVER_HOSTNAME`: Nome do servidor SMTP.
     - Exemplo: `postfix.mail.local`.

2. **Autenticação e Usuários**:
   - `SMTP_USER`: Cria um usuário no formato `username:password` para autenticação.
     - Exemplo: `user:password`.

3. **Domínios Permitidos**:
   - `ALLOWED_SENDER_DOMAINS`: Lista de domínios permitidos para envio de emails.
     - Exemplo: `example.com,anotherdomain.com`.
   - `ALLOW_EMPTY_SENDER_DOMAINS`: Define se remetentes de qualquer domínio podem enviar emails.
     - Exemplo: `true`.

4. **TLS e Segurança**:
   - `SMTP_TLS_SECURITY_LEVEL`: Configura o nível de segurança do TLS.
     - Valores: `may`, `encrypt`, `none`.
   - `TLS_CERT` e `TLS_KEY`: Certificados e chaves para TLS (se usados).

5. **Outras Configurações**:
   - `RELAY_HOST`: Define o servidor relay se o Postfix não for autônomo.
     - Exemplo: `smtp.gmail.com`.
   - `MESSAGE_SIZE_LIMIT`: Limite do tamanho da mensagem (em bytes).
     - Exemplo: `10485760` (10 MB).

---

### **Fluxo de Configuração Básica**
1. **Sem Relay**:
   - Define `ALLOWED_NETWORKS` para permitir acesso à rede.
   - Usa `ALLOW_EMPTY_SENDER_DOMAINS=true` para aceitar qualquer remetente.

2. **Com Relay**:
   - Define `RELAY_HOST` para um SMTP externo.
   - Usa `SMTP_USER` para autenticação no relay.

3. **TLS Opcional**:
   - TLS pode ser habilitado usando `SMTP_TLS_SECURITY_LEVEL=encrypt`.

---

### **Logs e Depuração**
Os logs do container são úteis para identificar problemas:
- Verifique as mensagens de erro relacionadas ao acesso, autenticação ou configuração de domínio.
- Use `docker logs postfix` para inspecionar o comportamento do Postfix no container.

---

Se precisar de mais ajuda com os problemas específicos da sua configuração, compartilhe os erros ou dificuldades que está enfrentando!

## Passos

### 1. **Criação do Docker Compose**

Crie um arquivo `docker-compose.yml` para orquestrar os três containers:

```yaml
version: '3.8'
services:
  sender:
    image: python:3.10
    container_name: sender
    volumes:
      - ./sender:/app
    working_dir: /app
    command: ["python", "send_email.py"]
    depends_on:
      - postfix

  postfix:
    image: catatnight/postfix
    container_name: postfix
    environment:
      - maildomain=mail.local
      - smtp_user=user:password
    ports:
      - "1025:25"

  receiver:
    image: python:3.10
    container_name: receiver
    volumes:
      - ./receiver:/app
    working_dir: /app
    command: ["python", "receive_email.py"]
```

---

### 2. **Configuração do Container Postfix**

O container Postfix (`catatnight/postfix`) já vem configurado para rodar um servidor SMTP simples. Ele aceita conexões de outros containers dentro da mesma rede Docker. 

- `maildomain=mail.local`: Define o domínio para o servidor SMTP.
- `smtp_user=user:password`: Configura um usuário e senha para autenticação.

---

### 3. **Criação do Código para o Sender**

Na pasta `./sender`, crie o arquivo `send_email.py`:

```python
import smtplib
from email.mime.text import MIMEText

# Configuração do e-mail
SMTP_SERVER = "postfix"  # Nome do serviço do container Postfix
SMTP_PORT = 25           # Porta SMTP padrão
SMTP_USER = "user"
SMTP_PASS = "password"

TO_EMAIL = "receiver@mail.local"
FROM_EMAIL = "sender@mail.local"
SUBJECT = "Teste de e-mail"
BODY = "Este é um e-mail enviado do Container 1 para o Container 3 através do Container 2."

# Enviar o e-mail
msg = MIMEText(BODY)
msg["Subject"] = SUBJECT
msg["From"] = FROM_EMAIL
msg["To"] = TO_EMAIL

try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
        print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")
```

---

### 4. **Criação do Código para o Receiver**

Na pasta `./receiver`, crie o arquivo `receive_email.py` para simular o recebimento de e-mails (usando logs ou um monitoramento básico):

```python
import time

def process_email():
    print("Aguardando e-mails...")
    # Simulação de processamento de e-mails recebidos
    while True:
        print("Verificando por novos e-mails... (simulado)")
        time.sleep(10)

if __name__ == "__main__":
    process_email()
```

---

### 5. **Iniciando o Sistema**
Execute o ambiente com:

```bash
docker-compose up --build
```

---

### 6. **Testando o Fluxo**

- O container `sender` enviará um e-mail para o container `receiver` através do servidor SMTP no container `postfix`.
- No console do container `receiver`, você verá logs simulando o recebimento de e-mails.

---

### 7. **Verificações e Depuração**
- **Monitorar Logs**: Verifique os logs do Postfix com:
  ```bash
  docker logs postfix
  ```
- **Testar Conexão SMTP**: Conecte-se ao Postfix a partir do container `sender` para testar:
  ```bash
  docker exec -it sender telnet postfix 25
  ```
- **Rede Docker**: Certifique-se de que todos os containers estão na mesma rede definida pelo Docker Compose.

Se precisar de mais ajustes ou tiver dúvidas, posso ajudar!

## Help

- [catatnight/postfix](https://hub.docker.com/r/catatnight/postfix)