import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()


@app.mcp_tool_trigger(
    arg_name="context",
    type="mcpToolTrigger",
    tool_name="get_pet_details",
    description="Get details about a pet",
    toolProperties='[' \
        '{"propertyName": "petName", "propertyType": "string", "description": "Name of the pet", "isRequired": true, "isArray": false}, ' \
        '{"propertyName": "petType", "propertyType": "string", "description": "Type of pet (e.g., dog, cat, bird)", "isRequired": true, "isArray": false}, ' \
        '{"propertyName": "age", "propertyType": "number", "description": "Age of the pet in years", "isRequired": false, "isArray": false}, ' \
        '{"propertyName": "breed", "propertyType": "string", "description": "Breed of the pet", "isRequired": false, "isArray": false}' \
    ']',
)
def get_pet_details(context) -> str:
    
    content = json.loads(context)
    pet_name = content["arguments"]["petName"]
    pet_type = content["arguments"]["petType"]
    age = content["arguments"].get("age")
    breed = content["arguments"].get("breed")

    if pet_name == "Buddy" and pet_type == "dog":
        return f"{pet_name} is a friendly {breed if breed else 'mixed breed'} dog aged {age if age else 'unknown'} years."
    else:
        return f"Details for {pet_name}, a {pet_type}, are not available."
