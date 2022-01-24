import os
from glob import glob
import json
import pandas as pd
from datetime import datetime

def Ensure_alphapet(Sequence):
    """Check for sequence alphabets
    :param Sequence: Nucleotide sequence or protein sequence
    :return string whether the input sequence is DNA or protein"""
    if "A" in Sequence and "C" in Sequence and "G" in Sequence and "T" in Sequence:
        return "NucleotideAlphabet()"
    else:
        return "ProteinAlphabet()"

def Write_fasta(file_name, ID, Seq):
    """ Write Sequence to fasta file
    :param file_name: Full path to fasta file
    :param Seq: Sequence to be written to file
    :param ID: Accession of sequence
    :return:
    """
    ofile = open(file_name, "a")
    ofile.write(">" + ID + "\n" + Seq + "\n")
    ofile.close()

def Process_DF(DF):
    for i in range(1, len(DF.axes[0])):
        if DF['alphabet'][i] == "NucleotideAlphabet()":
            Write_fasta("Patents_DNA.fasta", DF['id'][i], DF['sequence'][i])
        else:
            Write_fasta("Patents_Protein.fasta", DF['id'][i], DF['sequence'][i])

def JSON_TO_CSV(file_name):
    """
    Convert JSON file to dataframe and write it to a CSV file
    :param file_name: path to json file
    :return: dataframe to be processed
    """
    json_file = open(file_name)
    json_obj = json.load(json_file)
    df = pd.json_normalize(json_obj['sequences'])
    patent_id = file_name.split("_")[1]
    df['id'] = df['id'].astype(str) + "_" + patent_id
    df["sequence"] = df["sequence"].str.upper()
    File_outname = os.path.splitext(file_name)[0] + ".csv"
    df = df.iloc[1:, :]
    df['alphabet'] = df['sequence'].apply(Ensure_alphapet)
    df.to_csv(File_outname, sep=',', encoding='utf-8')
    return (df)

if __name__ == '__main__':
    NumberOfFiles = len(glob('./*.json'))
    Counter = 1
    logf = open("Service.log", "w")
    for file_name in glob('./*.json'):
        try:
            DF = JSON_TO_CSV(file_name)
            Process_DF(DF)
            print(Counter, "Finished out of", NumberOfFiles)
            Counter = Counter + 1
            logf.write("File {0} finished at: {1}\n".format(file_name, str(datetime.now())))
        except Exception as e:
            logf.write("Failed at {0}: {1}\n".format(file_name, str(e)))
        finally:
            pass