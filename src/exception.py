## Steps:
'''
    1. We first create our own exceptions. 
    - import sys --> sys will have info of runtimes of all functions 

    2. Make a function for error_message_detail()
        - we need error_detail --> sys
        - we need the error type itself --> exception 

        - Steps: 
            1. We need to save information of our exception. 
            2. We get the pbject of it and we save it --> exp_info() -> (type, error_message, traceback obj)
            3. We now need to just print the message:
                - we need the filename, 
                - the line number of where error occured
                - the error message
'''

import sys
import logging
from src.logger import logging


# When an error raises, this is the function we have to call. 
def error_message_detail(error: Exception, error_detail:sys):
    # Saving the detail of exception in the form of traceback obj:
    _,_,exp_tb_obj = error_detail.exp_info()

    # printing the message, we need: 
    # file name, line num of error, error_message

    file_name = exp_tb_obj.tb_frame.f_code.co_filename
    line_num = exp_tb_obj.tb_lineno
    error_message = str(error)

    final_message = (
        f"Error occured in python script name: {file_name} \n"
        f"file number: {line_num} \n"
        f"error message: {error_message}"
    )

    return final_message


# Now we have to make the CustomException class:
# we need: Constructor, methods, ...
class CustomException(Exception):
    def __init__(self, error: Exception, error_detail:sys):
        # let the parent(Exception) store what it already knows how to store using super()
        super().__init__(error)

        # Now add extra info:
        self.error_message = error_message_detail(
            error, 
            error_detail
        )

    def __str__(self):
        return self.error_message



if __name__  == "__main__":
    try: 
        a = 1/0
    except:
        logging.info("Divide by zero")
        raise CustomException
        

    


