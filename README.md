# ARC Py_39

This repo updates some utils, which were written to work with Python 3.5, but won't work with Python 3.9 which is a shortcoming when using the primer notebook in Visual Studio Code. 

## Installation

1. Download an Anaconda distribution for your specific OS: [Anaconda](https://www.anaconda.com/download/success)
2. Create a conda environment with Python 3.9 and activate it
```bash
conda create --name ARCenv python=3.9
conda activate ARCenv
```
3. Compile the C extension

### For Linux/Mac users

Download and install GNU C compiler. Then with terminal open, navigate to arc folder where `setupc.py` file is located execute:

```bash
python setupc.py build_ext --inplace
```
### For Windows users

You can follow the instructions to compile [here](https://arc-alkali-rydberg-calculator.readthedocs.io/en/latest/installation.html), but the best option is to install WSL 2 (Windows Subsystem for Linux) once and for all :)


4. Go to the folder `PROJECT_FOLDER/code/` and run

```bash
pip install -r requirements.txt
```

## Usage

In the root folder there is a file called `Rydberg_atoms_a_primer_notebook.ipynb`, now you should be able to run the examples in there.