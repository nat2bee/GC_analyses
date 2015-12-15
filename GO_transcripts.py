#!/usr/local/bin/python


"""
Take a list of GO terms and find all the transcripts with them in the annotation table.

Developed (in my case) to find transcripts potentially involved in the social behaviour
using a list of GO terms from literature. 

Usage = GO_transcripts.py -i <list> -a <annotation> -o <output>

Where: 
list = list with all the GO terms to search for (one per line)
output = the name of the output to save the list if transcripts Ids
annotation = table result from Annocript containing the information from annotation (...filt_ann_out.txt)

Options: -h for usage help
"""

import sys, getopt

# Check for the arguments, open the inputs and print useful help messages

try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:a:o:",["list=","annotation","output="])
except getopt.GetoptError:
    print '\n', '####     Invalid use     ####', '\n'
    print 'Usage = GO_transcripts.py -i <list> -a <annotation> -o <output>'
    print 'For help use GO_transcripts.py -h'
    sys.exit(99)
    
for opt, arg in opts:
    if len(arg) < 3 and opt == '-h':
        print '\n', 'Take a list of GO terms and find all the transcripts with them in the annotation table.', '\n'
        print 'Usage = GO_transcripts.py -i <list> -a <annotation> -o <output>'
        print 'Where: list = list with all the GO terms to search for (one per line)'
        print 'output =  the name of the output to save the list if transcripts Ids'
        print 'annotation = table result from Annocript containing the information from annotation (...filt_ann_out.txt)'
        sys.exit()
    elif len(arg) > 3:
        if opt in ("-i", "--list"):
            list = open(arg)
        if opt in ("-a", "--annotation"):
            annotation = open(arg)
        if opt in ("-o", "--output"):
            output = open(arg,"w")
    elif len(arg) < 3:
        print '\n', '###    Arguments are missing   ###', '\n', '\n' 'Use -h option for help\n'
        sys.exit(1)
    else:
        assert False, "unhandled option"


go_list = []


# Open the list of GOs and save them in a list

for go in list:
    go_name = go.split("\n")
    go_name = go_name[0]
    go_list.append(go_name)
    

# Check if the GO is in the annotation table line, if so save the transcript Id

for line in annotation:
    elements = line.split("\t")
    transcript_id = elements[0]
    for go in go_list:
        if go in line:
            output.write(transcript_id)
            output.write("\n")
    

output.close()
