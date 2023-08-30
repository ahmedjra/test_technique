# test_technique

The goal of the project is to extract entites from csv files to create a csv file containing these informations.

## Prerequisites

Ensure you have the following installed:
- **Python**: Version 3.11.3. If it's not installed, [download and install](https://www.python.org/downloads/).

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **(Optional) Set up a virtual environment**:
   Using a virtual environment is recommended. Set one up with:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
   ```

3. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To generate the `output.csv` file, run:

```bash
python main.py /path/to/your/directory/
```

Replace `/path/to/your/directory/` with the actual path where you have your data.

## Output

Upon successful execution, you'll find the `output.csv` file in the current directory.
You'll find also a plot "Histogramme" showing missing values of each column.

## License

This project is under the MIT License. See the [LICENSE.md](LICENSE.md) file for more details.
