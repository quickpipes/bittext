APP_NAME=bittext
IMAGE_NAME=ghcr.io/quickpipes/$(APP_NAME)

############
# Docker
#

docker-build:
	@echo "Building $(APP_NAME)"
	docker build -t $(IMAGE_NAME) .

docker-release:
	docker buildx build --platform linux/amd64,linux/arm64 -t $(IMAGE_NAME):latest --push .

docker-make-builder:
	docker buildx create --name builder --use
	docker buildx inspect --bootstrap
