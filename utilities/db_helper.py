import mysql.connector

from conftest import config


class DbHelper:

    @staticmethod
    def get_connection(config):
        db_config = config["db_config"]
        return mysql.connector.connect(host=db_config["host_name"], port=db_config["port"],
                                database=db_config["bd_name"],
                                username=db_config["username"],
                                password=db_config["password"])

    @classmethod
    def execute_query(cls, config, query):

        connection = cls.get_connection(config)
        curser = connection.cursor(dictionary=True)
        curser.execute(query)
        return curser.fetchall()


