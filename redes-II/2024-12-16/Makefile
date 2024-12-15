start:
	@docker compose up --build

run: 
	@docker compose up

logs:
	@docker compose logs -f

stop:
	@docker compose down

receiver:
	@docker compose exec receiver cat /app/emails.txt

send:
	@docker compose up sender

check-port:
	@telnet localhost ${port}