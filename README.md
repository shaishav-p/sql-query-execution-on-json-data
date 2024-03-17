# SQL Query Execution on JSON Data

## Description
This Python project allows SQL querying on an array of flat JSON objects. It supports `SELECT (comma separated list of cols or *) FROM table WHERE (conditions) LIMIT (integer);` queries. Currently, the project does not support group by, join, subqueries etc.

## Installation
1. Clone the repository to your local machine using `git clone <repository_link>`.
2. Navigate to the project directory using `cd <project_directory>`.
3. Install the required dependencies using `pip install -r requirements.txt`.

## Usage
To use this project, follow these steps:
1. Open the project in your preferred IDE.
2. Run the `main.py` file to start the application by using the `python3 main.py` or `python main.py` (depending on which python version you have installed - python 3.x or higher is recommended).
3. Enter your SQL queries in the prompt that appears 
   a. Note: semicolons at the end of the query have been made optional as we are executing the queries one at a time.

## Example Queries
Here are some example queries you can run using this project:
1. `SELECT state FROM table WHERE pop > 1000000 AND state != 'California';`
2. `SELECT * FROM table WHERE pop > 1000000000 OR (pop > 1000000 AND region = 'Midwest');`
3. `SELECT * FROM table WHERE pop_male > pop_female;`
4. `SELECT state, region  FROM table WHERE pop > 1000000000 OR (pop > 1000000 AND (region = 'Midwest' AND pop_female != 6368139)) OR pop = 5093253`
5. `SELECT state, region  FROM table WHERE pop > 1000000000 OR (pop > 1000000 AND (region = 'Midwest' AND pop_female != 6368139)) OR pop = 5093253 LIMIT 7;`
6. `SELECT state, region  FROM table WHERE pop > 1000000000 OR (pop > 1000000 AND (region = 'Midwest' AND pop_female != 6368139)) OR p = 46`
7. `SELECT * FROM table WH`
8. `SELECT * FROM table WHERE`
9. `SELECT * FROM table WHERE stat = "Ohio"`
10. `SELECT * FROM table WHERE state = "Ohio"`
11. `SELECT * FROM table WHERE state = 20`

## Limitations
- Only binary conditions `=`, `!=`, `<`, `>`, `AND`, `OR`, parentheses, and literals are supported. 
- All JSON objects should have the same keys and only string/number vals, no nulls, arrays, nested objects, etc.
- The program can fail on runtime on certain edge case parse errors, column names with reserved keyword, etc.

## Data Input
The program uses a JSON file as the data input. The JSON file should be an array of flat JSON objects. The path to the JSON file is currently hardcoded in the `main.py` file.

## Future Enhancements
- A feature can be added where the user can specify multiple file paths to relevant tables that we can run the SQL queries against
- Support more SQL keywords (e.g. GROUP BY, ORDER BY, etc.)


