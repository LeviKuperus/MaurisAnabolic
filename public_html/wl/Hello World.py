s = """\
<html><body>
<h2>Hello %s!</h2>
</body></html>
"""

def index():
   return s % 'World'
   
def everybody():
   return s % 'everybody'