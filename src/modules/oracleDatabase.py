
import os
import oracledb as oracle

class OracleDatabase():
    
    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, value):
        self.__connection = value

    def __init__(self):
        self.connection = None
        self.cursor = None

        self.username = os.getenv("oracle_username")
        self.password = os.getenv("oracle_password")
        self.host = os.getenv("oracle_host")
        self.port = os.getenv("oracle_port")
        self.service_name = os.getenv("oracle_service_name")

    def open_connection(self):
        return oracle.connect(
            user = self.username,
            password = self.password,
            dsn = f"{self.host}:{self.port}/{self.service_name}"
        )

    def close_connection(self):
        self.connection.close()
        self.connection = None