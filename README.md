# automation Yaml2file

This script tries to parse a yaml file of fstab configs and create a fstab file similar like /etc/fstab

#RUN
python main.py

#How Code Works
1. **PyYAML** is a YAML parser and emitter for Python. PyYAML features a complete YAML 1.1 parser, Unicode support, pickle support, capable extension API, and sensible error messages.

import yaml


2. This part is reading Yaml file and assigning its values to a variable named configuration which is a dictionary type. And after that iterates over imported yaml and creates a list named **entities** containing each fstab entry.


entities = []
with open('fstab.yaml', 'r') as file:
    configuration = yaml.safe_load(file)
    for k, v in configuration.items():
        for i in configuration[k].items():
            entities.append(i)

3. We are reading original /etc/fstab file to keep original values and adding new values by iterating over the imported entities list. entities is basically a list of tuples like below.

[('/dev/sda1', {'mount': '/boot', 'type': 'xfs'}), ('/dev/sda2', {'mount': '/', 'type': 'ext4'}), ('/dev/sdb1', {'mount': '/var/lib/postgresql', 'type': 'ext4', 'root-reserve': '10%'}), ('192.168.4.5', {'mount': '/home', 'export': '/var/nfs/home', 'type': 'nfs', 'options': ['noexec', 'nosuid']})]

We have set a check base on type of file system type as nfs have dirrerent type of entry.


f = open('fstab', 'w')
origin = open('/etc/fstab', 'r')
f.writelines(origin.readlines())

for i, z in entities:
    if z['type'] != 'nfs':
        f.write(i + '\t' + z['mount'] + '\t' + z['type'] + '\t' + '0 0''\n')
    else:
        f.write(i + ':' + z['export'] + '\t' + z['mount'] + '\t' + z['type']+ '\t')
        if 'options' in z:
            f.writelines(",".join(z['options']) + '\t' + '0 0''\n')
        else:
            f.write('defaults' + '0 0''\n')

f = open("fstab", "r")
print(f.read())
f.close()
origin.close()



