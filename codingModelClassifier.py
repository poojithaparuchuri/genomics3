"""
Problem Set-4
Sree Poojitha Paruchuri
codingModelClassifier.py
"""

import math

#list of codon labels to the coding and non-coding models

modelCodons = ['TTT', 'TTC', 'TTA', 'TTG', 'CTT', 'CTC', 'CTA',
               'CTG', 'ATT', 'ATC', 'ATA', 'ATG', 'GTT', 'GTC',
               'GTA', 'GTG', 'TCT', 'TCC', 'TCA', 'TCG', 'AGT',
               'AGC', 'CCT', 'CCC', 'CCA', 'CCG', 'ACT', 'ACC',
               'ACA', 'ACG', 'GCT', 'GCC', 'GCA', 'GCG', 'TAT',
               'TAC', 'CAT', 'CAC', 'CAA', 'CAG', 'AAT', 'AAC',
               'AAA', 'AAG', 'GAT', 'GAC', 'GAA', 'GAG', 'TGT',
               'TGC', 'CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG',
               'GGT', 'GGC', 'GGA', 'GGG', 'TGG', 'TAA', 'TAG',
               'TGA']

# function to score coding and non-coding models
def scoreModels():
    # loading the probability matrices for coding and non coding models
    codingMatrix = getProbs("./codingModel.tab") #64x64 matrix of probabilities for coding triplet mutations
    noncodingMatrix = getProbs("./noncodingModel.tab")  # 64x64 matrix of probabilities for non-coding triplet mutations

    #reads the ancestor sequences
    id2ancestorSeq = getSeq("./Ancestor.fa")
    id2spaciiSeq = getSeq("./Spacii.fa")

    # the two sequences above share dictionary indexes
    allID = list(id2ancestorSeq.keys())

    # loop over all sequences
    for ID in allID:
        cScore = 0 #variable to contain the score of id2ancestorSeq[ID] and id2spaciiSeq[ID] with the coding model
        nScore = 0  # variable to contain the score of id2ancestorSeq[ID] and id2spaciiSeq[ID] with the non-coding model

        ancestor_sequence = id2ancestorSeq[ID]
        spacii_sequence = id2spaciiSeq[ID]

        # loop over each triplet in the sequences
        for i in range(len(ancestor_sequence) // 3):
            ancestor_codon = ancestor_sequence[i * 3: (i + 1) * 3]
            spacii_codon = spacii_sequence[i * 3: (i + 1) * 3]

            ancestor_index = modelCodons.index(ancestor_codon)
            spacii_index = modelCodons.index(spacii_codon)

            # add logarithm of probabilities to the scores
            cScore += math.log(codingMatrix[ancestor_index][spacii_index])
            nScore += math.log(noncodingMatrix[ancestor_index][spacii_index])

        if cScore >nScore:
            print(f"{ID} is likely coding: {cScore} {nScore}")

        else:
            print(f"{ID} is likely not coding: {cScore} {nScore}")

# function to read Sequences from a file
def getProbs(f1):
    f = open(f1)
    pMatrix = []
    for line in f:
        tmp = line.rstrip().split("\t")
        tmp = [float(i) for i in tmp]
        pMatrix.append(tmp)
    return pMatrix

# function to read sequences from a file
def getSeq(filename):
    f = open(filename)
    id2seq = {}
    currkey = ""
    for line in f:
        if line.find(">") == 0:
            currkey = line[1:].split("|") [0]
            id2seq[currkey] = ""
        else:
            id2seq[currkey] = id2seq[currkey] + line.rstrip()
    f.close()
    return id2seq

# call the function to execute the classification
scoreModels()