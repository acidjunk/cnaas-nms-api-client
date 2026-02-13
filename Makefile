.PHONY: generate convert build clean lint

generate:
	rm -rf /tmp/cnaas-generated
	openapi-python-client generate \
		--path swagger_files/swagger-3.1.json \
		--meta uv \
		--config openapi-client-config.yaml \
		--output-path /tmp/cnaas-generated
	rm -rf cnaas_nms_api_client
	cp -r /tmp/cnaas-generated/cnaas_nms_api_client .

convert:
	cd swagger_files && python ../convert_swagger.py

build:
	uv build

clean:
	rm -rf dist/ build/ *.egg-info

lint:
	uv run ruff check .
	uv run ruff format --check .
