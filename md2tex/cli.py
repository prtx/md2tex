import click
from md2tex import md2tex


@click.command()
@click.argument("md_file")
@click.argument("config_file")
@click.argument("tex_file")
@click.option("--generate-pdf", is_flag=True, help="")
def main(md_file, config_file, tex_file, generate_pdf):
    """md2tex CLI"""
    print("Converting markdown to LaTeX...")
    md2tex.convert(md_file, config_file, tex_file)
    print("Generating pdf from LaTeX...")
    if generate_pdf:
        md2tex.generate_pdf(tex_file)
