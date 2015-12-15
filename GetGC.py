####################################################################################### 
#
# Get the GC % from each transcript in a fasta file
#
# Usage: GetGC.py -f <fasta> -o <output>
#
# Where:
# fasta = the fasta file containing all the sequences
# output = Name of the output file (table containing the GC results)
#
# 
#######################################################################################

#!/usr/bin/python

import sys, getopt
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

c = 0

fasta = ""
input1 = ""
outputfile = ""
gcpercentage = float()

# Check for the arguments and print useful help messages

try:
    opts, args = getopt.getopt(sys.argv[1:],"hf:o:",["fasta=","output="])
except getopt.GetoptError:
    print '\n', '####     Invalid use     ####', '\n'
    print 'Usage: GetGC.py -f <fasta> -o <output>'
    print 'For help use GetGC.py -h'
    sys.exit(99)

for opt, arg in opts:
    if opt == '-h':
        print '\n', 'Get the GC % from each transcript in a fasta file.', '\n'
        print 'Usage: GetGC.py -f <fasta> -o <output>'
        print 'Where: fasta = the fasta file containing all the sequences'
        print 'output = Name of the output file' , '\n'
        sys.exit()
    elif opt in ("-f", "--fasta"):
        fasta = open(arg)
    elif opt in ("-o", "--output"):
        outname = arg
        outputfile = open(outname,"w")
    else:
        assert False, "unhandled option"


## Open the fasta file
for seq_record in SeqIO.parse(fasta, "fasta"):
    gene_id = str(seq_record.id)
    bases = str(seq_record.seq)
    if c == 0:
        outputfile.write("Transcript_ID\t%GC\n")
        c = c + 1
    else:
        nbases = bases.count("n") + bases.count("N")
        gcpercentage = float(bases.count("c")+ bases.count("C")+ bases.count("g")+ bases.count("G"))*100/(len(bases)-nbases)
        gcpercentage = str(gcpercentage)
        outputfile.write(gene_id)
        outputfile.write("\t")
        outputfile.write(gcpercentage)
        outputfile.write("\n")
    
         
outputfile.close()
