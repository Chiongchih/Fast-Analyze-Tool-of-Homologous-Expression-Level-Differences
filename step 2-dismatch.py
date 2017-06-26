align = open('R.align', 'r')
disAlign = open('R.disalign', 'w')
fastq = open('SRR.fastq', 'r')
fastq2 = open('SRR.fastq', 'r')

all = align.read().strip()
all = all.split(" ")
count = 0

for line in fastq:
    if re.match(r"@SRR1793918(.*)", line):
        fastq2.readline()
        li = line.strip().split()
        if li[0] != ali[count]:
            disAlign.write(line)
            disAlign.write(fastq2.readline())
            disAlign.write(fastq2.readline())
            disAlign.write(fastq2.readline())
        else:
            count += 1
            fastq2.readline()
            fastq2.readline()
            fastq2.readline()

fastq.close()
fastq2.close()
disAlign.close()
align.close()


