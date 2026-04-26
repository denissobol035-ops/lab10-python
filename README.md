# Report Tool CLI

## Description
A command-line tool for processing numeric data and generating reports.

## Arguments

--input <file>     Input file with numbers  
--out <file>       Output file  
--format           text | json  
--log-level        DEBUG | INFO | WARNING | ERROR  

## Examples

python -m report_tool --input data.txt --out report.txt --format text --log-level INFO

python -m report_tool --input data.txt --out report.json --format json --log-level WARNING

## Output formats

text:
Human-readable report

json:
Structured data with statistics


## Example

Create a file data.txt with content:

1, 2; 3  4.5

Run:

python -m report_tool --input data.txt --out result.txt --format text --log-level INFO
