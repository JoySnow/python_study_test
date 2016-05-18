import json

filep = open("output.json", "w+")
mydict = {'foo': {'bar': ('baz', None, 1.0, 2)}}
myjson = json.dump(mydict, filep, indent=4, separators=(',',':'), sort_keys=True)
filep.close()



