import json
from typing import List, Dict

# load tables from multiple tables
def loadDataFromTables(filePaths: List[str]) -> List[Dict]:
    data = []
    
    for filePath in filePaths:
        file = open(filePath, 'r')
        
        # we combine data from each file into a single list/rows of data
        data.extend(json.load(file))

        file.close()

    return data

# in the future, we can add more functions to interact with the databases (such as writes, updates)
