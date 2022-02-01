import os
import glob
import json
import pandas as pd
from datetime import datetime

os.chdir(".")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
logf = open("CombineService.log", "w")

Combinedframe = pd.DataFrame()
Counter = 1
for file in all_filenames:
    try:
        metadata = ','.join(pd.read_csv(file, nrows=0).columns)
        metadata = json.loads(metadata)
        sequences = pd.read_csv(file, header=1)
        OAS_info = pd.DataFrame.from_dict(metadata, orient="index").T
        Combinedframe = pd.concat([OAS_info, Combinedframe], axis=0)
        sequences_filtered = pd.DataFrame(sequences['sequence_alignment_aa'])
        sequences_filtered.loc[:, 'Species'] = str(OAS_info['Species'][0])
        sequences_filtered['Chain'] = file.split("_")[1]
        sequences_filtered['Isotype'] = file.split("_")[2].split(".")[0]
        sequences_filtered.to_csv(file, header=True)
        logf.write("File {0} finished at: {1}\n".format(file, str(datetime.now())))
        print("File " + str(Counter) + " Finished out of " + str(len(all_filenames)))
        Counter = Counter + 1
    except Exception as e:
        logf.write("Failed at {0}: {1}\n".format(file, str(e)))
    finally:
        pass

Combinedframe.to_csv('Combined_OAS_Stats.csv', index=None, header=True)