from typing import Dict, List, Union
from util.errors import InvalidQueryError
import logging
import copy

log = logging.getLogger(__name__)

def evaluateCondition(condition: List[Union[str, int]], row: Dict[str, Union[str, int]], columns: set[str]) -> bool:
    # ex. pop > 1000000000

    if len(condition) != 3:
        raise InvalidQueryError("Invalid condition: " + condition)
    
    column = condition[0]
    operator = condition[1]
    columnOrValue = condition[2] # can be a literal(str/num) or a column name

    if column not in row:
        return False
    
    if column != columnOrValue and columnOrValue in row.keys():
        if columnOrValue not in row:
            return False
        columnOrValue = row[columnOrValue]

    
    if operator == "=":
        return row[column] == columnOrValue
    elif operator == "!=":
        return row[column] != columnOrValue
    elif operator == "<":
        return row[column] < columnOrValue
    elif operator == ">":
        return row[column] > columnOrValue
    else:
        raise InvalidQueryError("Invalid operator: " + operator)


def evaluateBooleanExpression(operand1: bool, operator: str, operand2: bool) -> bool:
    if operator == "AND":
        return operand1 and operand2
    elif operator == "OR":
        return operand1 or operand2
    else:
        raise InvalidQueryError("Invalid operator: " + operator)


def validRow(row: Dict[str, Union[str, int]], conditions: List[Union[str, int]], columns: set[str]) -> bool:
    # ex. pop > 1000000000 OR (pop > 1000000 AND region = 'Midwest')
    if conditions == None or len(conditions) == 0:
        return True
    
    curr = True
    result = True
    operator = "AND"
    columnExpression = []
    stack = []

    for i in range(len(conditions)):
        c = conditions[i]

        if c in ["AND", "OR"]:
            if len(columnExpression) > 0:
                conditionResult = evaluateCondition(columnExpression, row, columns)
                columnExpression = []
                result = evaluateBooleanExpression(result, operator, conditionResult)
            
            operator = c

        elif c == "(":
            stack.append(result)
            stack.append(operator)
            result = True
            operator = "AND"
        
        elif c == ")":
            if len(columnExpression) > 0:
                conditionResult = evaluateCondition(columnExpression, row, columns)
                columnExpression = []
                result = evaluateBooleanExpression(result, operator, conditionResult)
                
            oldOperator = stack.pop()
            oldResult = stack.pop()
            result = evaluateBooleanExpression(oldResult, oldOperator, result)
            operator = "AND"
            
        else:
            columnExpression.append(c)

    if len(columnExpression) > 0:
        conditionResult = evaluateCondition(columnExpression, row, columns)
        result = evaluateBooleanExpression(result, operator, conditionResult)

    return result


def filterColumns(row: Dict[str, Union[str, int]], columnsToKeep: set[str]) -> Dict[str, Union[str, int]]:
    if list(columnsToKeep)[0] == "*":
        return row
    
    filteredRow = {col: row[col] for col in columnsToKeep}
    return filteredRow


def executeQuery(data: List[Dict[str, Union[str, int]]], columns: set[str], conditions: List[Union[str, int]], limit: int) -> List[Dict[str, Union[str, int]]]:
    validData = []

    for row in data:
        isValidRow = validRow(row, conditions, columns)
        log.debug("isValidRow: %s %s", isValidRow, row)

        if isValidRow:
            validData.append(filterColumns(row, columns))

        if limit and len(validData) == limit:
            break
    
    return validData
