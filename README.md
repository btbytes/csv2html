# csv2html
A script to convert a CSV file to HTML file with some options.Reads a CSV File and writes the output to the terminal.


Options:

1. Field delimiter
2. Quote character
3. HTML Table caption
4. Page title
5. First row has header information.




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

Example input:

```csv
mpg,cylinders,displacement,horsepower,weight,acceleration,model_year,origin,name
18,8,307,130,3504,12,70,1,chevrolet chevelle malibu
15,8,350,165,3693,11.5,70,1,buick skylark 320
18,8,318,150,3436,11,70,1,plymouth satellite
```

Command: `./csv2html.py example.csv --header --caption "Car MPGs" > example.html`

Output:

```HTML
<!doctype html><head><style type="text/css">
                table {
                  border-collapse: collapse;
                  margin-bottom: 10px;
                }

                td,
                th {
                  padding: 6px;
                  text-align: left;
                }

                thead {
                  border-bottom: 1px solid var(--border);
                }

                tfoot {
                  border-top: 1px solid var(--border);
                }

                tbody tr:nth-child(even) {
                  background-color: var(--background-alt);
                }</style></head><body>
                
<table>
<caption>Car MPGs</caption>
<tr>
<th>mpg</th>
<th>cylinders</th>
<th>displacement</th>
<th>horsepower</th>
<th>weight</th>
<th>acceleration</th>
<th>model_year</th>
<th>origin</th>
<th>name</th>
</tr>
<tr>
<td>18</td>
<td>8</td>
<td>307</td>
<td>130</td>
<td>3504</td>
<td>12</td>
<td>70</td>
<td>1</td>
<td>chevrolet chevelle malibu</td>
</tr>
<tr>
<td>15</td>
<td>8</td>
<td>350</td>
<td>165</td>
<td>3693</td>
<td>11.5</td>
<td>70</td>
<td>1</td>
<td>buick skylark 320</td>
</tr>
<tr>
<td>18</td>
<td>8</td>
<td>318</td>
<td>150</td>
<td>3436</td>
<td>11</td>
<td>70</td>
<td>1</td>
<td>plymouth satellite</td>
</tr>
</table>

```

