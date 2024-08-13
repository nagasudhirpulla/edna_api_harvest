from dataclasses import dataclass
import datetime as dt


@dataclass
class EdnaSample:
    val: float
    timeStamp: dt.datetime
    pntId: str
