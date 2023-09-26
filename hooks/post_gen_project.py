from pathlib import Path


def get_project_slug_name():
    """This is a workaround to get the project slug name from the
    used as cookiecutter template container without using braces
    so the template can be rendered correctly."""
    lbrace = "{"
    rbrace = "}"

    return f"{lbrace}{lbrace}cookiecutter.project_slug{rbrace}{rbrace}"

# Create the project slug directory
Path(get_project_slug_name()).mkdir(
    parents=True,
    exist_ok=True
)

# Create the hooks directory
Path("hooks").mkdir(
    parents=True,
    exist_ok=True
)
