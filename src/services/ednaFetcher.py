import datetime as dt
import requests
import json
from src.entities.ednaSample import EdnaSample
from src.utils.timeUtils import convertTimeToReqStr
from typing import TypedDict


class EdnaPayloadDto(TypedDict):
    dval: float
    timestamp: str
    status: str


class EdnaFetcher():
    def __init__(self, host: str):
        self.host = host

    def fetchEdnaData(self, pntId: str, startTime: dt.datetime, endTime: dt.datetime, periodicitySecs: float, samplingType: str) -> list[EdnaSample]:
        startTimeStr = convertTimeToReqStr(startTime)
        endTimeStr = convertTimeToReqStr(endTime)

        params = dict(
            pnt=pntId,
            strtime=startTimeStr,
            endtime=endTimeStr,
            secs=periodicitySecs,
            type=samplingType
        )
        r = requests.get(
            url="{0}/api/values/history".format(self.host), params=params)
        fetchedObjects: list[EdnaPayloadDto] = json.loads(r.text)
        samples = [EdnaSample(val=x["dval"], timeStamp=dt.datetime.strptime(x["timestamp"], "%Y-%m-%dT%H:%M:%S"),
                              pntId=pntId) for x in fetchedObjects]
        return samples
