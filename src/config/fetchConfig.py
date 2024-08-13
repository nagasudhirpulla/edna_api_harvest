from dataclasses import dataclass, field

from src.utils.variableTime import VariableTime


@dataclass
class FetchConfig:
    apiBaseUrl: str = field(default="http://localhost:62448")
    absoluteStartTime: str = field(default="2024-08-07 00:00:00")
    varStartYears: int | None = field(default=0)
    varStartMonths: int | None = field(default=0)
    varStartDays: int | None = field(default=0)
    varStartHours: int | None = field(default=0)
    varStartMinutes: int | None = field(default=-2)
    varStartSeconds: int | None = field(default=None)
    absoluteEndTime: str = field(default="2024-08-07 01:00:00")
    varEndYears: int | None = field(default=0)
    varEndMonths: int | None = field(default=0)
    varEndDays: int | None = field(default=0)
    varEndHours: int | None = field(default=0)
    varEndMinutes: int | None = field(default=0)
    varEndSeconds: int | None = field(default=None)
    fetchStrategy: str = field(default="snap")
    fetchPeriodicitySecs: int = field(default=60)

    # TODO add type checking after initialization

    def getStartDt(self):
        startTime = VariableTime(absoluteTime=self.absoluteStartTime,
                                 varYears=self.varStartYears,
                                 varMonths=self.varStartMonths,
                                 varDays=self.varStartDays,
                                 varHours=self.varStartHours,
                                 varMinutes=self.varStartMinutes,
                                 varSeconds=self.varStartSeconds)
        startDt = startTime.getDt()
        return startDt

    def getEndDt(self):
        endTime = VariableTime(absoluteTime=self.absoluteEndTime,
                               varYears=self.varEndYears,
                               varMonths=self.varEndMonths,
                               varDays=self.varEndDays,
                               varHours=self.varEndHours,
                               varMinutes=self.varEndMinutes,
                               varSeconds=self.varEndSeconds)
        endDt = endTime.getDt()
        return endDt
