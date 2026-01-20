import re
from markupsafe import escape

def clean_form(form):
    cleaned = {}
    for key, value in form.items():
        value = value.strip()
        value = escape(value)
        value = re.sub(r"[<>]", "", value)
        cleaned[key] = value
        
    return cleaned