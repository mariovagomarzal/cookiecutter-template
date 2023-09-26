"""Test if the cookiecutter template renders correctly."""
import pytest


# Useful constants
DIRECTORIES = [
    "{{cookiecutter.project_slug}}",
    "hooks",
    "tests",
]
FILES = [
    ".gitignore",
    ".pre-commit-config.yaml",
    "cookiecutter.json",
    "LICENSE",
    "noxfile.py",
    "pyproject.toml",
    "README.md",
    "requirements.txt",
    "tests/__init__.py",
]


# Auxiliary functions
def check_no_errors(result):
    """Check if the cookiecutter template rendered without errors."""
    assert result.exit_code == 0
    assert result.exception is None

def check_properly_created(path, name):
    """Check if the cookiecutter template was properly created."""
    assert path.is_dir()
    assert path.name == name

def check_directories_exist(path, directories):
    """Check if the given directories exist."""
    for directory in directories:
        assert (path / directory).is_dir()

def check_files_exist(path, files):
    """Check if the given files exist."""
    for file in files:
        assert (path / file).is_file()

def get_licenses(author=""):
    """Return a dict of the licenses names and contents that should contain
    if the that license is selected."""
    return {
        "MIT": ["MIT License", author],
        "Apache-2.0": ["Apache License", author],
        "The-Unlicense": ["unlicense.org"],
    }

def check_license_content(path, license, author):
    """Check if the license file contains the required content."""
    license_file = path / "LICENSE"
    license_content = license_file.read_text()

    for required_content in get_licenses(author)[license]:
        assert required_content in license_content


# Fixtures
@pytest.fixture
def extra_context():
    """Return a list of extra contexts."""
    return [
        {
            "project_slug": "test_project",
            "author": "Test Author",
            "license": license,
        } for license in get_licenses().keys()
    ]


# Tests
def test_cookiecutter_no_context(cookies):
    """Test if the cookiecutter template renders correctly without
    context."""
    result = cookies.bake()
    path = result.project_path

    check_no_errors(result)
    check_properly_created(path, "cookiecutter-template")
    check_directories_exist(path, DIRECTORIES)
    check_files_exist(path, FILES)
    check_license_content(path, "MIT", "Your Name")

def test_cookiecutter_context(cookies, extra_context):
    """Test if the cookiecutter template renders correctly with
    context."""
    for context in extra_context:
        result = cookies.bake(extra_context=context)
        path = result.project_path

        check_no_errors(result)
        check_properly_created(path, context["project_slug"])
        check_directories_exist(path, DIRECTORIES)
        check_files_exist(path, FILES)
        check_license_content(path, context["license"], context["author"])
