__author__ = 'dako'
from mysql import connector

class DbFixture():
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = connector.connect(host=host, port=port, database=database, user=user, password=password)

    def destroy(self):
        self.connection.close()