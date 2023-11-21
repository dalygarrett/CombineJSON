import os
import json

# Input and output directories
input_folder = 'Documents/public_kbs'
output_file = 'Documents/combined_data.json'

combined_data = []

for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        file_path = os.path.join(input_folder, filename)

        with open(file_path, 'r') as file:
            data = json.load(file)

        combined_data.append(data)

output_data = {'list_key': combined_data}

with open(output_file, 'w') as output_file:
    json.dump(output_data, output_file, indent=2)

print(f'Combination completed. Output saved to {output_file}')
