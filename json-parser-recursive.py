def parse_string(_data, index):
  string = ''
  while _data[index] != '"':
    string += _data[index]
    index += 1
  return string, index + 1

def parse_number(_data, index):
  number = ''
  while _data[index] not in (',', ']', '}'):
    number += _data[index]
    index += 1
  if number == 'null':
    number = None
  elif '.' in number:
    number = float(number)
  else:
    number = int(number)
  return number, index

def parse_json(_data, index):
  if _data[index] == '[':
    _list = []
    index += 1
    while _data[index] != ']':
      if _data[index] == '"':
        string, index = parse_string(_data, index+1)
        _list.append(string)
      elif _data[index] in (' ', ','):
        index += 1
      elif _data[index] in ('[', '{'):
        value, index = parse_json(_data, index)
        _list.append(value)
      else:
        number, index = parse_number(_data, index)
        _list.append(number)
    return _list, index + 1
  elif _data[index] == '{':
    _object = {}
    index += 1
    while _data[index] != '}':
      key, index = parse_string(_data, index+1)
      while _data[index] in (':', ' '):
        index += 1
      if _data[index] in ('{', '['):
        value, index = parse_json(_data, index)
        _object[key] = value
      elif _data[index] == '"':
        value, index = parse_string(_data, index+1)
        _object[key] = value
      else:
        number, index = parse_number(_data, index)
        _object[key] = number
      while _data[index] in (',', ' '):
        index += 1
    return _object, index + 1

# data = {}
# data = []
# data = ['', None]
# data = {'name': 'rahul  arya', 'company': 'artelus'}
data = [['alien'], 'alien', 123, 'rahul arya', 'alien', 231412344234, ['alien', 1234], [65478, 234342], [1234234324234324233], 'alienalien', ['alien', 'rahul', 'arya'], 31231, 'rahulalien', 1231312321]
# data = [{'name': 'rahul arya', 'company': 'artelus'}, None, 123.456, {'age': 27}, ['alien']]
# data = {'arya': [None, 12.34, 'surname', 'first_name', {'alien': ['rahul', 'arya']}], 'age': 27, 'alien': {'company': 'artelus', 'age': 20}, 'object': {'name': 'arya'}}

import json
json_data = json.dumps(data)
parsed_json = parse_json(json_data, 0)[0]

print (parsed_json)
