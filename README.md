# KURT
extract annotation from the illumina Nirvana tool

python kurt.py in.vcf nirvana.json.gz > out.vcf

thousand genome and dgv frequencies are added to the out.vcf file.

NOTE: kurt will only print CNVs (DUP or DEL) to the output file
