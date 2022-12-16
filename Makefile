help:
	@echo "Local examples:"
	@echo "    make run-dev       # Starts a FastAPI development server locally."
	@echo "    make install       # install requirements.txt."

install:
	python -m pip install --upgrade pip && \
	pip install --upgrade --force-reinstall --trusted-host pypi.python.org -r requirements.txt

run-dev:
	uvicorn main:app --timeout-keep-alive 60 --port 8080 --reload

build-run:
	sudo docker build -t knn-mobile-predict:latest . && \
	sudo docker run --name knn-mobile-predict -p 8080:8080 knn-mobile-predict:latest

code-formatting:
	black .
	isort .