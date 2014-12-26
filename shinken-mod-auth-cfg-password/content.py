
import json
import tarfile
import os
import sys
from os.path import join

base_dir = sys.argv[1]

tar = tarfile.open('content.tar', 'w')
for elem in os.listdir(base_dir):
    tar.add(join(base_dir, elem), arcname=join('.', elem))

package_content = []
for e in tar.getmembers():
    package_content.append({
        'name': e.name,
        'mode': e.mode,
        'type': e.type,
        'size': e.size
    })

tar.close()
os.remove('content.tar')

print(json.dumps(package_content))
