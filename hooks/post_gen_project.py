from pathlib import Path


Path("\{\{cookiecutter.project_slug\}\}").mkdir(
    parents=True,
    exist_ok=True
)
