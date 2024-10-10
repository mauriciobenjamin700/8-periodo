start:
	@echo "Starting the project"
	@docker compose up --build --remove-orphans


stop-all:
	@echo "Stopping all containers"
	@docker stop $(shell docker ps -q)

clean:
	@echo "Removing all containers and images"
	@docker rm -f $(shell docker ps -aq)
	@docker rmi -f $(shell docker images -q)