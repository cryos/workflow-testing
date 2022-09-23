from jinja2 import FileSystemLoader, Environment
import yaml

chaps = {}

with open("chapters.yml", "r") as stream:
  try:
    chaps = yaml.safe_load(stream)
  except yaml.YAMLError as exc:
    print(exc)

templateLoader = FileSystemLoader(searchpath="./")
templateEnv = Environment(loader=templateLoader)
TEMPLATE_FILE = "main.tex.j2"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(chaps)  # this is where to put args to the template renderer
with open("main.tex", "w") as main_file:
  main_file.write(outputText)
