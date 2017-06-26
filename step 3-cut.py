import re
reads = open('R.disalign', 'r')
reads_r = open('R.disalign', 'r')
reads_cut = open('R.disaligncut.disAlign', 'w')


for l in reads:
    if re.match(r"@SRR(.*)", l):
        line1 = reads_r.readline().strip()
        line1 = line1.split()
        seq = reads_r.readline().strip()
        line3 = reads_r.readline().strip()
        line3 = line3.split()
        qual = reads_r.readline().strip()
        for i in xrange(4):
            reads_cut.write(line1[0]+'.'+str(i+1)+'\t'+line1[1]+'\t'+'length = 25'+'\n')
            reads_cut.write(seq[i*25:(i+1)*25]+'\n')
            reads_cut.write(line3[0]+'.'+str(i+1)+'\t'+line3[1]+'\t'+'length = 25'+'\n')
            reads_cut.write(qual[i*25:(i+1)*25]+'\n')