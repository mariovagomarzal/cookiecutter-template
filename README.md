# cookiecutter-template v0.1.0

Cookiecutter template is a template for creating... cookiecutter templates!

## Usage

Since this is a
[Cookiecutter](https://github.com/cookiecutter/cookiecutter)
template, you must have Cookiecutter installed to use it. Refer to the
Cookiecutter documentation for installation instructions.

To use this template, run the following command:

```bash
cookiecutter gh:mariovagomarzal/cookiecutter-template
```

You can also specify a directory to create the template in with the
`--output-dir` option. For more details on how to use the command refer
to the Cookiecutter documentation.

When you run the command, you will be prompted to enter values for the
variables defined in the template. These are the options, what they do and
their default values:

- `project_slug`: The name of the directory that will be created for the
  project. The default value is `cookiecutter-template`.
- `author`: The name of the author of the project. The default value is
  `Your Name`.
- `license`: The license to use for the project. The default value is
  `MIT`. The available options are:
    - `MIT`
    - `Apache 2.0`
    - `The-Unlicense`

With the default options, the project will be created in a directory named
`cookiecutter-template` with the following structure:

```text
cookiecutter-template/
├── LICENSE
├── README.md
├── cookiecutter.json
├── noxfile.py
├── pyproject.toml
├── requirements.txt
├── tests
│   └── __init__.py
└── {{cookiecutter.project_slug}}
```

To understand what each file and directory is for, refer to the
(feautures)[#features] section.

## Features

- **Base files:** The template includes the basic `cookiecutter.json` and
    `{{cookiecutter.project_slug}}` file and directory of a Cookiecutter
    template.
- **Python environment:** The template includes a `requirements.txt` file
  with the dependencies needed to use and test the template. We use `nox`
  to manage the testing and linting sessions. Refer to the documentation
  of each tool for more details.
- **Git repository:** The template includes a `.gitignore` file and a
  `README.md` file with a basic template for the README. It also lets you
  choose a license for the project. Lastly, it includes a
  `.pre-commit-config.yaml` file with the configuration for the
    [pre-commit](https://pre-commit.com/) tool.

## Contributing

Feel free to open an issue or a pull request if you find a bug or want to
add a new feature. Make sure to follow the [code of
conduct](./CODE_OF_CONDUCT.md).

## License

This project is licensed under the terms of the [MIT License](./LICENSE) by
Mario Vago Marzal.

_Note: The license under the `{{cookiecutter.project_slug}}` directory
is part of the template and does not affect the license of this software_
