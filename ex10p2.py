name = input("Enter file name: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    wds = line.split()
    if len(wds) < 2 : continue
    if wds[0] != "From" : continue
    hours = wds[5]
    time=hours.split(':')
    hour=time[0]
    #print(time[0])
    counts[hour] = counts.get(hour,0) + 1
for k,v in sorted(counts.items()):
    print(k,v)



        #counts[email] = counts.get(email,0) + 1
