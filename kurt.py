import json
import gzip
import sys

hej=[]
for line in gzip.open(sys.argv[2]):
        hej.append(line)

json_in="".join(hej)
nirvana_in= json.loads(json_in)


overlap_lim=0.7
annotations=[]
for var in nirvana_in["positions"]:
        if not "svEnd" in var:
                continue

        #for entry in var:
                #print entry
        dgv=0
	dgv_sm=0
        if "dgv" in var:
                for dgv_var in var["dgv"]:
                        #print dgv_var
                        if not "variantFreqAll" in dgv_var or not "reciprocalOverlap" in dgv_var:
                                continue
                        if dgv_var["sampleSize"] < 100:
                                continue

                        if dgv_var["reciprocalOverlap"] > overlap_lim:
                                dgv=dgv_var["variantFreqAll"]
                                dgv_sm=dgv_var["sampleSize"]
        kg=0
	if "oneKg" in var:
                for kg_var in  var["oneKg"]:
                        if not "reciprocalOverlap" in kg_var:
                                continue
                        if kg_var["reciprocalOverlap"] < overlap_lim:
                                continue
                        if kg_var["variantFreqAll"] > kg:
                                kg=kg_var["variantFreqAll"]
                                #print kg_var


        annotations.append("AF_DGV={};AF_kg={}".format(dgv,kg) )

i=0
for line in open(sys.argv[1]):
        if line[0] == "#":
                if line[1] == "#":
                        print line.strip()
                else:
                     	print line.strip()
                continue

        if "SVTYPE=BND;" in line or "SVTYPE=INV" in line:
                continue


        content=line.strip().split()
        content[7]+=";"+annotations[i]
        i+=1


	print "\t".join(content)
