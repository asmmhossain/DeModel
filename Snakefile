rule muscle:
    input:
        "examples/Vill_01_pol.fas"
        
    output:
        "examples/Vill_01_pol.muscle"
    log: 
        "examples/muscle.log"
    shell:
        "muscle -in {input} -out {output}"
        
rule makephylip:
    input: 
        "examples/Vill_01_pol.muscle"
    output:
        "examples/input.phy"
    run:
        from Bio import SeqIO
        SeqIO.convert(input[0],'fasta',output[0],'phylip-relaxed')
        
rule examlParser:
    input:
        "examples/input.phy"
    params:
        prefix = "input"
    output:
        "input.binary",
        temp("RAxML_info.input")
    shell:
        "~/Downloads/ExaML/parser/parse-examl -s {input} -m DNA -n {params.prefix}"

        
rule parsimonyTree:
    input:
        "examples/input.phy"
    output:
        "RAxML_parsimonyTree.startTree",
        temp("RAxML_info.startTree")
    params:
        prefix = "startTree"
    shell:
        "~/Downloads/RAxML/raxmlHPC-SSE3 -y -m GTRCAT -p 12345 -s {input} -n {params.prefix}"
        
rule examlTree:
    input:
        "input.binary",
        "RAxML_parsimonyTree.startTree"
    params:
        prefix = "outTree"
    output:
        "ExaML_result.outTree"
    shell:
        "~/Downloads/ExaML/examl/examl -a -B 10 -D -m GAMMA -n {params.prefix} -s {input[0]} -t {input[1]}"    

