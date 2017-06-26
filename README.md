# Fast-Analyze-Tool-of-Homologous-Expression-Level-Differences
Fast analyze tool of homologous expression level differences (FATHED) is a useful tool based on the famous tool Tophat by Johns Hopkins University( https://ccb.jhu.edu/software/tophat/index.shtml). And my new tool FATHED utilize the basic idea of tophat, while my attention is a higher efficiency and higher rate to analyze the large scale (human chromosomes level) datas and find out the special differences among different samples (same gene, different expression). FATHED can complete the job in a higher rate because it simplify the step of alignment. Each read will only be cut into 4 parts and align on genome randomly and once the disalign happened, FATHED will determine this read only depend on its alignment score (control by user). And the rpkm file will easily show the result of efficiency and score in a clear way.