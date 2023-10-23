import os
import unittest
from dataProcessor import read_json_file, avgAgeCountry

class TestDataProcessor(unittest.TestCase):
    def test_read_json_file_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)
       
        self.assertEqual(len(data), 1000)  # Ajustar o número esperado de registros
        self.assertEqual(data[0]['name'], 'William Todd')
        self.assertEqual(data[1]['age'], 54)

    def test_read_json_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_json_file("non_existent.json")

    def test_read_json_file_invalid_json(self):
        with open("invalid.json", "w") as file:
            file.write("invalid json data")
        with self.assertRaises(ValueError):
            read_json_file("invalid.json")
    
    # Aqui
    
    def test_avgAgeCountry_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        result = avgAgeCountry(file_path)
       
        self.assertEqual(result['US'], 40.89208633093525)
        self.assertEqual(result['AU'], 37.25735294117647)

    def test_avgAgeCountry_json_vazio(self):
        with open("vazio.json", "w") as file:
            file.write("[]") 

        with self.assertRaises(ValueError):
            avgAgeCountry("vazio.json")

    def test_avgAgeCountry_age_ausente(self):
        with open("age_ausente.json", "w") as file:
            file.write('{"name": "Alice", "country": "US"}')

        with self.assertRaises(ValueError):
            avgAgeCountry("age_ausente.json")

    def test_avgAgeCountry_country_ausente(self):
        with open("country_ausente.json", "w") as file:
            file.write('{"name": "Alice", "age": 25}')

        with self.assertRaises(ValueError):
            avgAgeCountry("country_ausente.json")

    def test_avgAgeCountry_com_transform(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        def age_in_months(age):
            return age * 12

        result = avgAgeCountry(file_path, age_transform=age_in_months)
       
        self.assertEqual(result['US'], 40.89208633093525 * 12)
        self.assertEqual(result['AU'], 37.25735294117647 * 12)

if __name__ == '__main__':
    unittest.main()