# IDS706_Individual_Project_1🌟

This repository is for the IDS706 Individual Porject #1, and the project performs data analysis on the `cereal.csv` dataset, generating summary statistics, visualizing data, and automating the analysis pipeline using Python scripts and a Jupyter Notebook. The project is integrated with continuous integration (CI) for automated testing and reporting.

![CI](https://github.com/therealzella/IDS706-python-github-template/actions/workflows/ci.yml/badge.svg)

## Table of Contents✅
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Makefile Commands](#makefile-commands)
- [Contributing](#contributing)
- [License](#license)

## Project Overview✅
This repository is a Python project template designed for the IDS706 course. It includes:
- A `main.py` file with the core functionality.
- A `main_test.py` file with unit tests for the project.
- A `Makefile` for automating common tasks like formatting, linting, and testing.
- A `.gitignore` file to keep unnecessary files out of your repository.
- A `requirements.txt` file to manage dependencies.
- A `cereal.csv` file for the main.py to do the pandas analysis
- A `summary_statistics.csv` file to store the metrics of the cereal.csv
- A `calories_histogram.png` file to show the data visualization of the data from the cereal.csv
- A `Individual_Project_1.ipynb` file to show the descriptive statistical analysis and relate data visualization for the cereal.csv
- A `test_script.py` and a `test_lib.py` file to provide unit and functional tests for the codes in this project. 


## Installation▶️
To set up this project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/IDS706-python-template.git
    ```

2. Navigate to the project directory:
    ```sh
    cd IDS706-python-template
    ```

3. Create a virtual environment (optional but recommended):
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required packages:
    ```sh
    make install
    ```

## Usage✅
You can run the main script using:
```sh
python main.py
```

## Contributing🫡

We welcome contributions to this project! Please read our [Contributing Guidelines](LINK_TO_CONTRIBUTING_GUIDELINES) for details on our code of conduct and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc.

## Versioning

We use [SemVer](https://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/yourusername/IDS706-python-template/tags).
