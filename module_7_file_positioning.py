
def custom_write(file_name: str, strings: list) -> dict:
    file = open(file_name, 'w', encoding='utf-8')
    string_positions ={}
    for i in range(len(strings)):
        string_positions[(i, file.tell())] = strings[i]
        file.write(strings[i] + '\n')
    file.close()
    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

