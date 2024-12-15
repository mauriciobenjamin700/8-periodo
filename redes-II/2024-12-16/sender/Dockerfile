FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . /app

# Instala a biblioteca necessária
RUN pip install --no-cache-dir aiosmtpd

# Define o comando de execução
CMD ["python", "send_email.py"]
