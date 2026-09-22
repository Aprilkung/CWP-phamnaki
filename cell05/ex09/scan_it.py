import sys

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    search_string = sys.argv[2]
    
    match_count = search_string.count(keyword)
    
    if match_count > 0:
        print(match_count)
    else:
        print("none")