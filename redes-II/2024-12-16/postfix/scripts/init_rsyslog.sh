#!/bin/bash

# Criar diretórios de log, se não existirem
mkdir -p /var/log
chmod 0775 /var/log

# Corrigir permissões no arquivo de configuração
chmod 0644 /etc/rsyslog.conf

# Iniciar o rsyslog
rsyslogd -n
