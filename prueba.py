m = [["x", "x", "x"], ["x", "o", "o"], ["o", "x", "o"]]
print(m)

for row in m:
    if "".join(row) == "xxx" or "".join(row) == "ooo":
        print("won in rows")
    else:
        print("loose in rows")

m = [["x", "x", "o"], ["x", "o", "o"], ["o", "x", "o"]]
print(m)

for col in range(len(m)):
    cols = [val[col] for val in m]
    if "".join(cols) == "xxx" or "".join(cols) == "ooo":
        print("won in cols")
    else:
        print("loose in cols")


main_diagonal = [m[index][index] for index in range(len(m))]

if "".join(main_diagonal) == "xxx" or "".join(main_diagonal) == "ooo":
    print("won in main diagonal")
else:
    print("loose in main diagonal")




secondary_diagonal = [m[index][len(m) -1 - index] for index in range(len(m))]
if "".join(secondary_diagonal) == "xxx" or "".join(secondary_diagonal) == "ooo":
    print("won in secondary diagonal")
else:
    print("loose in secondary diagonal")
    