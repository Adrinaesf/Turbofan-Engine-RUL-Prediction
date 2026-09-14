## Starting a New Machine Learning Project (Complete Workflow)


* Outline: 
    - Making an environment
    - Maiking a github repository
    - Make ``setup.py`` and ``requirements.txt``
    - Make a source folder
    - Making a function for package organization


1. Making an environment
    - 1.1: Create a project folder
        ``mkdir Generic-ML-Project``
    - 1.2: Move into it:
        ``cd Generic-ML-Project``
    - 1.3: Open nit in VScode:
        ``code .``
    - 1.4: Create a Conda environment
        ``conda create -p ./venv python=3.11 -y``  
        Functionality of -p: Put the environment at this path (./venv). 
        Functionality of -y: Automatically answer yes. 
    - 1.5: Activate the environment:
        ``conda activate ./venv``
    - 1.6: Check Python: 
        ``python --version``

2. Making a repository:
    - 2.1: Got to github and make a new repository for your project. 
    - 2.2: Copy the HTTPS of project
    - 2.3: Initilize the git in terminal of VSCode
        ``git init``
        This tells git to start tracking this project.

    - 2.4: Connect the github
        ``git remote add origin https://github.com/username/project.git``

        This adds a remote named "origin": It's like my online copy of the project.
        It cfan be checked by: ``git remote -v``

    - 2.5: Create .gitignore
        Go to github. 
        Create a new file, name it .gitignore, and choose language as Python. 

        Then in VSCode do: 
            first time: ``git pull origin main``
            after: ``git pull``

        To put the files you made on github on your local env of VSCode.

        Why? Because venv is systemp dependent and you may have python 3.6 but it won't work on other systems if they differ, so the best practice is to make the requirment.txt. 

    - 2.6: Check the status of git 
        ``git status``

        This answers: What's changed? What hasn't? What's staged? What's untracked? Think of it as Git's dashboard.
    
    - 2.7: Add the files 
        `` git add . ``
    - 2.8: Commit
        `` git commit -m "message" ``
    - 2.9: Push
        first time: ``git push -u origin main ``
        after: ``git push``

3. Make ``setup.py``, ``requirements.txt`` and ``.gitignore``
    **Importance of setup.py**: 
        - It tells Python how to package/install the project
        - It can be upload to PyPi, and others can download it using: ``pip install your-package``. 

    **Importance of requirement.txt**: 

    - 3.1: Make a file name ``setup.py``
    - 3.2: Import the setup libarary:
        ``from setuptools import find_packages,setup``
    - 3.3: write the setup information:
        ``setup(name,version,...)``
    
4. Make a source folder: 
    This is a folder where your actual source code such as like data cleaening, your ML model, are inside. 
    
    - 4.1: Make a folder named `src`
    - 4.2: Make a ``__init__.py`` file. This make src as a package. 

5. Making a function for package organization
    Adding the required packages to the list ``install_requires`` can be inefficient if you have a lot of packages. So we make a function to deal with it. 

    - 5.1: Change the list for `install_requirments` to a function named `get_requirments('requirements.txt')`

    - 5.2: Make the function + add the required libaries for it:  `` from typing import List ``

    - 5.3: Define the function:
        `` def get_requirements(file_path:str)->List[str]: ``








