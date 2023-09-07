from json_validator import JsonValidator

# Create an instance of the JsonValidator class
validator = JsonValidator("schema/schema.json")

# JSON data file to be validated
json_file_to_validate = "data/data_to_validate.json"

# Validate the JSON data against the schema
is_valid = validator.validate_schema(json_file_to_validate)

if is_valid:
    print("Validation succeeded. The JSON data is valid.")
else:
    print("Validation failed. The JSON data is not valid.")
