import sys
import logging

def error_message_detail(error,error_detail:sys):
   _,_,exc_tb=error_detail.exe_info()
   file_name=exc_tb.tb_frame.f_code.co_filename
   error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
   file_name,exc_tb.tb_lineno,str(error))

    return error_message

   

class CustomException(Exception):
    def __init_(self,error_message,error_detail:say):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    def__srt__(self):
        return self.error_message

