"""Common utility functions for the model_info management command."""


def clean_docstring(text: str) -> str:
    """Clean docstring by preserving code blocks and handling line breaks."""
    if not text:
        return ""

    # Escape code blocks
    text = text.replace("```", "\\```")
    # Replace line breaks with HTML tags
    text = text.replace("\n\n", "</p><p>").replace("\n", "<br>")
    # Escape markdown characters
    text = text.replace("_", "\\_").replace("*", "\\*")
    text = text.replace("|", "\\|")
    # Wrap non-code content in p tags if not already wrapped
    if not text.startswith("<p>"):
        text = f"<p>{text}</p>"
    return text
