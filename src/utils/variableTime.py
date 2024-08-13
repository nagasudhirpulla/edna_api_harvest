from dataclasses import dataclass, field
import datetime as dt
import calendar


@dataclass
class VariableTime:
    absoluteTime: str = field(default="2024-08-07 00:00:00")
    varYears: int = field(default=0)
    varMonths: int = field(default=0)
    varDays: int = field(default=0)
    varHours: int = field(default=0)
    varMinutes: int = field(default=-2)
    varSeconds: int = field(default=None)

    def getDt(self):
        absDt = dt.datetime.strptime(
            self.absoluteTime, "%Y-%m-%d %H:%M:%S")
        nowDt = dt.datetime.now()

        # make millisecond component as zero
        absDt = absDt.replace(microsecond=0)
        nowDt = nowDt.replace(microsecond=0)

        reqDt = nowDt

        # Add offsets to current time as per the settings
        if not self.varYears is None:
            reqDt = addMonths(reqDt, 12*self.varYears)
        if not self.varMonths is None:
            reqDt = addMonths(reqDt, self.varYears)
        if not self.varDays is None:
            reqDt += dt.timedelta(days=self.varDays)
        if not self.varHours is None:
            reqDt += dt.timedelta(hours=self.varHours)
        if not self.varMinutes is None:
            reqDt += dt.timedelta(minutes=self.varMinutes)
        if not self.varSeconds is None:
            reqDt += dt.timedelta(seconds=self.varSeconds)

        # Set absolute time settings to the result time
        if self.varYears is None:
            reqDt = addMonths(reqDt, 12*(absDt.year-reqDt.year))
        if self.varMonths is None:
            reqDt = addMonths(reqDt, (absDt.month-reqDt.month))
        if self.varDays is None:
            reqDt += dt.timedelta(days=(absDt.day-reqDt.day))
        if self.varHours is None:
            reqDt += dt.timedelta(hours=(absDt.hour-reqDt.hour))
        if self.varMinutes is None:
            reqDt += dt.timedelta(minutes=(absDt.minute-reqDt.minute))
        if self.varSeconds is None:
            reqDt += dt.timedelta(seconds=(absDt.second-reqDt.second))
        return reqDt


def addMonths(inpDt, mnths):
    tmpMnth = inpDt.month - 1 + mnths

    # Add floor((input month - 1 + k)/12) to input year component to get result year component
    resYr = inpDt.year + tmpMnth // 12

    # Result month component would be (input month - 1 + k)%12 + 1
    resMnth = tmpMnth % 12 + 1

    # Result day component would be minimum of input date component and max date of the result month (For example we cant have day component as 30 in February month)
    # Maximum date in a month can be found using the calendar module monthrange function as shown below
    resDay = min(inpDt.day, calendar.monthrange(resYr, resMnth)[1])

    # construct result datetime with the components derived above
    resDt = dt.datetime(resYr, resMnth, resDay, inpDt.hour,
                        inpDt.minute, inpDt.second, inpDt.microsecond)

    return resDt
