
# JSON Validation Project

This project provides a Python tool for validating JSON data against a specified schema. It includes a `JsonValidator` class that can check for various schema rules, such as required fields, field values, and more.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Features

The `JsonValidator` class in this project supports the following schema validation features:

1. Required fields: Ensure that specific fields in the JSON data are mandatory.
2. At least one of many fields: Check that at least one of a set of fields is present in the JSON data.
3. Either one field or another field: Validate that either one field or another field (mutually exclusive) is present in the JSON data.
4. Mutually exclusive fields: Ensure that if one field is present, another field should not be present.
5. Field value to be one of a set of values: Validate that a field's value matches one of a predefined set of values (enum).

## Installation

To use this JSON validation tool, follow these steps:

1. Clone this GitHub repository:

   ```shell
   git clone https://github.com/yourusername/json-validation-project.git
   ```

2. Change to the project directory:

   ```shell
   cd json-validation-project
   ```

3. (Optional) Create and activate a virtual environment:

   ```shell
   python -m venv venv
   source venv/bin/activate   # On Windows, use: venv\Scripts\activate
   ```

4. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

To use the JSON validation tool, you can create an instance of the `JsonValidator` class and call the `validate_schema` method. Here's an example:

```python
from json_validator import JsonValidator

# Create an instance of the JsonValidator class
validator = JsonValidator(schema_file="path/to/schema.json", schema_integrity_file="path/to/schema_integrity.json")

# JSON data to be validated (provide the path to your JSON data file)
json_file_to_validate = "path/to/your/data.json"

# Validate the JSON data against the schema
is_valid = validator.validate_schema(json_file_to_validate)

if is_valid:
    print("Validation succeeded. The JSON data is valid.")
else:
    print("Validation failed. The JSON data is not valid.")
```

Replace `"/schema.json"`, and `"/data.json"` with the actual file paths and JSON data you want to validate.

## Project Structure

The project directory structure is organized as follows:

- `json_validator.py`: The Python script containing the `JsonValidator` class.
- `validation_script.py`: An example script demonstrating how to use the `JsonValidator` class.
- `data/`: Directory containing JSON data files for validation.
- `README.md`: This README file.


## Contributing

Contributions to this project are welcome! If you have suggestions or want to report issues, please open an [issue](https://github.com/sejalmankar1012/json-validation-project/issues) or submit a [pull request](https://github.com/sejalmakar1012/json-validation-project/pulls).

