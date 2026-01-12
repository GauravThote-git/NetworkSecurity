import sys
from networksecurity.logging import logger


class NetworkSecurityException(Exception):
    def __init__(self, error_message: Exception, error_details: sys):
        super().__init__(error_message)

        _, _, exc_tb = error_details.exc_info()

        if exc_tb is not None:
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno = "Unknown"
            self.file_name = "Unknown"

        self.error_message = error_message

    def __str__(self):
        return (
            f"Error occurred in python script name "
            f"[{self.file_name}] line number "
            f"[{self.lineno}] error message "
            f"[{self.error_message}]"
        )


if __name__ == "__main__":
    try:
        logger.info("Enter the try block")
        a = 1 / 0
    except Exception as e:
        logger.error("Exception occurred", exc_info=True)
        raise NetworkSecurityException(e, sys)
