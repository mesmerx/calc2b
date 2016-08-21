from django import template
from django.conf import settings
import os
register = template.Library()

def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()


@register.filter
def html(value):
    new_value=value.replace("[intro]","<div style='margin-top:60px;'>")
    new_value=new_value.replace("[/intro]","</div>")
    new_value=new_value.replace("[titulo]","<h3>")
    new_value=new_value.replace("[/titulo]","</h3>")
    new_value=new_value.replace("[texto]","<p><pre>")
    new_value=new_value.replace("[/texto]","</p></pre>")
    new_value=new_value.replace("[caixac]",'<div class="codeheader" id="codeheader_html"></div> <div id="codebox"><pre><code data-language="html"><p> ')
    new_value=new_value.replace("[/caixac]","</p></code></pre></div>")
    new_value=new_value.replace("[img]",'<img src="')
    new_value=new_value.replace("[/img]",'" />')
    new_value=new_value.replace("[codigo]","<code>")
    new_value=new_value.replace("[/codigo]","</code>")
    return new_value

@register.filter
def ler(f):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, f)
    file_path = file_path.replace("templatetags", "templates/polls")
    txt=open(file_path)
    texto=txt.read()
    return texto
