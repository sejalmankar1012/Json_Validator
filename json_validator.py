import jsonschema
import json

class JsonValidator:
    '''
    Class to validate the JSON Schema 
    :param1: schema_file, A Schema file as per validation instructions
    :type param1: file
    :param2: schema_integrity_file, An integrity file 
    :type param2: file
    '''
    def __init__(self, schema_file, schema_integrity_file=None):
        self.schema_file = schema_file
        self.schema_integrity_file = schema_integrity_file

    def validate_schema(self, json_file)->bool:
        '''
        Method to validate a json file
        :param : json_file, A json file to be validated
        :type param: file
        :returns true if file is validated
        '''
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)

            with open(self.schema_file, 'r') as f:
                schema = json.load(f)

            if self.schema_integrity_file:
                with open(self.schema_integrity_file, 'r') as f:
                    schema_integrity = json.load(f)
                validator = jsonschema.validators.validator_for(schema)(schema, schema_integrity=schema_integrity)
            else:
                validator = jsonschema.validators.validator_for(schema)(schema)

            validator.validate(data)
            return True
        except jsonschema.ValidationError as e:
            print(e)
            return False
        except FileNotFoundError as err:
            print("File not found.",err)
            return False
