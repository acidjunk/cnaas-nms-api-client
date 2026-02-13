import json


def fix_ref(obj):
    """Recursively update $ref paths from #/definitions/ to #/components/schemas/."""
    if isinstance(obj, dict):
        new = {}
        for k, v in obj.items():
            if k == "$ref" and isinstance(v, str):
                new[k] = v.replace("#/definitions/", "#/components/schemas/")
            else:
                new[k] = fix_ref(v)
        return new
    elif isinstance(obj, list):
        return [fix_ref(item) for item in obj]
    return obj


def convert_swagger_to_openapi(swagger):
    """Convert a Swagger 2.0 spec dict to an OpenAPI 3.1.0 spec dict."""
    openapi = {
        "openapi": "3.1.0",
        "info": swagger["info"],
        "servers": [{"url": swagger.get("basePath", "/")}],
        "paths": {},
        "components": {"schemas": {}, "securitySchemes": {}},
        "security": swagger.get("security", []),
        "tags": swagger.get("tags", []),
    }

    # Convert securityDefinitions -> components/securitySchemes
    for name, sec_def in swagger.get("securityDefinitions", {}).items():
        openapi["components"]["securitySchemes"][name] = sec_def

    # Convert definitions -> components/schemas
    for name, schema in swagger.get("definitions", {}).items():
        openapi["components"]["schemas"][name] = fix_ref(schema)

    # Default content types
    consumes = swagger.get("consumes", ["application/json"])
    produces = swagger.get("produces", ["application/json"])

    # Convert paths
    for path, path_item in swagger.get("paths", {}).items():
        new_path_item = {}
        path_level_params = path_item.get("parameters", [])

        for method, operation in path_item.items():
            if method == "parameters":
                # Convert path-level params (non-body)
                converted = []
                for p in path_level_params:
                    param = dict(p)
                    if param.get("description") is None:
                        param.pop("description", None)
                    if "type" in param and param.get("in") != "body":
                        param["schema"] = {"type": param.pop("type")}
                        if "format" in param:
                            param["schema"]["format"] = param.pop("format")
                    converted.append(param)
                new_path_item["parameters"] = converted
                continue

            if not isinstance(operation, dict):
                continue

            new_op = {}
            for key in ["summary", "description", "operationId", "tags"]:
                if key in operation:
                    new_op[key] = operation[key]

            # Convert parameters
            params = []
            request_body = None
            for p in operation.get("parameters", []):
                if p.get("in") == "body":
                    schema = fix_ref(p.get("schema", {}))
                    request_body = {
                        "required": p.get("required", False),
                        "content": {ct: {"schema": schema} for ct in consumes},
                    }
                else:
                    param = dict(p)
                    if param.get("description") is None:
                        param.pop("description", None)
                    if "type" in param:
                        param["schema"] = {"type": param.pop("type")}
                        if "format" in param:
                            param["schema"]["format"] = param.pop("format")
                    params.append(param)

            if params:
                new_op["parameters"] = params
            if request_body:
                new_op["requestBody"] = request_body

            # Convert responses
            new_responses = {}
            for status, resp in operation.get("responses", {}).items():
                new_resp = {"description": resp.get("description", "")}
                if "schema" in resp:
                    schema = fix_ref(resp["schema"])
                    new_resp["content"] = {ct: {"schema": schema} for ct in produces}
                new_responses[status] = new_resp
            new_op["responses"] = new_responses

            new_path_item[method] = new_op

        openapi["paths"][path] = new_path_item

    # Convert top-level responses
    if "responses" in swagger:
        openapi["components"]["responses"] = {}
        for name, resp in swagger["responses"].items():
            openapi["components"]["responses"][name] = {
                "description": resp.get("description", "")
            }

    return openapi


if __name__ == "__main__":
    with open("swagger.json", "r") as f:
        swagger = json.load(f)

    openapi = convert_swagger_to_openapi(swagger)

    with open("swagger-3.1.json", "w") as f:
        json.dump(openapi, f, indent=2)

    print("Done! swagger-3.1.json created.")
