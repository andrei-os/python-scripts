import sys

if len(sys.argv) != 4:
    print('Input file path, old and new string.')
    sys.exit(1)

path = sys.argv[1]
old = sys.argv[2]
new = sys.argv[3]

updated_content = []
with open(path, 'r') as file:
    for line in file:
        updated_content.append(line.replace(old,new))

with open(path, 'w') as file:
    for line in updated_content:
        file.write(line)
