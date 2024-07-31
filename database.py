# database.py
import os, logging, mariadb

class DB:
    def __init__(self, database):
        self.conn = mariadb.connect(
                host=os.environ['DB_HOST'],
                port=10021,
                user=os.environ['DB_USER'],
                password=os.environ['DB_PASSWORD'],
                database=database,
                autocommit=True
            )
        
        self.cur = self.conn.cursor()

        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    def __del__(self):
        self.conn.close()
        self.logger.info('Connect close')

    def execute(self, query):
        try:
            self.cur.execute(query)

            self.logger.info(f'Success to execute query: {query}')

            if (type(self.cur.description) == tuple):
                query_result = []
                for result in self.cur:
                    query_result.append(result)

                return query_result
            else:
                return {'message': 'sucess'}

        except mariadb.Error as e:
            self.logger.error(f'Fail to execute {query}: {e}')

            return {'message': 'fail'}

            

def request_connect_db(database):
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        db = DB(database)
        logger.info("Success to connect DB")

        return {
            "connect": True,
            "message": "Success to connect DB",
            "DB": db,
            }
    except mariadb.Error as e:
        logger.error(f"Fail to connect DB: {e}")
        return {
            "connect": False,
            "message": "Fail to connect DB",
            "Error": e
            }