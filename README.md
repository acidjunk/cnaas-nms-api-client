# cnaas-nms-api-client

A typed Python client library for the [CNaaS NMS](https://github.com/SUNET/cnaas-nms) API, auto-generated from the OpenAPI specification using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

## Installation

```bash
pip install cnaas-nms-api-client
```

Or install directly from GitHub:

```bash
pip install git+https://github.com/acidjunk/cnaas-nms-api-client.git
```

## Usage

```python
from cnaas_nms_api_client import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://your-cnaas-instance/api/v1.0",
    token="your-api-token",
)

# Example: list devices
from cnaas_nms_api_client.api.device import get_devices_api
response = get_devices_api.sync_detailed(client=client)
print(response.status_code)
```

Every endpoint has both `sync_detailed` and `asyncio_detailed` variants for synchronous and async usage.

## Development

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
# Clone and install
git clone https://github.com/acidjunk/cnaas-nms-api-client.git
cd cnaas-nms-api-client
uv sync

# Regenerate client from OpenAPI spec
make generate

# Build package
make build

# Lint
make lint
```

## Regenerating the Client

If the upstream CNaaS NMS API changes:

1. Place the updated Swagger 2.0 spec in `swagger_files/swagger.json`
2. Run `make convert` to produce the OpenAPI 3.1 spec
3. Run `make generate` to regenerate the Python client

## License

MIT
