import json

def converter(path):
    with open(path, encoding='utf-8') as file:
        data = json.load(file)

    with open(path, 'w', encoding='utf-8') as fil:
        json.dump(data, fil, ensure_ascii=True, indent=2)

path = 'fixtures.json'

converter(path)