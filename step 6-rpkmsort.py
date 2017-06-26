rpkm=open('rpkm.txt','r')
rpkm2=open('rpkmsort.txt','w')
g=0
ima=[[0 for col in range(2)]for row in range(23398)]
for i in rpkm:
    i=i.strip().split()
    ima[g][0]=i[0]
    ima[g][1]=float(i[1])
    g=g+1

def sort(a):
    for k in range(len(a)):
        (a[k][0],a[k][1]) = (a[k][1],a[k][0])
        a[k][0] = float(a[k][0])*(-1)
    a.sort()
    for k in range(len(a)):
        (a[k][0],a[k][1]) = (a[k][1],a[k][0])
        a[k][1] = float(a[k][1])*(-1)
        a[k][1] = str(a[k][1])
        rpkm2.write(a[k][0]+'\t'+a[k][1]+'\n')

sort(ima)

rpkm.close()
rpkm2.close()