# converters/json_converter.py
import json

class JsonConverter:
    @staticmethod
    def read(file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON file: {str(e)}")
        except Exception as e:
            raise IOError(f"Error reading JSON file: {str(e)}")

    @staticmethod
    def write(data, file_path):
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            raise IOError(f"Error writing JSON file: {str(e)}")
