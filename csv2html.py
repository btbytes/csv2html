#!/usr/bin/env python3

import csv


def csv2html(csvfile, delimiter, quotechar, caption, title, header=False):
    print('''<!doctype html><head><style type="text/css">
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
                ''')
    if title:
        print(f'''<h1>{title}</h1>''')
    print('<table>')
    if caption:
        print(f'<caption>{caption}</caption>')
    with open(csvfile, 'r') as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
        for idx, row in enumerate(reader):
            if idx == 0 and header:
                td = 'th'
            else:
                td = 'td'
            print('<tr>')
            for col in row:
                print(f'<{td}>{col}</{td}>')
            print('</tr>')
        print('</table>')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='CSV to HTML converter.')
    parser.add_argument('csvfile')
    parser.add_argument(
        '--delimiter', help='Field delimiter. Default is , .', default=',')
    parser.add_argument(
        '--quotechar', help='Quote Character. Deault is nothing')
    parser.add_argument(
        '--title', help='Page title. Will be printed in h1 tag.')
    parser.add_argument('--caption', help='Table caption.')
    parser.add_argument(
        '--header',
        action='store_true',
        help='data has header. First row will be "th".')
    args = parser.parse_args()
    csv2html(args.csvfile, args.delimiter, args.quotechar,
             args.caption, args.title, args.header)
