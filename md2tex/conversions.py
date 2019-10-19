"""
Contains all functions to convert markdown codes to LaTeX.
"""

import re


def convert_headers(md):
    """
    Convert header tags (#, ##...) to LaTeX section, subsections.

    :param md: markdown text
    :type md: str
    :return: corresponding LaTeX codes
    :rtype: str
    """

    header_dict = [
        {
            "name": "subparagraph",
            "match_regex": r"^#####[^#].*",
            "replace_regex": r"##### (.*)",
        },
        {
            "name": "paragraph",
            "match_regex": r"^####[^#].*",
            "replace_regex": r"#### (.*)",
        },
        {
            "name": "subsubsection",
            "match_regex": r"^###[^#].*",
            "replace_regex": r"### (.*)",
        },
        {
            "name": "subsection",
            "match_regex": r"^##[^#].*",
            "replace_regex": r"## (.*)",
        },
        {"name": "section", "match_regex": r"^#[^#].*", "replace_regex": r"# (.*)"},
    ]
    for header in header_dict:
        for md_code in re.findall(header["match_regex"], md, re.M):
            tex_code = (
                "\\"
                + header["name"]
                + "{"
                + re.findall(header["replace_regex"], md_code, re.M)[0]
                + "}"
            )
            md = md.replace(md_code, tex_code)

    return md


def convert_bold(md):

    """
    Convert bold tags (**, __) to LaTeX textbf

    :param md: markdown text
    :type md: str
    :return: corresponding LaTeX codes
    :rtype: str
    """

    for md_code in re.findall(r"\*\*.*?\*\*", md, re.M):
        tex_code = "\\textbf{" + re.findall(r"\*\*(.*?)\*\*", md_code, re.M)[0] + "}"
        md = md.replace(md_code, tex_code)

    for md_code in re.findall(r"__.*?__", md, re.M):
        tex_code = "\\textbf{" + re.findall(r"__(.*?)__", md_code, re.M)[0] + "}"
        md = md.replace(md_code, tex_code)

    return md


def convert_italics(md):

    """
    Convert bold tags (*, _) to LaTeX textit

    :param md: markdown text
    :type md: str
    :return: corresponding LaTeX codes
    :rtype: str
    """

    for md_code in re.findall(r"\*.*?\*", md, re.M):
        tex_code = "\\textit{" + re.findall(r"\*(.*?)\*", md_code, re.M)[0] + "}"
        md = md.replace(md_code, tex_code)

    for md_code in re.findall(r"_.*?_", md, re.M):
        tex_code = "\\textit{" + re.findall(r"_(.*?)_", md_code, re.M)[0] + "}"
        md = md.replace(md_code, tex_code)

    return md


def convert_images(md):

    """
    Convert image tags to LaTeX codes

    :param md: markdown text
    :type md: str
    :return: corresponding LaTeX codes, has image
    :rtype: (str, bool)
    """

    md_image_caption_codes = re.findall(r"!\[alt text\]\(.*?\".*?\".*?\)", md, re.M)
    for md_code in md_image_caption_codes:
        image, caption = re.findall(
            r"!\[alt text\]\((.*?)\"(.*?)\".*?\)", md_code, re.M
        )[0]
        tex_code = (
            "\\begin{figure}[p]\n\\centering\n\\includegraphics{"
            + image.strip()
            + "}\n\\caption{"
            + caption.strip()
            + "}\n\\end{figure}"
        )
        md = md.replace(md_code, tex_code)

    md_image_codes = re.findall(r"!\[alt text\]\(.*?\)", md, re.M)
    for md_code in md_image_codes:
        image = re.findall(r"!\[alt text\]\((.*?)\)", md_code, re.M)[0]
        tex_code = (
            "\\begin{figure}[p]\n\\centering\n\\includegraphics{"
            + image.strip()
            + "}\n\\end{figure}"
        )
        md = md.replace(md_code, tex_code)

    return md, bool(md_image_codes or md_image_caption_codes)


def convert_links(md):
    """
    Convert markdown links to LaTeX code

    :param md: markdown text
    :type md: str
    :return: corresponding LaTeX codes, has links
    :rtype: (str, bool)
    """

    md_link_codes = re.findall(r"\[.*?\]\(.*?\)", md, re.M)
    for md_code in md_link_codes:
        label, link = re.findall(r"\[(.*?)\]\((.*?)\)", md_code, re.M)[0]
        tex_code = "\\href{" + link + "}{" + label + "}"
        md = md.replace(md_code, tex_code)

    return md, bool(md_link_codes)


def convert_table(md):
    """
    Convert markdown tables to LaTeX code

    :param md: markdown text
    :type md: str
    :return: corresponding LaTeX codes
    :rtype: str
    """

    md_table_codes = re.findall(r".*\|.*\n.*\-.*(?:\n.*\|.*)*", md, re.M)
    for md_code in md_table_codes:
        md_rows = re.findall(r"(.*\|.*)", md_code, re.M)
        header = md_rows.pop(0)
        column_count = md_rows.pop(0).count("-")

        tex_code = "\\begin{tabular}{|" + "l|" * column_count + "}\n\\hline\n"
        tex_code += header.strip(" |").replace("|", "&") + " \\\\\n\\hline\n"
        for row in md_rows:
            tex_code += row.strip(" |").replace("|", "&") + " \\\\\n"
        tex_code += "\\hline\n\\end{tabular}"

        md = md.replace(md_code, tex_code)

    return md
