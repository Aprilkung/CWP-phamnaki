import sys

if len(sys.argv) < 3:
    print("none")
else:
    params = sys.argv[1:]
    params.reverse()
    
    for p in params:
        print(p)