import re
import util.constants as constants
from util.errors import InvalidQueryError
import logic.patterns as patterns
from typing import Any, Dict, List, Union
import logging

log = logging.getLogger(__name__)

def getRegexPattern(query: str) -> re.Pattern[Any]:
    regexPatterns = {}

    if constants.SELECT in query and constants.FROM in query:
        regexPatterns[0] = patterns.BASE_PATTERN
    else:
        raise InvalidQueryError("Invalid query: SELECT and FROM keywords are mandatory")

    if constants.WHERE in query:
        indexOfWhere = query.find(constants.WHERE)
        regexPatterns[indexOfWhere] = patterns.WHERE_PATTERN
    
    if constants.LIMIT in query:
        indexOfLimit = query.find(constants.LIMIT)
        regexPatterns[indexOfLimit] = patterns.LIMIT_PATTERN

    # in the future, we can add other patterns here for other SQL keywords (e.g. GROUP BY, ORDER BY, etc.)
    
    sortedPatterns = sorted(regexPatterns.items(), key=lambda x: x[0])
    finalRegexPattern = ""
    for pattern in sortedPatterns:
        finalRegexPattern += pattern[1]
    finalRegexPattern = finalRegexPattern + patterns.END_PATTERN

    finalRegexPattern = re.compile(finalRegexPattern)
    return finalRegexPattern

def parseWhereConditions(conditions: str) -> List[Union[str, int]]:
    conditions = conditions.strip()

    tokens = []
    currentToken = ""

    def checkCurrentToken():
        nonlocal currentToken
        if currentToken != "":
            if currentToken.isnumeric():
                tokens.append(int(currentToken))
            else:
                tokens.append(currentToken)
            currentToken = ""

    for c in conditions:
        if c in " \'":
            checkCurrentToken()
            
        elif c in ["(", ")", "AND", "OR", "=", "!", "<", ">"]:
            checkCurrentToken()
            
            if tokens[-1] == "!":
                if c == "=":
                    tokens[-1] = "!="
                    continue
                else:
                    raise InvalidQueryError("Invalid operator: " + c)
    
            tokens.append(c)
        elif c.isalnum() or c == "_":
            currentToken += c

    checkCurrentToken()


    return tokens

def parseColumns(columns: str) -> List[str]:
    columns = columns.split(",")

    for i in range(len(columns)):
        columns[i] = columns[i].strip()
    
    return columns
        

def parseQuery(query: str) -> Dict[str, Any]:
    if query == None or query == "":
        return None
    
    regexPattern = getRegexPattern(query)
    match = regexPattern.match(query)
    if match == None:
        log.debug("regex pattern: %s %s", regexPattern, constants.NEWLINES)
        raise InvalidQueryError("Invalid query: " + query)

    log.debug("received query from user: %s %s", query, constants.NEWLINES)
    log.debug("matched pattern: %s %s", match.groupdict(), constants.NEWLINES)    
    
    columns = parseColumns(match.groupdict()["columns"])

    parsedConditions, limit = None, None
    if "conditions" in match.groupdict():
        parsedConditions = parseWhereConditions(match.groupdict()["conditions"])
    if "limit" in match.groupdict():
        limit = int(match.groupdict()["limit"]) 
    
    return {
        "columns": columns,
        "table": match.groupdict()["table"],
        "conditions": parsedConditions,
        "limit": limit
    }

    