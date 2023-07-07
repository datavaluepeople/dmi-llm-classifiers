# dmi-llm-classifiers
Work done during the DMI project on LLM classifiers for conflict and dialogue monitoring 

## Getting Started
To get started with the project, please follow the steps below:

### Step 1: Setting up Python Environment
Install pyenv by following the instructions provided in the official [pyenv installation
guide](https://github.com/pyenv/pyenv#installation).
Once pyenv is installed, open a new terminal session or restart your current session.

You will then need to install the current version of python for the project.
Open a terminal and navigate to the root directory of the project.
```
pyenv install
```

Once this is complete check the version:
```
cat .python-version
python --version
```
You should see the same python version printed twice.

### Step 2: Setting up a Python Virtual Environment
Open a terminal and navigate to the root directory of the project.

Run the following command to create a new Python virtual environment:

````
python -m venv .venv
```
This command will create a new directory named .venv in the project's root directory, which will contain all the necessary files for the virtual environment.

Activate the virtual environment:

On macOS and Linux:

```bash
source .venv/bin/activate
```

On Windows:
```
.venv\Scripts\activate
```
After activation, you should see (.venv) prefix in your terminal, indicating that the virtual environment is active.

### Step 3: Installing Requirements
Ensure that you have activated the virtual environment as instructed in Step 2.

Install the project dependencies by running the following command in your terminal:

```bash
pip install -r requirements.txt
```
This command will install all the required Python packages specified in the requirements.txt file located in the project's root directory.

Congratulations! You have successfully set up the Python environment, created a virtual environment, and installed the project dependencies.

Additional Resources
[Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
[pip - The Python Package Installer](https://pip.pypa.io/en/stable/)
[pyenv - Simple Python version management](https://github.com/pyenv/pyenv)
