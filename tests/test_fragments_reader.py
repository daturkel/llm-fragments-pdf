import os

from llm_fragments_pdf import pdf_loader


def test_pdf_loader():
    test_file_path = os.path.join(os.path.dirname(__file__), "test.pdf")
    fragment = pdf_loader(test_file_path)

    assert (
        str(fragment)
        == f"Filename: {test_file_path}\n\n*This* is a **test** document with a [link](https://google.com/)\n"
    )
    assert fragment.source == test_file_path
