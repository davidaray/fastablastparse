
from Bio import SeqIO
import argparse

def get_args():
	parser = argparse.ArgumentParser(description="Iterative pseudoreference generation with pseudo-it", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-i', '--ifasta', type=str, help='Name of the peptide file', required=True)
	parser.add_argument('-b', '--blastp', type=str, help='Name of the blastp file', required=True)
	parser.add_argument('-o', '--outprefix', help='Prefix to use on output files', required=True)

	args = parser.parse_args()
	INFASTA = args.ifasta
	BLASTP = args.blastp
	PREFIX = args.outprefix
	
	return INFASTA, BLASTP, PREFIX
#	return INFASTA, PREFIX
INFASTA, BLASTP, PREFIX = get_args()
#INFASTA, PREFIX = get_args()

print("Input fasta = " + INFASTA + ".")
print("Input blastp = " + BLASTP + ".")
print("The prefix = " + PREFIX + ".")

HITS=[]
NOHITS=[]
HITS_FILE = open(PREFIX + '.hits.fas', 'w')
NOHITS_FILE = open(PREFIX + '.nohits.fas', 'w')

hitcount = 0
nohitcount = 0

for RECORD in SeqIO.parse(INFASTA, 'fasta'):
	if RECORD.id in open(BLASTP).read():
		hitcount = hitcount+1
		SeqIO.write(RECORD, HITS_FILE, 'fasta')
	else: 
		nohitcount = nohitcount+1
		SeqIO.write(RECORD, NOHITS_FILE, 'fasta')

HITS_FILE.close()
NOHITS_FILE.close()

print("hitcount = " + str(hitcount))
print("nohitcount = " + str(nohitcount))


	


