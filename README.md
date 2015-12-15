# GC_analyses
Scripts to analyse the GC content of the transcripts and to find transcripts from especific GO categories.


# GO_transcripts.py

Take a list of GO terms and find all the transcripts with them in the annotation table generated from **Annocript** (Musacchia et al. Annocript: a flexible pipeline for the annotation of transcriptomes able to identify putative long noncoding RNAs. Bioinformatics 2015, 31(13):2199-201. doi: 10.1093/bioinformatics/btv106).

Developed (in my case) to find transcripts potentially involved in the social behaviour
using a list of GO terms from literature. 

**Usage:**
GO_transcripts.py -i *list* -a *annotation* -o *output*

**Where:** 
- list = list with all the GO terms to search for (one per line)
- output = the name of the output to save the list if transcripts Ids
- annotation = table result from **Annocript** containing the information from annotation (*...filt_ann_out.txt*)

**Options:**
-h for usage help


# GetGC.py

Get the GC % from each transcript in a fasta file

**Usage:**
GetGC.py -f *fasta* -o *output*

**Where:**
- fasta = the fasta file containing all the sequences
- output = Name of the output file (table containing the GC results)
