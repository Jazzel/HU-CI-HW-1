# CI Assignment 1

URL : [https://github.com/Jazzel/HU-CI-Assignment-1](https://github.com/Jazzel/HU-CI-Assignment-1)

Report: [https://github.com/Jazzel/HU-CI-Assignment-1/blob/main/CI%20assignment%201%20MM06886-AK06857.pdf](https://github.com/Jazzel/HU-CI-Assignment-1/blob/main/CI%20assignment%201%20MM06886-AK06857.pdf)

## File Hierarchy

Here is the hierarchy of your code files:

- `images/` contains generated images by EAA (Evolutionary Algorithm Art | Mona Lisa)
- `tsp_results/`
  - `analysis.py` generates plots by taking json file as input
  - `tsp_{dataset}_p{scheme_no}_s{scheme_no}.json` multiple files will be generated by analysis.py
- `jssp_results/`
  - `analysis.py` generates plots by taking json file as input
  - `jssp_{dataset}_p{scheme_no}_s{scheme_no}.json` multiple files will be generated by analysis.py
- `main.py` contains Evolutionary Algorithm code
- `selectionSchemes.py` contains code for selection schemes used by EA
- `tsp.py` contains driver code/class to run TSP algorithm based on EA
- `JSSP.py` contains driver code/class to run JSSP algorithm based on EA
- `EAA.py` contains driver code/class to run EA art (Mona Lisa) algorithm based on EA

## Installation

Provide instructions on how to install and set up your project here.
**Virtual Environment Setup using `virtualenv`**

### Introduction

A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. It allows you to work on a specific project without worrying about the impact of other projects or the system-wide Python installation.

#### Prerequisites

- python and pip ( version = "\*" )

  Visit [https://www.python.org/](https://www.python.org/) and download any version of python for your operating system.
  Open command prompt/powershell/terminal in default python environment.

  ```
  # For verification open command prompt or terminal and run
  python --version
  Output: Python 3.x.x
  ```

- virtualenv ( version = "\*" )
  ```
  pip install virtualenv
  # Again for verification
  virtualenv --version
  Output: pipenv, version 2020.x.x
  ```

#### Available Scripts

- Download Project files

  - Clone using git
    ```
    git clone https://github.com/Jazzel/HU-CI-Assignment-1
    cd HU-CI-Assignment-1/
    ```
    #### Or
  - Download the repository from [https://github.com/Jazzel/HU-CI-Assignment-1](https://github.com/Jazzel/HU-CI-Assignment-1) then move to the directory where you downloaded or cloned the repository and cd into project directory.

    `cd HU-CI-Assignment-1-main/`

- Launching in project's virtual environment

  ```
  virtual env
  ```

- Install dependencies via your powershell/terminal/cmd.

  ```
  pip install -r requirements.txt
  ```

## Execution

- To run tsp:

  ```
  python ./tsp.py
  ```

  This will generate `tsp_results/` folder and json files according to selection schemes.
  You can change selection schemes by changing tuples in `combinations` variable.

  `combinations =  [(1,  5),  (3,  4),  (4,  4),  (5,  5),  (1,  2),  (1,  4),  (2,  4)]`

- To run jssp:

  ```
  python ./JSSP.py
  ```

  This will generate `jssp_results/` folder and images files according to selection schemes.
  You can change selection schemes by changing tuples in `combinations` variable.

  `combinations =  [(1,  5),  (3,  4),  (4,  4),  (5,  5),  (1,  2),  (1,  4),  (2,  4)]`

- To run EAA (Mona Lisa):

  ```
  python ./EAA.py
  ```

  This will generate `images/` folder and json files according to selection schemes.
  You can change selection schemes by changing two variables in `EAA.py`.
  `parent_selection =  2 & survival_selection =  4`

#### Group

- Ali Asghar Kerai | [https://github.com/AliasgharKerai](https://github.com/AliasgharKerai)
- Muhammad Jazzel Mehmood | [https://github.com/Jazzel](https://github.com/Jazzel)
