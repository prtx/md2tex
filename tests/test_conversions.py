import pytest

from md2tex import conversions


@pytest.mark.parametrize(
    ["md", "tex"],
    [
        ("# Header1", r"\section{Header1}"),
        ("## Header2", r"\subsection{Header2}"),
        ("### Header3", r"\subsubsection{Header3}"),
        ("#### Header4", r"\paragraph{Header4}"),
        ("##### Header5", r"\subparagraph{Header5}"),
    ],
)
def test_convert_header(md, tex):
    assert conversions.convert_headers(md) == tex


@pytest.mark.parametrize(
    ["md", "tex"],
    [
        ("**text**", "\\textbf{text}"),
        ("__text__", "\\textbf{text}"),
        ("**sample text**", "\\textbf{sample text}"),
        ("__sample text__", "\\textbf{sample text}"),
    ],
)
def test_convert_bold(md, tex):
    assert conversions.convert_bold(md) == tex


@pytest.mark.parametrize(
    ["md", "tex"],
    [
        ("*text*", "\\textit{text}"),
        ("_text_", "\\textit{text}"),
        ("*sample text*", "\\textit{sample text}"),
        ("_sample text_", "\\textit{sample text}"),
    ],
)
def test_convert_italics(md, tex):
    assert conversions.convert_italics(md) == tex


@pytest.mark.parametrize(
    ["md", "tex", "has_image"],
    [
        (
            "![alt text](sample.jpeg)",
            "\\begin{figure}[p]\n\\centering\n\\includegraphics{sample.jpeg}\n\\end{figure}",
            True,
        ),
        (
            '![alt text](sample.jpeg "Caption")',
            "\\begin{figure}[p]\n\\centering\n\\includegraphics{sample.jpeg}\n\\caption{Caption}\n\\end{figure}",
            True,
        ),
        ("Test", "Test", False),
    ],
)
def test_convert_images(md, tex, has_image):
    actual_tex, actual_has_image = conversions.convert_images(md)
    assert actual_tex == tex
    assert actual_has_image == has_image


@pytest.mark.parametrize(
    ["md", "tex", "has_link"],
    [
        (
            "[Sample link](https://www.google.com)",
            "\\href{https://www.google.com}{Sample link}",
            True,
        ),
        ("Test", "Test", False),
    ],
)
def test_convert_links(md, tex, has_link):
    actual_tex, actual_has_link = conversions.convert_links(md)
    assert actual_tex == tex
    assert actual_has_link == has_link


@pytest.mark.parametrize(
    ["md", "tex"],
    [
        (
            ("|H1|H2|H3|\n|-|-|-|\n|11|12|13|\n|21|22|23|"),
            (
                "\\begin{tabular}{|l|l|l|}\n"
                "\\hline\n"
                "H1&H2&H3 \\\\\n"
                "\\hline\n"
                "11&12&13 \\\\\n"
                "21&22&23 \\\\\n"
                "\\hline\n"
                "\\end{tabular}"
            ),
        ),
        (
            ("H1|H2|H3\n-|-|-\n11|12|13\n21|22|23"),
            (
                "\\begin{tabular}{|l|l|l|}\n"
                "\\hline\n"
                "H1&H2&H3 \\\\\n"
                "\\hline\n"
                "11&12&13 \\\\\n"
                "21&22&23 \\\\\n"
                "\\hline\n"
                "\\end{tabular}"
            ),
        ),
    ],
)
def test_convert_tables(md, tex):
    assert conversions.convert_table(md) == tex


@pytest.mark.parametrize(
    ["md", "tex"],
    [
        (
            ("- Text 1\n- Text 2\n- Text 3"),
            (
                "\\begin{itemize}\n"
                "    \\item Text 1\n"
                "    \\item Text 2\n"
                "    \\item Text 3\n"
                "\\end{itemize}"
            ),
        ),
        (
            ("1. Text 1\n2. Text 2\n3. Text 3"),
            (
                "\\begin{enumerate}\n"
                "    \\item Text 1\n"
                "    \\item Text 2\n"
                "    \\item Text 3\n"
                "\\end{enumerate}"
            ),
        ),
    ],
)
def test_convert_lists(md, tex):
    assert conversions.convert_lists(md) == tex
