from django import template
from django.conf import settings
import os
import re
register = template.Library()
from django.contrib.sites.shortcuts import get_current_site
def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()


@register.filter
def html(value):
    new_value=value.replace("[intro]","<div style='margin-top:60px;'>")
    new_value=new_value.replace("[/intro]","</div>")
    matchl=re.findall(r'.*link="(.*?)".*](.*)\[',value)
    new_value=re.sub('\[*link=".*\[\\\link]','<a href="{0}">{1}</a>'.format(matchl[0][0],matchl[0][1]),value)
    new_value=new_value.replace("[titulo]","<h3>")
    new_value=new_value.replace("[/titulo]","</h3>")
    new_value=new_value.replace("[texto]","<div><pre><p>")
    new_value=new_value.replace("[/texto]","</p></pre></div>")
    new_value=new_value.replace("[caixac]",'<div class="codeheader" id="codeheader_html"></div> <div id="codebox"><pre><code data-language="html"><p> ')
    new_value=new_value.replace("[/caixac]","</p></code></pre></div>")
    new_value=new_value.replace("[img]",'<img src="')
    new_value=new_value.replace("[/img]",'" />')
    new_value=new_value.replace("[codigo]","<code>")
    new_value=new_value.replace("[/codigo]","</code>")
    new_value=new_value.replace("[site]",get_current_site(None).domain)
    return new_value

@register.filter
def ler(f):
    file2=f.split(":")
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, file2[0])
    file_path = file_path.replace("templatetags", "templates/polls")
    txt=open(file_path)
    texto=txt.read()
    return texto
