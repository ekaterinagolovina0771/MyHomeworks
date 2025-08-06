from file_classes import JsonFile, TxtFile, CsvFile

if __name__ == "__main__":
    json_file = JsonFile('test.json')
    txt_file = TxtFile('test.txt')
    csv_file = CsvFile('test.csv')

    json_data = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}]
    txt_data = 'Hello, world!'
    csv_data = [['Name', 'Age'], ['John', 30], ['Alice', 25]]

    json_file.write(json_data)
    txt_file.write(txt_data)
    csv_file.write(csv_data)

    print(json_file.read())
    print(txt_file.read())
    print(csv_file.read())

    json_file.append({'name': 'Bob', 'age': 40})
    txt_file.append(' This is a test.')
    csv_file.append(['Bob', 40])

    print(json_file.read())
    print(txt_file.read())
    print(csv_file.read())