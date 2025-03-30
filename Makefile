# Makefile for buckpal project

.PHONY: build start stop logs restart clean shell db_shell

build:
	docker-compose build

start:
	docker-compose up -d

stop:
	docker-compose down

restart:
	docker-compose restart

logs:
	docker-compose logs -f

shell:
	docker-compose exec web /bin/bash

db_shell:
	docker-compose exec db psql -U postgres -d buckpal

clean:
	docker-compose down --rmi all --volumes --remove-orphans

alembic-init:
	docker-compose run --rm web alembic init migrations

alembic-revision:
	docker-compose run --rm web alembic revision --autogenerate -m "initial migration"

alembic-upgrade:
	docker-compose run --rm web alembic upgrade head

test:
	docker-compose run --rm -e DATABASE_URL=postgresql://postgres:password@test_db:5432/buckpal_test web pytest tests -v --cov=app
