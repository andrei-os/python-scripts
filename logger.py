import time
import sys

# mimics "tail -f" used to log files
def tail(f):
    f.seek(0, 2)

    while True:
        line = f.readline();

        if not line:
            time.sleep(0.1)
        else:
            yield line

# mimics "grep pattern"
def grep(lines, pattern):
    for line in lines:
        if pattern in line:
            yield line


if len(sys.argv) != 3:
    print("Provide file to log and pattern to match.", file = sys.stderr)
    sys.exit(1)

# mimics "tail -f file | grep pattern"
for line in grep(tail(open(sys.argv[1])), sys.argv[2]):
    print(line)
