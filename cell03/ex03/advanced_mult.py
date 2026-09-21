import sys

if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    # แม่สูตร
    while i <= 10:
        row = "Table de " + str(i) + ":"
        j = 0
        # ตัวคูณ
        while j <= 10:
            row += " " + str(i * j)
            j += 1
        print(row)
        i += 1