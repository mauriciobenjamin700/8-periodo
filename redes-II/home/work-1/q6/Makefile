start:
	@echo "Starting the project"
	@docker compose up -d --build --remove-orphans


stop:
	@echo "Stopping all containers"
	@docker stop $(shell docker ps -q)

clean:
	@echo "Removing all containers and images"
	@docker rm -f $(shell docker ps -aq)
	@docker rmi -f $(shell docker images -q)

logs:
	@echo "Showing logs"
	@docker compose logs

run-sender:
	@echo "Running sender.py in a new container"
	@docker run --rm --name sender-q6 -v "$(pwd)":/app -w /app python:3.9-slim python sender.py

result-client:
	@docker logs sender-q6

result-server:
	@docker logs receiver-q6