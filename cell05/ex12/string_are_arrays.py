import sys

if len(sys.argv) == 1:
    print("none")
else:
    string = sys.argv[1]
    z_count = string.count('z')

    if z_count > 0:
        print("z" * z_count)
    else:
        print("none")