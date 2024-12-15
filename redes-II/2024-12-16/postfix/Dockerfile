FROM debian:latest

# Instalar dependências
RUN apt-get update && apt-get install -y postfix rsyslog supervisor

# Configurar rsyslog
COPY rsyslog.conf /etc/rsyslog.conf
RUN chmod 0644 /etc/rsyslog.conf

# Configurações padrão do Postfix
ENV ALLOWED_NETWORKS=0.0.0.0/0 \
    SMTP_SERVER_HOSTNAME=postfix.mail.local \
    SMTP_USER=user:password \
    ALLOW_EMPTY_SENDER_DOMAINS=true

# Copiar configurações customizadas (se necessário)
COPY supervisord.conf /etc/supervisor/supervisord.conf
COPY main.cf /etc/postfix/main.cf
COPY sasl_passwd /etc/postfix/sasl_passwd
RUN chmod 600 /etc/postfix/sasl_passwd

# Porta para SMTP
EXPOSE 25

# Iniciar o supervisord
CMD ["/bin/bash", "-c", "rm -f /run/rsyslogd.pid && supervisord -c /etc/supervisor/supervisord.conf"]