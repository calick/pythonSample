# coding: utf-8
import cgi
from string import Template

import cgitb;cgitb.enable()

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# t=Template(open('../template/tmpl.txt').read())
t=Template(open('template/tmpl.html').read())
# t=Template(open('template/tmpl.txt').read())

# body=t.substitute({'title':'The title1','body':'This is body1'})
body=t.substitute(title='The title2',body='This is body2')


# body=t.substitute(title='The title',body='This is body')}

print("Content-type: text/html;charset=utf-8\n")
# print("<html><head><title>aa</title></head><body>body</body></html>")
print(body)