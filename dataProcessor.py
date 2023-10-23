import json
from collections import defaultdict

def read_json_file(file_path):

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")
    
def avgAgeCountry(file_path, age_transform=None):
    data = read_json_file(file_path)
        
    age_by_country = defaultdict(list)

    for entry in data:
        if 'country' not in entry:
            raise ValueError("Faltando campo 'country' no JSON")
        if 'age' not in entry:
            raise ValueError("Faltando campo 'age' no JSON")

        country = entry['country']
        age = entry['age']

        if age_transform:
            age = age_transform(age)

        age_by_country[country].append(age)

    avg_age_by_country = {}
    for country, ages in age_by_country.items():
        avg_age = sum(ages) / len(ages)
        avg_age_by_country[country] = avg_age

    return avg_age_by_country
    
print(avgAgeCountry(file_path='users.json'))