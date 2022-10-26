#!/usr/bin/python3
from string import Template

list = ["2", "3"]
'''
=HYPERLINK("[Book1.xlsx]January!A10","Go to January > A10")

To jump to a different location in the current worksheet, include both the workbook name, and worksheet name like this, 
where January is another worksheet in the workbook.
'''
dataTemp = Template('=HYPERLINK("[Excel文件名.xlsx]Excel文件中工作表名!A${index}","${ele}")')

for index, item in enumerate(list):
    print(dataTemp.substitute(index=(index + 2), ele=item))
