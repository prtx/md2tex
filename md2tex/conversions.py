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
