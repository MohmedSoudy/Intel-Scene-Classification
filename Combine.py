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
for file in all_filenames:
    try:
        metadata = ','.join(pd.read_csv(file, nrows=0).columns)
        metadata = json.loads(metadata)
        OAS_info = pd.DataFrame.from_dict(metadata, orient="index").T
        Combinedframe = pd.concat([OAS_info, Combinedframe], axis=0)
        logf.write("File {0} finished at: {1}\n".format(file, str(datetime.now())))
    except Exception as e:
        logf.write("Failed at {0}: {1}\n".format(file, str(e)))
    finally:
        pass

Combinedframe.to_csv('Combined_OAS_Stats.csv', index=None, header=True)
