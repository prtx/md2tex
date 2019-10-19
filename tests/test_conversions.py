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
