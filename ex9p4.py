name = input("Enter file name: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name,'r')
count = 0
o_dic=dict()
dum=None
for line in handle:
    line=line.rstrip()
    wds=line.split()
    if len(wds)<3 or wds[0]!='From':
        continue
    #print(wds[1])
    if dum==wds[1]:
        dum=wds[1]
        o_dic[dum]=o_dic[dum]+1
    else :
        dum=wds[1]
        o_dic[dum]=1
print(o_dic)
bigcount=None
bigword=None
for word,count in o_dic.items():
    #for word in wds
    #o_dic[word]=o_dic.get(word,0)+1
    #print(o_dic)
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print("now final output")
print(bigword,bigcount)

#print(o_dic)
