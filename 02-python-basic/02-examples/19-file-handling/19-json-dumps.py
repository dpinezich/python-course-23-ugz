import json

data = {
    'employees' : [
        {
            'name' : 'John Doe',
            'department' : 'Marketing',
            'place' : 'Remote'
        },
        {
            'name' : 'Jane Doe',
            'department' : 'Software Engineering',
            'place' : 'Remote'
        },
        {
            'name' : 'Don Joe',
            'department' : 'Software Engineering',
            'place' : 'Office'
        }
    ]
}

# .dumps() as a string
json_string = json.dumps(data)
print(json_string)

# Using a JSON string
with open('json_data.json', 'w') as outfile:
    outfile.write(json_string)

# Directly from dictionary
#with open('json_data.json', 'w') as outfile:
#    json.dump(json_string, outfile)
