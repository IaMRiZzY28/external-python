import csv
import json
with open('example.txt', 'w') as file:
    file.write("Hello, Blah Blah Blllaaaaah!\nThis is a text file handling example with funny Indian names.")
with open('example.txt', 'r') as file:
    content = file.read()
    print("Text File Content:")
    print(content)
with open('image.png', 'rb') as file:
    binary_content = file.read()
with open('output_image.png', 'wb') as file:
    file.write(binary_content)
data = [['Name', 'Age'], 
        ['Blah Bhagat', 32], 
        ['Blaaah Bedi', 27], 
        ['Blibba Blobber', 45],
        ['Bloop Blooper', 29],
        ['Blunder Bhagat', 22]]
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    print("\nCSV File Content with Weird Names:")
    for row in reader:
        print(row)
json_data = {
    'name': 'Blah Bheem', 
    'age': 35, 
    'city': 'Blooppur', 
    'friends': ['Blaaah Baaz', 'Blip Blop', 'Blimp Bloopers'],
    'nickname': 'Blunderer'
}
with open('data.json', 'w') as file:
    json.dump(json_data, file)
with open('data.json', 'r') as file:
    json_content = json.load(file)
    print("\nJSON File Content with Weird Names and Cities:")
    print(json_content)
