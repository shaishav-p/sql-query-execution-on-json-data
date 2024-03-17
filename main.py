from typing import List, Dict, Union
from logic.db import loadDataFromTables
from logic.parse import parseQuery
from util.errors import InvalidQueryError
from logic.execute import executeQuery
from util.constants import NEWLINES
import logging
import pprint


log = logging.getLogger(__name__)

def main():
    logging.basicConfig(level=logging.WARN, format="%(levelname)s (%(filename)s)   %(message)s")
    
    # can add a feature in the future where the user can specify the file paths to relevant tables
    data = loadDataFromTables(["./dataSources/db1/table.json"])
    log.debug("data from tables: %s %s", data, NEWLINES)
    
    query = None

    while query != "exit":
        query = input("Enter SQL query: ")
        if query == "exit":
            break
        try:
            result = parseQuery(query)
            log.debug("parsed query: %s %s", result, NEWLINES)                                                             

            output = executeQuery(data, set(result["columns"]), result["conditions"], result["limit"])
            print("\nResult:")
            pprint.pprint(output)
            print()
        except InvalidQueryError as e:
            log.debug(e)
            print(str(e),"\nTry again", NEWLINES)

if __name__ == "__main__":
    main()
