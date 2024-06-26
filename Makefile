SHELL := /bin/bash

.PHONY: set-envs, run, install-requirements

set-envs:
	export TF_ENABLE_ONEDNN_OPTS=0
	export TF_CPP_MIN_LOG_LEVEL=3

install-requirements:
	pip3 install -r requirements.txt

run:
	uvicorn main:app --host 0.0.0.0 --port 8000

build:
	docker build -t ai-model .
run-bg:
	docker run -p 8000:8000 ai-model
