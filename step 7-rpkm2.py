lls=open('rpkmsort.txt','r')
rpkm2=open('rpkmss.txt','w')
lll=lls.readline()
for i in lls:
    llll=i.strip().split()
    vv=float(llll[1])*1000/75
    vvv=str(vv)
    #print(llll[3])
    rpkm2.write(llll[0]+'\t'+vvv+'\n')
rpkm2.close()
lls.close()