# Python Data Boilerplate

Repository that I use as a starting point for my python data wrangling experiments and screencasts.

The repository comes with data analysis libraries stored in requirements.txt. In the future generic data wrangling utilities that I create may be added to the project.

## Setup

### 1. Clone this repository

```
git clone git@github.com:encho/python-data-boilerplate.git my-python-project
```

### 2. Remove origin

```
git remote remove origin
```

### 3. Create a new git repository

Create a new repo on your github, gitlab account, or wherever you manage your git projects.

### 4. Set the new origin for your data project

```
git remote add origin git@github.com:<YOUR_ACCOUNT>/<YOUR_REPO>.git
```

### 5. Initial push to your new repo

```
git push -u origin main
```

## Create a virtual environment (highly recommended)

Using a virtual environment for Python projects is sensible because it allows you to create an isolated environment for your project with specific versions of packages and dependencies. This avoids conflicts with other versions of packages installed globally and ensures consistency across different machines and platforms. Virtual environments are essential for managing dependencies and ensuring reproducibility in Python projects.

### 1. Create a virtual environment

```
python3 -m venv venv
```

### 2. Activate the virtual environment

```
source ./venv/bin/activate
```

### 3. Install the dependencies in `requirements.txt`

```
pip install -r requirements.txt
```

## Working with the virtual environment

### 1. Install new dependencies

Once your virtual environment is setup and activated, you can install new python packages as you normally would, for example:

```
pip install <your-great-library>
```

### 2. Freeze the updated dependencies into `requirements.txt`

Remember to persist your updated dependencies to the `requirements.txt` file **before checking in any code changes**, like so:

```
pip freeze > requirements.txt
```

### 3. Deactivate virtual environment at the end of your session

```
deactivate
```
