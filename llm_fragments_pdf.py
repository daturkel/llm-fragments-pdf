import llm
import pymupdf4llm


@llm.hookimpl
def register_fragment_loaders(register):
    register("pdf", pdf_loader)


def pdf_loader(argument: str) -> llm.Fragment:
    """
    Use PyMuPDF to insert PDFs as markdown

    Example usage:
      llm -f 'pdf:my_pdf.pdf' ...
    """
    result = f"Filename: {argument}\n\n"
    result += (
        pymupdf4llm.to_markdown(
            argument, ignore_images=True, ignore_graphics=True
        ).rstrip()
        + "\n"
    )

    return llm.Fragment(result, source=argument)
