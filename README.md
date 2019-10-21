# md2tex

Converts markdown to LaTeX. Saves time. Makes shiba inu happy.

## Requirements
- Python3
- pdflatex


## Installation

Clone the repository and install using setup.py.

```bash
git clone https://github.com/prtx/md2tex
cd md2tex
python3 setup.py install
```

## Usage

### Config file

A yaml file is needed to store some configs and document information.

```yaml
title: md2tex
author: Pratik Shrestha
document_type: article
```

### LaTeX Generation
```bash
md2tex --generate-pdf <MD-FILE> <CONFIG-FILE> <OUTPUT-TEX-FILE>
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
