fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname,'r')
count = 0
for line in fh:
    line=line.rstrip()
    wds=line.split()
    if len(wds)<3 or wds[0]!='From':
        continue
    print(wds[1])
    count=count+1


print("There were", count, "lines in the file with From as the first word")
