from aiosmtpd.controller import Controller


class CustomSMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        mailfrom = envelope.mail_from
        rcpttos = envelope.rcpt_tos
        data = envelope.content.decode('utf-8', errors='replace')

        print("\n--- Novo e-mail recebido ---")
        print(f"De: {mailfrom}")
        print(f"Para: {', '.join(rcpttos)}")
        print("\nConteúdo do e-mail:")
        print(data)
        print("--- Fim do e-mail ---\n")

        return '250 Mensagem aceita para entrega'

if __name__ == "__main__":
    handler = CustomSMTPHandler()
    controller = Controller(handler, hostname='0.0.0.0', port=1025)

    print("Servidor SMTP do Receiver rodando na porta 1025...")
    try:
        controller.start()
        while True:
            pass  # Mantém o servidor rodando
    except KeyboardInterrupt:
        print("Encerrando o servidor...")
    finally:
        controller.stop()