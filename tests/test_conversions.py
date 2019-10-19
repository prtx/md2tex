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
