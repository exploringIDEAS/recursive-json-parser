def parse_json(_data, index):
  if _data[index] == '[':
    _list = []
    index = index + 1
    open_sbrackets = 1
    while open_sbrackets != 0:
      if _data[index] == '"':
        string = ''
        index += 1
        while _data[index] != '"':
          string += _data[index]
          index += 1
        _list.append(string)
        index += 1
      elif _data[index] in (' ', ','):
        index += 1
      elif _data[index] in ('[', '{'):
        value, index = parse_json(_data, index)
        _list.append(value)
      elif _data[index] == ']':
        open_sbrackets -= 1
      else:
        number = ''
        while _data[index] not in (',', ']'):
          number += _data[index]
          index += 1
        if number == 'null':
          _list.append(None)
        elif '.' in number:
          _list.append(float(number))
        else:
          _list.append(int(number))
    return _list, index + 1
  elif _data[index] == '{':
    _object = {}
    index += 1
    open_cbrackets = 1
    while open_cbrackets != 0:
      key = ''
      index += 1
      while _data[index] != '"':
        key += _data[index]
        index += 1
      index += 1
      while _data[index] in (':', ' '):
        index += 1
      if _data[index] in ('{', '['):
        value, index = parse_json(_data, index)
        _object[key] = value
      elif _data[index] == '}':
        open_cbrackets -= 1
      elif _data[index] == '"':
        string = ''
        index += 1
        while _data[index] != '"':
          string += _data[index]
          index += 1
        _object[key] = string
        index += 1
      else:
        number = ''
        while _data[index] not in (',', '}'):
          number += _data[index]
          index += 1
        if number == 'null':
          _object[key] = None
        elif '.' in number:
          _object[key] = float(number)
        else:
          _object[key] = int(number)
      while _data[index] in (',', ' '):
        index += 1
      if _data[index] == '}':
        open_cbrackets -= 1
    return _object, index + 1

data = {'name': 'rahul  arya', 'company': 'artelus'}
data = [['alien'], 'alien', 123, 'rahul arya', 'alien', 231412344234, ['alien', 1234], [65478, 234342], [1234234324234324233], 'alienalien', ['alien', 'rahul', 'arya'], 31231, 'rahulalien', 1231312321]
data = [{'name': 'rahul arya', 'company': 'artelus'}, None, 123.456, {'age': 27}, ['alien']]
data = {'arya': [None, 12.34, 'surname', 'first_name', {'alien': ['rahul', 'arya']}], 'age': 27, 'alien': {'company': 'artelus', 'age': 20}, 'object': {'name': 'arya'}}

import json
json_data = json.dumps(data)
parsed_json = parse_json(json_data, 0)[0]

print (parsed_json)
