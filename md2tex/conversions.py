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
    :return: corresponding LaTeX codes
    :rtype: str
    """

    md_image_caption_codes = re.findall(r"!\[alt text\]\(.*?\".*?\".*?\)", md, re.M)
    for md_code in md_image_caption_codes:
        image, caption = re.findall(
            r"!\[alt text\]\((.*?)\"(.*?)\".*?\)", md_code, re.M
        )[0]
        tex_code = (
            "\\begin{figure}\n\\centering\n\\includegraphics[width=\\textwidth]{"
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
            "\\begin{figure}\n\\centering\n\\includegraphics[width=\\textwidth]{"
            + image.strip()
            + "}\n\\end{figure}"
        )
        md = md.replace(md_code, tex_code)

    return md


def convert_links(md):
    """
    Convert markdown links to LaTeX code

    :param md: markdown text
    :type md: str
    :return: corresponding LaTeX codes
    :rtype: str
    """

    md_link_codes = re.findall(r"\[.*?\]\(.*?\)", md, re.M)
    for md_code in md_link_codes:
        label, link = re.findall(r"\[(.*?)\]\((.*?)\)", md_code, re.M)[0]
        tex_code = "\\href{" + link + "}{" + label + "}"
        md = md.replace(md_code, tex_code)

    return md


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


def convert_lists(md, tab_level=0):
    """
    Convert markdown lists to LaTeX code. Works recursively to convert lists on current indent level.

    :param md: markdown text
    :type md: str
    :param tab_level: track indentation currently working on
    :type tab_level: int
    :return: corresponding LaTeX codes
    :rtype: str
    """

    # list all unordered list codes for current indent level
    MD_UNORDERED_REGEX = (
        r"^\t{"
        + str(tab_level)
        + r"}[\*\-\+] .+(?:\n^\t{"
        + str(tab_level)
        + r",}(?:[\*\-\+]|[0-9]+\.) .+)*"
    )
    md_unordered_list_codes = re.findall(MD_UNORDERED_REGEX, md, re.M)
    for md_code in md_unordered_list_codes:
        # add itemize begin/end block
        tex_code = r"\begin{itemize}" + "\n" + md_code + "\n" + r"\end{itemize}"
        md = md.replace(md_code, tex_code)

        # convert each element of list for current indent level
        md_item_codes = re.findall(
            r"^\t{" + str(tab_level) + r"}[\*\-\+] .*$", md_code, re.M
        )
        for md_code in md_item_codes:
            item = re.findall(
                r"^\t{" + str(tab_level) + r"}[\*\-\+] (.*)$", md_code, re.M
            )[0]
            tex_code = "    " * (tab_level + 1) + "\\item " + item
            md = md.replace(md_code, tex_code)

    # ordered list conversion works similar to unordered list conversion
    MD_ORDERED_REGEX = (
        r"^\t{"
        + str(tab_level)
        + r"}[0-9]+\. .+(?:\n^\t{"
        + str(tab_level)
        + r",}(?:[\*\+\-]|[0-9]+\.) .+)*"
    )
    md_ordered_list_codes = re.findall(MD_ORDERED_REGEX, md, re.M)
    for md_code in md_ordered_list_codes:
        tex_code = r"\begin{enumerate}" + "\n" + md_code + "\n" + r"\end{enumerate}"
        md = md.replace(md_code, tex_code)

        md_item_codes = re.findall(
            r"^\t{" + str(tab_level) + r"}[0-9]+\. .*$", md_code, re.M
        )
        for md_code in md_item_codes:
            item = re.findall(
                r"^\t{" + str(tab_level) + r"}[0-9]+\. (.*)$", md_code, re.M
            )[0]
            tex_code = "    " * (tab_level + 1) + "\\item " + item
            md = md.replace(md_code, tex_code)

    if md_unordered_list_codes or md_ordered_list_codes:
        md = convert_lists(md, tab_level + 1)

    return md
