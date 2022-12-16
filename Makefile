help:
	@echo "Local examples:"
	@echo "    make run-dev       # Starts a FastAPI development server locally."
	@echo "    make install       # install requirements.txt."

install:
	python -m pip install --upgrade pip
	pip install keyrings.google-artifactregistry-auth && \
	cp ./package_manager/.pypirc ${HOME} && \
	cp ./package_manager/pip.conf ./venv/ && \
	pip install --upgrade --force-reinstall --trusted-host pypi.python.org -r requirements.txt

run-dev:
	export GOOGLE_APPLICATION_CREDENTIALS=./credentials/credential.json && \
	export DEV_TOKEN=$(shell gcloud auth print-identity-token) && \
	export SERVICE=data-augmentation && \
	export PROJECT_ID=santoid-dev && \
	uvicorn main:app --timeout-keep-alive 60 --port 8080 --reload

run-test:
	export GOOGLE_APPLICATION_CREDENTIALS=./credentials/credential.json && \
	export DEV_TOKEN=$(shell gcloud auth print-identity-token) && \
	export SERVICE=data-augmentation && \
	export PROJECT_ID=santoid-dev &&\
	pytest tests

build-run:
	sudo docker build -t data-augmentation:latest . && \
	sudo docker run --name data-augmentation -p 8080:8080 data-augmentation:latest

code-formatting:
	black .
	isort .