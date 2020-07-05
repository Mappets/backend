# import deploy config
# You can change the default deploy config with `make cnf="deploy_special.env" release`
# dpl ?= deploy.env
# include $(dpl)
# export $(shell sed 's/=.*//' $(dpl))

# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help


# DOCKER TASKS

# Build the container
build: ## Build the container release
	docker-compose -f docker-compose.yml -p mappets build

# Build the container
build-nc: ## Build the container without caching
	docker-compose build --no-cache

# Build and run the container
up: ## Spin up the project
	docker-compose -p mappets up --build

dev:
	docker-compose -f docker-compose.yml -f docker-compose-dev.yml -p mappets up --build

test:
	docker-compose -f docker-compose.yml -p mappets run --rm django python manage.py test

stop: ## Stop running containers
	docker-compose -p mappets stop

down: ## Down running containers
	docker-compose -p mappets down

clean: stop ## Stop and clean running containers
	docker-compose -p mappets down -v

# Docker release - build, tag and push the container
release: build publish ## Make a release by building and publishing the `latest` tagged containers to ECR

publish: tag ## publish the `latest` taged container to ECR
	@echo 'publish latest to $(DOCKER_REPO)'
	@eval $$(aws ecr get-login --no-include-email); \
	docker push $(DOCKER_REPO)/$(APP_NAME):latest

tag: ## Generate container `{version}` tag
	@echo 'create tag latest'
	docker tag $(APP_NAME) $(DOCKER_REPO)/$(APP_NAME):latest

run_prod:
	docker-compose -f docker-prod.yml up --build -d