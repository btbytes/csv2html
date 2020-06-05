# csv2html
A script to convert a CSV file to HTML file with some options

```
$ ./csv2html.py -h
usage: csv2html.py [-h] [--delimiter DELIMITER] [--quotechar QUOTECHAR]
                   [--title TITLE] [--caption CAPTION] [--header]
                   csvfile

CSV to HTML converter.

positional arguments:
  csvfile

optional arguments:
  -h, --help            show this help message and exit
  --delimiter DELIMITER
                        Field delimiter. Default is , .
  --quotechar QUOTECHAR
                        Quote Character. Deault is nothing
  --title TITLE         Page title. Will be printed in h1 tag.
  --caption CAPTION     Table caption.
  --header              data has header. First row will be "th".
```
