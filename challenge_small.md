Given an array of flat JSON objects, allow SQL querying it. You only need to support `SELECT (comma separated list of cols or \*) FROM TABLE WHERE (conditions) LIMIT (integer);`. No group by, join, subqueries etc. You may use any programming language.

Example Input:
```
[{ state: 'California', region: 'West', pop: 2312312321, pop_male: 3123123, pop_female: 123123 }, ...]
```

Examples:
```
SELECT state FROM table WHERE pop > 1000000 AND state != 'California';
SELECT * FROM table WHERE pop > 1000000000 OR (pop > 1000000 AND region = 'Midwest');
SELECT * FROM table WHERE pop_male > pop_female;
```

- Only need to support binary conditions `=`, `!=`, `<`, `>`, `AND`, `OR`, parentheses, and literals. Greater than/less than only need to work for numbers
- All JSON objects should have the same keys and only string/number vals, no nulls, arrays, nested objects, etc.
- Can fail inelegantly on runtime on empty array, unknown column/key, parse errors, type mismatch, column names with reserved keyword, etc. Not trying to trick you with edge cases, focus on the core flow.
- Serve as a command line binary with the JSON file as the input. Take the SQL queries as a line on standard input, print the result in any format to standard output.
- Submit either a repository or a single file.
- Write the parser and executor yourself, don't use existing SQL parsers/libraries.
- If you use Haskell, I recommend using aeson for JSON parsing and either attoparsec or megaparsec for the SQL parsing. `ts_parsec` for JS/TS is good, most languages in general should have some decent parsing library.

Criteria for quality:
- Correctness on valid queries
- Graceful failure on invalid queries -- do not crash or fail silently to the user given valid initial inputs
- General code structure and taste.
- No excessive optimizations, difficult to read function chaining, etc.