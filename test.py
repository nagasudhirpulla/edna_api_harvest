from src.config.appConfig import loadFetchConfig, loadEdnaPnts, loadDbConfig
from src.services.ednaFetcher import EdnaFetcher
from src.services.ednaDbAdapter import EdnaDbAdapter

fetchConf = loadFetchConfig()
startDt = fetchConf.getStartDt()
endDt = fetchConf.getEndDt()
print(startDt)
print(endDt)

pnts = loadEdnaPnts()

fetcher = EdnaFetcher(fetchConf.apiBaseUrl)
data = fetcher.fetchEdnaData(pntId=pnts[0][0], startTime=startDt, endTime=endDt,
                             periodicitySecs=fetchConf.fetchPeriodicitySecs, samplingType=fetchConf.fetchStrategy)
print(data)

dbConf = loadDbConfig()
print(dbConf)

dbAdapter = EdnaDbAdapter(dbConf)
dbAdapter.connectToDb()
dbAdapter.pushRows(data)
dbAdapter.disconnectDb()

print("done...")
