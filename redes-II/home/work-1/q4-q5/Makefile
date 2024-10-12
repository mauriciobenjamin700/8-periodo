start:
	@echo "Starting the project"
	@docker compose up -d --build --remove-orphans

run-server:
	@echo "Running server"
	@docker compose up -d receiver

run-sender:
	@echo "Running sender"
	@docker compose run sender

show-results:
	@echo "Showing results"
	@docker logs receiver

stop-all:
	@echo "Stopping all containers"
	@docker stop $(shell docker ps -q)

clean:
	@echo "Removing all containers and images"
	@docker rm -f $(shell docker ps -aq)
	@docker rmi -f $(shell docker images -q)