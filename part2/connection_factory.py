import MySQLdb


class Connection_factory(object):
    def get_connection(self):
        connection = MySQLdb.connect(
            host="localhost",
            user="root",
            password="",
            db="alura"
        )
        return connection
