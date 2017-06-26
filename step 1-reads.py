find = open('R.align', 'w')
sams = open('S.sam','r')
for l in sams:
    if re.match(r"SR(.*)", line):
        ll=l.split('\t')
        if int(ll[1]) !=4:
            find.write('@'+str(ll[0])+" ")
find.close()
sams.close()