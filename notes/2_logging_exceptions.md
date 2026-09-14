## Logging and Exception handelling

* Outline: 
    - In ``src`` make ``components`` folder
    - In ``src`` make ``pipeline`` folder
    - In ``src`` make ``logger`` file
    - In ``src`` make ``exception`` file
    - In ``src`` make ``utils`` file
    - Making our own exceptions
    - Coding the logging file


1. In ``src`` Make ``components``
    - 1.1: Make the folder
    - 1.2: In components, make ``__init__.py``
        * This is because we want the components to be in the form of a package. 
        * It will have all the modules. Ex: data-ingestion, data-transformation, data-validation, ...

    - 1.3: Make the module files. 
        * data_ingestion: Reading the data
        * data_transformation: Transforming the data
        * model_trainer: training the model 

2. In ``src`` make ``pipeline``:
    ``pipeline``is a way of organizing a series of operations or functions that process some data. 

    - 2.1: Make the ``train_pipeline.py`` in the folder
    - 2.2: Make the ``perdict_pipeline.py`` in the folder
    - 2.3: Make the ``__init__.py`` in the folder so we can import it. 

3. In ``src`` make ``logger`` file
    This is for login info. 
4. In ``src`` make ``exception`` file
    This is for exception handelling
5. In ``src`` make ``utils`` file
    This is a general file for all the functions we make and we c an also use these in the components folder as well. 

6. Making our own exceptions
    - 6.1: do ``import sys``
        * What is sys: The sys module is responsible for manippulating different parts of Python envs. 
        * So any exception that is getting controlled, the sys will have all its info. 
    - 6.2: add ``sys`` to ``requirment.txt``
    - 6.3: Make the function ``error_message_detail``:
        * This is a function to send an error when an exception occurs. 
        * More detail of function in ``src/exception.py``
    - 6.4: Make the customException class

7. Coding the logging file
    **Order:** Create folder -> Create full path -> Now tell logging where to write. 
    Using this file we create a ``log`` file to store program records. Without logging, you may only see an error in the terminal, and then it disappears. With logging, you get a file like:
        ``2026-07-26 18:42:10 - data_ingestion.py - line 41 - Data ingestion started``
        ``2026-07-26 18:42:12 - data_ingestion.py - line 58 - Dataset loaded successfully``
        ``2026-07-26 18:42:14 - train_pipeline.py - line 73 - division by zero``
    
    - 7.1: import ``logging``, ``os``, ``from datetime imprt datetime``
        * ``logging``: Python’s built-in system for recording messages. 
        * ``os`` : Used here for folders and file paths.
        * ``datetime``: Used for putting data abd time in log file. 
    
    - 7.2: Make the Log filename
    - 7.3: Creating the folder path 
        * To do this, we need the path of folder. 
        * So we have to create the folder path: 
        * Now use: ``ps.mkdirs(logs_path, exist=ok)``



        
