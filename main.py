import yaml

entities = []
with open('fstab.yaml', 'r') as file:
    configuration = yaml.safe_load(file)
    for k, v in configuration.items():
        for i in configuration[k].items():
            entities.append(i)

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
