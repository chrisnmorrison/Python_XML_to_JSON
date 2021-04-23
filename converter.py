import json
import xmltodict

# to convert other files, simply modify the filename in the following line
with open('input.xml') as xml_file:
    # converts XML data to a dictionary
    data = xmltodict.parse(xml_file.read())

    # once finished, closes file
    xml_file.close()

    # converts an object to JSON format. In this case, converts dictionary to JSON
    json_conversion = json.dumps(data)

    # writes the converted data to a new JSON file.
    with open('output.json', 'w') as json_file:
        json_file.write(json_conversion)

        json_file.close()
