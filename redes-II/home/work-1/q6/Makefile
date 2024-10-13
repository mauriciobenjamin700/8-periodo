start:
	@echo "Starting the project"
	@docker compose up -d --build --remove-orphans


stop:
	@echo "Stopping all containers"
	@docker stop $(shell docker ps -q)

clean:
	@echo "Removing all containers, images, and volumes"
	@docker rm -f $(shell docker ps -aq)
	@docker rmi -f $(shell docker images -q)
	@docker volume rm $(shell docker volume ls -q)

logs:
	@echo "Showing logs"
	@docker compose logs

result-client:
	@docker logs sender-q6

result-server:
	@docker logs receiver-q6