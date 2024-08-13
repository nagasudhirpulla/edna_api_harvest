import json
import pandas as pd
from src.config.fetchConfig import FetchConfig
from src.config.dbConfig import DbConfig

# initialize the app config global variable
fetchConf = None
ednaPnts: 'list[tuple[str]]' = []
dbConf = None


def loadFetchConfig(jsonPath="config/fetchConfig.json"):
    # load config json into the global variable
    with open(jsonPath) as f:
        global fetchConf
        jsonDict = json.load(f)
        fetchConf = FetchConfig(**jsonDict)
        return fetchConf


def getFetchConfig():
    # get the cached application config object
    global fetchConf
    return fetchConf


def loadEdnaPnts(filePath="config/pnts.csv"):
    global ednaPnts
    pntsDf = pd.read_csv(filePath, header=None)
    ednaPnts = list(
        pntsDf.itertuples(index=False, name=None))
    return ednaPnts


def getEdnaPnts():
    global ednaPnts
    return ednaPnts


def loadDbConfig(jsonPath="config/dbConfig.json"):
    # load config json into the global variable
    with open(jsonPath) as f:
        global dbConf
        jsonDict = json.load(f)
        dbConf = DbConfig(**jsonDict)
        return dbConf


def getDbConfig():
    global dbConf
    return dbConf
