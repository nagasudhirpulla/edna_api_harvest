import psycopg2
from src.config.dbConfig import DbConfig
from src.entities.ednaSample import EdnaSample
import datetime as dt


class EdnaDbAdapter:
    def __init__(self, dbConf: DbConfig):
        self.conn = None
        self.dbConf = dbConf

    def pushRows(self, dataRows: 'list[EdnaSample]') -> bool:
        cur = self.conn.cursor()
        # commit in multiples of 500 rows
        rowIter = 0
        insIncr = 500
        numRows = len(dataRows)
        while rowIter < numRows:
            # set iteration values
            iteratorEndVal = rowIter+insIncr
            if iteratorEndVal >= numRows:
                iteratorEndVal = numRows

            # Create row tuples
            dataInsertionTuples = []
            for insRowIter in range(rowIter, iteratorEndVal):
                dataRow = dataRows[insRowIter]

                dataInsertionTuple = (dt.datetime.strftime(dataRow.timeStamp, '%Y-%m-%d %H:%M:%S'), dataRow.pntId,
                                      dataRow.val)
                dataInsertionTuples.append(dataInsertionTuple)

            # prepare sql for insertion and execute
            dataText = ','.join(cur.mogrify('(%s,%s,%s)', row).decode(
                "utf-8") for row in dataInsertionTuples)
            sqlTxt = 'INSERT INTO public.meas_time_data(\
        	meas_time, meas_tag, meas_val)\
        	VALUES {0} on conflict (meas_tag, meas_time) \
            do update set meas_val = excluded.meas_val'.format(dataText)
            cur.execute(sqlTxt)
            self.conn.commit()

            rowIter = iteratorEndVal

        # close cursor and connection
        cur.close()
        return True

    def connectToDb(self):
        self.conn = psycopg2.connect(host=self.dbConf.host, dbname=self.dbConf.db,
                                     user=self.dbConf.uname, password=self.dbConf.pwd, port=self.dbConf.port)

    def disconnectDb(self):
        self.conn.close()
