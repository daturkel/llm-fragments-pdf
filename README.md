# llm-fragments-pdf

A fragment loader for [LLM](https://llm.datasette.io/) that converts PDF files into markdown plaintext using [PyMuPDF4LLM](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/index.html).

This is especially useful for models which don't support [attachments](https://llm.datasette.io/en/stable/python-api.html#attachments).

[![PyPI](https://img.shields.io/pypi/v/llm-fragments-pdf.svg)](https://pypi.org/project/llm-fragments-pdf/)
[![Changelog](https://img.shields.io/github/v/release/daturkel/llm-fragments-pdf?include_prereleases&label=changelog)](https://github.com/daturkel/llm-fragments-pdf/releases)
[![Tests](https://github.com/daturkel/llm-fragments-pdf/actions/workflows/test.yml/badge.svg)](https://github.com/daturkel/llm-fragments-pdf/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/daturkel/llm-fragments-pdf/blob/main/LICENSE)

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/):

```bash
llm install llm-fragments-pdf
```

## Usage

Use `-f 'pdf:filepath'` convert a pdf file to markdown text and insert that text as a fragment.

Example:

```bash
llm -f 'pdf:my_pdf.pdf' "What is this document about?"
```

The output includes:
- Filename
- PDF contents as markdown

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

```bash
cd llm-fragments-pdf
python -m venv venv
source venv/bin/activate
```

Install the dependencies and test dependencies:

```bash
pip install -e '.[test]'
```

To run the tests:

```bash
pytest
```

## Dependencies

- [PyMuPDF4LLM](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/index.html): For extracting markdown from PDFs
- [llm](https://llm.datasette.io/): The LLM CLI tool this plugin extends
