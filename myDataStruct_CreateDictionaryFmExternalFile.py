'''
A dictionary is like an address-book where we can find the address or contact details of a person by knowing only his/her name
i.e. we associate keys (name) with values
Dictionary is represented by dict class. Pair of keys and values are specified in dictionary using the notation
d = {key1 : value1, key2 : value2 }
When we need to create a dictionary from a list of dictionary by filtering specific keys
'''
import json

filepath = '/mnt/sda/Sandbox/PythonLab/PythonSandbox/Data/tmp.txt'
with open(filepath) as fp:
    line = fp.readline()
    while line:
        print("line: ", line)

        json_str = json.loads(line)
        print("json_str:", json_str)

        filter_list = ["a", "c"]
        d22 = [{k: d[k] for k in filter_list if k in d} for d in json_str]
        print("d22:", d22)
        line = fp.readline()