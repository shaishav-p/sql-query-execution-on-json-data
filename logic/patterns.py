BASE_PATTERN = r"""SELECT\s+(?P<columns>[\w\s\*,]+)\s+FROM\s+(?P<table>\w+)"""

WHERE_PATTERN = r"""\s+WHERE\s+(?P<conditions>[\w\s\'\"\=\!\<\>\(\)]+)"""
LIMIT_PATTERN = r"""\s+LIMIT\s+(?P<limit>\d+)"""

CONDITION_PATTERN = r"""(?P<column>\w+)\s*(?P<operator>[\=\!\<\>]{1,2}|AND|OR)\s*(?P<value>\d+|\'\w+\')""" 

END_PATTERN = r"""\s*;{0,1}\s*$"""
