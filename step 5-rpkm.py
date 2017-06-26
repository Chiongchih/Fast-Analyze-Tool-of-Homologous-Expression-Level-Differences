import collections
sam = open('S.sorted.sam', 'r')
sam_split = open('Rs.psam', 'r')
gtf = open('exome.gtf', 'r')
rpk = open('Ss.rpkm', 'w')

change = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 'M', 'X', 'Y']
chan = {'1':1, '10':10, '11':11, '12':12, '13':13, '14':14, '15':15, '16':16, '17':17, '18':18, '19':19, '2':2, '20':20, '21':21, '22':22, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'M':23, 'X':24, 'Y':25}
chrom_gene = []
for c in change:
    chrom = open('chromosome'+str(c)+".txt", 'r')
    chrom_gene.append(['' for i in xrange(len(chrom.read().strip()))])

gene_id = collections.OrderedDict()
totalreads = 0

for line in gtf:
    li = line.strip().split()
    gene = li[0]
    gene_id[gene] = [0, 0]
    le = 0
    ch = li[0].split('@')
    if len(ch[0]) > 5:
        continue
    ch = ch[0][3:len(ch[0])]
    for i in xrange(len(li)-1):
        lo = li[i+1]
        lo = lo.split(',')
        le += int(lo[1]) - int(lo[0]) + 1
        #print gene
        for j in range(int(lo[0])-1,int(lo[1])):
            chrom_gene[chan[ch]-1][j] += gene + ' '
    gene_id[gene][0] = le

for i in xrange(27):
    line = sam.readline()
    line = sam_split.readline()

for line in sam:
    lin = line.strip().split()
    test = lin[1]
    if test == '4':
        continue
    totalreads += 1
    ch = lin[2][3:len(lin[2])]
    lo = int(lin[3])
    try:
        genes = chrom_gene[chan[ch]-1][lo]
    except:
        print lin
        print genes
    if genes == '':
        continue
    for g in genes.split():
        gene_id[g][1] += 1


read_id = -1
for line in sam_split:
    lii = line.strip().split()
    test = lii[1]
    if test == '4':
        continue
    read = lii[0].split('.')
    temp = read[1]
    if read_id == temp:
        continue
    else:
        totalreads += 1
        read_id = temp
    ch = lii[2][3:len(lii[2])]
    lo = int(lii[3])
    try:
        genes = chrom_gene[chan[ch]-1][lo]
    except:
        print line
        print genes
    if genes == '':
        continue
    for g in genes.split():
        gene_id[g][1] += 1

rpk.write(str(totalreads)+'\n')
for c in gene_id:
    try:
        rpk.write(c+'\t'+str(float(1000000000*gene_id[c][1])/(gene_id[c][0]*totalreads))+'\n')
    except:
        print c+'\t'+str(gene_id[c][0])+'\t'+str(gene_id[c][1])
rpk.close()
sam.close()
gtf.close()
sam_split.close()
