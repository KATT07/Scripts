import csv
lst=[]
with open('csv.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if not row[7][0].isalpha():
            lst.append([row[1],int(round(float(row[7])*18/5))])
    csv_file.close()

x=0
l2=""
l3=""
h=0
m=0
s=-(int(input("Enter OFFSET(seconds):"))) #enter offset in seconds here
f=open("subs.srt","w")
for i in range(len(lst)):
    s=s+1
    if s==60:
        s=0
        if m==60:
            m=0
            h+=1
        else:
            m+=1
    if s>=0:
        x+=1
        l1=str(x)
        l2=str(h)+":"+str(m)+":"+str(s)+",000 --> "+str(h)+":"+str(m)+":"+str(s)+",999"
        l3="Speed :"+str(lst[i][1])
        f.write(l1+"\n")
        f.write(l2+"\n")
        f.write(l3+"\n\n")
        print(l1+"\n"+l2+"\n"+l3+"\n")
