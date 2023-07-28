import yaml

def read_secret(filename):
    try:
        with open (filename, 'r') as file:
            credentials = yaml.safe_load(file)
        return credentials
    except Exception as e: 
        print(f'Error al leer el archivo: {e}')
        return None