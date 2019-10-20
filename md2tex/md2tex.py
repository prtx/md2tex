import os

import yaml
from jinja2 import Template

from md2tex import conversions

PATH = os.path.dirname(os.path.abspath(__file__))
DOCUMENT_TYPES = {"article": PATH + "/templates/article.jinja"}


def convert_md2tex(md):
    """
    Convert markdown to LaTeX
    :param md: markdown file content
    :type md: str
    :return: corresponding LaTeX codes
    :rtype: str
    """
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
    """
    Convert markdown file to tex file
    :param md_file: markdown file path
    :type md_file: str
    :param config_file: yaml config file path
    :type config_file: str
    :param tex_file: LaTeX file path
    :type tex_file: str
    """
    config = yaml.load(open(config_file), Loader=yaml.FullLoader)

    document_type = config.get("document_type", "").lower()
    if document_type not in DOCUMENT_TYPES:
        raise Exception("Invalid document type.")
    with open(DOCUMENT_TYPES[document_type]) as template_fp:
        template = Template(template_fp.read())

    with open(md_file) as md_fp:
        md = md_fp.read()
    tex = convert_md2tex(md)

    with open(tex_file, "w") as tex_fp:
        tex_fp.write(template.render(**config, body=tex))


def generate_pdf(tex_file):
    """
    Generate pdf from TeX file.

    :param tex_file: name of document
    :type tex_file: str
    """

    os.system("pdflatex {}".format(tex_file))
