import sys

if len(sys.argv) == 1:
    print("none")
else:
    params = sys.argv[1:]
    
    print(f"parameters: {len(params)}")
    
    for word in params:
        print(f"{word}: {len(word)}")