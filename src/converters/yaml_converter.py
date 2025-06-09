# converters/yaml_converter.py
import yaml

class YamlConverter:
    @staticmethod
    def read(file_path):
        try:
            with open(file_path, 'r') as file:
                return yaml.safe_load(file)
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML file: {str(e)}")
        except Exception as e:
            raise IOError(f"Error reading YAML file: {str(e)}")

    @staticmethod
    def write(data, file_path):
        try:
            with open(file_path, 'w') as file:
                yaml.dump(data, file, default_flow_style=False)
        except Exception as e:
            raise IOError(f"Error writing YAML file: {str(e)}")
