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
