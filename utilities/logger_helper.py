import logging


class LoggerHelper:

    @staticmethod
    def get_logger():
        logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s : %(levelname)s : %(message)s")
        return logging.getLogger()
