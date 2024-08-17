def parseStyle(dictionary):
    bodystyle = ""
    stylei = 0

    for style in dictionary:
        stylei+=1
        bodystyle += f"; " if stylei>1 else ''
        bodystyle += f"{style}: {dictionary[style]}"

    return bodystyle

def parseCfg(dictionary):
    cfgstyle = ""
    cfgi = 0

    for style in dictionary:
        cfgi += 1
        cfgstyle += f"{style}={dictionary[style]}"
        cfgstyle += " " if not cfgi>1 else ''

    return cfgstyle


class Pytml:
    def __init__(self, project="Project.html", 
                 title="Homepage",
                 background="#000000",
                 custom_style={},
                 extra_config={},
                 css=""):
        
        self.project = project
        self.title = title
        self.background = background
        self.bodystyle = parseStyle(custom_style)
        self.extraconfig = parseCfg(extra_config)
        self.lli_body = 8 # Last Line Index

        with open(project, "w+") as pytmlp:
            pytmlp.write(f"""
<!DOCTYPE html>
</html>
    <head>
        <title>{title}</title>
        {f'<link rel="stylesheet" href="{css}">' if css else ''}

        </pytml>
    </head>

    <body style="{self.bodystyle}; background: {background}" {self.extraconfig}>
""")

    def StartDiv(self, _class="", _id="",
                 custom_style={},
                 extra_config={}):
        
        self.lli_body += 4

        style = parseStyle(custom_style)
        cfg = parseCfg(extra_config)

        with open(self.project, "a+") as pytmlp:
            ln = f"{' '*(self.lli_body-4)}<div"
            ln += f" class='{_class}'" if _class else ''
            ln += f" id='{_id}'" if _id else ''
            ln += f" style=\"{style}\"" if style else ''
            ln += f" {cfg}" if cfg else ''
            ln += ">\n"

            pytmlp.write(ln)

    def CloseDiv(self):
        self.lli_body -= 4

        with open(self.project, "a+") as pytmlp:
            pytmlp.write(f"{' '*self.lli_body}</div>\n")

    def Header(self, text="Header", 
               size=1, 
               color="red",
               background="black", 
               font_family="Courier New", 
               custom_style={},
               extra_config={}):
        
        if size > 6: print("WARNING - Pytml: Header size cannot be over 6. Reverting to 6."); size=6

        style = parseStyle(custom_style)
        cfg = parseCfg(extra_config)

        with open(self.project, "a+") as pytmlp:
            ln = f"{' '*self.lli_body}<h{size}"
            ln += f" style=\"{style}\"" if style else ''
            ln += f" {extra_config}" if cfg else ''
            ln += f">{text}</h{size}>\n"

            pytmlp.write(ln)
    
    def Close(self):
        with open(self.project, "a+") as pytmlp:
            pytmlp.write("""
    </body>
</html>
""")
            
html = Pytml(custom_style={"color": "white", "position": "relative"}, css="style.css")

html.StartDiv(_class="maindiv", custom_style={"color": "green"})
html.Header("i love u life", size=2)
html.CloseDiv()

html.Close()