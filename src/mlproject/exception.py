import sys 
from src.mlproject.logger import logging


def get_error_message_details(error_message, error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_message = "Exception error occured with following details: \nPython script name: {0} \nline number: {1} \nerror message: {2}".format(file_name, line_no, str(error_message))

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = get_error_message_details(error_message, error_details) 

    def __str__(self) -> str:
        return self.error_message