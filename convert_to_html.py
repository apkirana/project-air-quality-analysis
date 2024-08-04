import nbconvert
import nbformat

with open('air_quality.ipynb') as f:
    notebook_content = nbformat.read(f, as_version=4)

html_exporter = nbconvert.HTMLExporter()
html_exporter.template_name = 'classic'

(body, resources) = html_exporter.from_notebook_node(notebook_content)

with open('air_quality.html', 'w') as f:
    f.write(body)


    #bash : python convert_to_html.py