build:
	docker-compose -f docker-compose.yml build
up:
	docker-compose -f docker-compose.yml up
down:
	docker-compose -f docker-compose.yml down
shell:
	docker-compose -f docker-compose.yml exec bash
test:
	docker-compose -f docker-compose.test.yml up