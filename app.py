import json
from jinja2 import Environment, FileSystemLoader


with open("data.json","r") as d:
    data = json.load(d)


fileLoader = FileSystemLoader('templates')
env = Environment(loader=fileLoader)

rendered = env.get_template("temp.html").render(data = data)

#save content in html file

filename = "index.html"

with open("index.html",'w') as f:
    f.write(rendered)




