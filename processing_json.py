import os
import json
import sys

path='/srv/runme/'

def extract(x):
    return x['name'],x['prop']['age']

def extracting(prefix):
    prefixed = [path+filename for filename in os.listdir(path) if filename.startswith(prefix) and filename.endswith('json')]
    if len(prefixed)>0:
        for filename in prefixed:
            f=open(filename,'r')
            content=[json.loads(line) for line in f.readlines()]
            f.close()
            extracted=map(lambda x: extract(x),content)
            time_file = open("%s.txt"%filename.split('.')[0], "w")
            time_file.write('\n'.join(['name: %s  age: %s'%(i[0],i[1]) for i in extracted]))
            time_file.close()

prefix = sys.argv[1]
extracting(prefix)