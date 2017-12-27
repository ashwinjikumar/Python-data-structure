fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    h=line.split()
    for x in h:
        if x not in lst:
            lst.append(x)
            lst.sort()
print(lst)
