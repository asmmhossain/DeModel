workdir : "examples/"

rule all:
    input:
        "ExaML_result.Vill_01_pol.fas.new.muscle_result_newick_date.txt",
        "ExaML_result.Vill_02_pol.fas.new.muscle_result_newick_date.txt"

'''
rule mapSeqs:
    input:
        "{ds1}_pol.fas",
    output:
        "{ds1}_pol.fas.new",
        "{ds1}_pol.fas.map",
        "{ds1}_pol.fas.nDate"
    shell:
        "python ../mapSeqname.py {input} {input}.dates"
           
rule muscle:
    input:
        "{ds2}.new"
        
    output:
        "{ds2}.new.muscle"
    log: 
        "muscle.log"
    shell:
        "muscle -in {input} -out {output}"

rule makephylip:
    input: 
        "{ds3}.muscle"
    output:
        "{ds3}.muscle.phy"
    shell:
        "python ../fasta2phylip.py {input} {output}"
        
rule examlParser:
    input:
        "{ds4}.phy"
    params:
        prefix = "{ds4}"
    output:
        "{ds4}.binary",
        temp("RAxML_info.{ds4}")
    shell:
        "~/Downloads/ExaML/parser/parse-examl -s {input} -m DNA -n {params.prefix}"


rule parsimonyTree:
    input:
        "{ds5}.phy"
    output:
        "RAxML_parsimonyTree.{ds5}.startTree",
        temp("RAxML_info.{ds5}.startTree")
    params:
        prefix = "{ds5}.startTree"
    shell:
        "~/Downloads/RAxML/raxmlHPC-SSE3 -y -m GTRCAT -p 12345 -s {input} -n {params.prefix}"


rule examlTree:
    input:
        "{ds6}.binary",
        "RAxML_parsimonyTree.{ds6}.startTree"
    params:
        prefix = "{ds6}.outTree"
    output:
        "ExaML_result.{ds6}.outTree"
        
    shell:
        "~/Downloads/ExaML/examl/examl -a -B 10 -D -m GAMMA -n {params.prefix} -s {input[0]} -t {input[1]}; rm ExaML_binaryCheckpoint.*; rm ExaML_info.{params.prefix}; rm ExaML_log.{params.prefix}; rm ExaML_modelFile.{params.prefix}; rm RAxML_10_goodTrees.{params.prefix}"


        
rule lsdDateFile:
    input:
        "{ds7}.nDate"
    output:
        "{ds7}.lsd.dates"
    shell:
        "python ../makeLsdDateFile.py {input} {output}"
        
rule LSD:
    input:
        "ExaML_result.{ds8}.new.muscle.outTree",
        "{ds8}.lsd.dates"
    output:
        "ExaML_result.{ds8}.new.muscle_result.txt",
        "ExaML_result.{ds8}.new.muscle_result_nexus.txt",
        "ExaML_result.{ds8}.new.muscle_result_newick_date.txt",
        "ExaML_result.{ds8}.new.muscle_result_newick_brl.txt"
    shell:
        "~/apps/lsd -i {input[0]} -d {input[1]} -c -r"    
        
'''        
