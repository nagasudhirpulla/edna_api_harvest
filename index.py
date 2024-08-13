from src.entities.ednaSample import EdnaSample
from src.config.appConfig import loadFetchConfig, loadEdnaPnts, loadDbConfig
from src.services.ednaFetcher import EdnaFetcher
from src.services.ednaDbAdapter import EdnaDbAdapter
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--fetchConfig', help='edna API config file path',
                    default="config/fetchConfig.json")
parser.add_argument('--dbConfig', help='DB config file path',
                    default="config/dbConfig.json")
parser.add_argument(
    '--pnts', help='edna points list file path', default="config/pnts.csv")

args = parser.parse_args()
fetchConfigPath = args.fetchConfig
dbConfigPath = args.dbConfig
pntsPath = args.pnts

fetchConf = loadFetchConfig(fetchConfigPath)
startDt = fetchConf.getStartDt()
endDt = fetchConf.getEndDt()

print(f"{startDt} to {endDt}")

pnts = loadEdnaPnts(pntsPath)

fetcher = EdnaFetcher(fetchConf.apiBaseUrl)
dataRows: list[EdnaSample] = []
for pnt in pnts:
    dataRows += fetcher.fetchEdnaData(pntId=pnt[0], startTime=startDt, endTime=endDt,
                                      periodicitySecs=fetchConf.fetchPeriodicitySecs, samplingType=fetchConf.fetchStrategy)
# print(dataRows)

dbConf = loadDbConfig(dbConfigPath)
# print(dbConf)

dbAdapter = EdnaDbAdapter(dbConf)
dbAdapter.connectToDb()
dbAdapter.pushRows(dataRows)
dbAdapter.disconnectDb()

print("done...")
