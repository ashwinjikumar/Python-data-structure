# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
dum=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue

    hari=line.find(':')
    count=count+1
    dum=float(line[hari+2:])+dum
print('Average spam confidence:',float(dum/count))
