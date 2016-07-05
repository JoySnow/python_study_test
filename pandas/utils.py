import glob
import sys
import json


def parse_sysctl_conf(path):
    for record in read_json(path):
        for line in record['content'].splitlines():
            parsed = record.copy()
            del parsed['content']
            row = line.strip()
            if not row or "=" not in row or row.startswith('#'):
                continue

            try:
                (key, value) = row.split("=", 1)
            except:
                raise

            parsed["key"] = key.strip()
            parsed["value"] = value.strip()
            yield parsed
            

def read_json(path):
    for p in glob.glob(path):
        with open(p) as fp:
            for line in fp:
                yield json.loads(line)

if __name__ == '__main__':
    list(parse_sysctl_conf(sys.argv[1]))

    
