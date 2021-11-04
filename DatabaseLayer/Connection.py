import psycopg2.extras

DB_HOST = "localhost"
DB_NAME = "OKTravel"
DB_USER = "postgres"
DB_PASS = "frigider"


class Connection:

    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    curs = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def closeConnection(self):
        self.conn.close()

    def closeCursor(self):
        self.curs.close()
