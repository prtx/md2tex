import os

import yaml
from jinja2 import Template

from md2tex import conversions

PATH = os.path.dirname(os.path.abspath(__file__))
DOCUMENT_TYPES = {
    "article": PATH + "/templates/article.jinja"
}

def convert_md2tex(md):
    temp = md
    temp = conversions.convert_headers(temp)
    temp = conversions.convert_lists(temp)
    temp = conversions.convert_table(temp)
    temp = conversions.convert_images(temp)
    temp = conversions.convert_links(temp)
    temp = conversions.convert_bold(temp)
    temp = conversions.convert_italics(temp)
    tex = temp

    return tex


def convert(md_file, config_file, tex_file):
    config = yaml.load(open(config_file), Loader=yaml.FullLoader)

    document_type = config.get("document_type", "").lower()
    if document_type not in DOCUMENT_TYPES:
        raise Exception("Invalid document type.")
    with open(DOCUMENT_TYPES[document_type]) as f:
        template = Template(f.read())

    with open(md_file) as f:
        md = f.read()
    tex = convert_md2tex(md)

    with open(tex_file, "w") as f:
        f.write(template.render(
            **config,
            body=tex,
        ))


def generate_pdf(tex_file):
	"""
	Generate pdf from TeX file.

	:param tex_file: name of document
	:type tex_file: str
	"""

	os.system("pdflatex {}".format(tex_file))
