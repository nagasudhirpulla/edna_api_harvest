this script fetches data from edna and pushes it to a DB

## sample config/dbConfig.json
```json
{
    "host": "localhost",
    "port": "5432",
    "db": "db",
    "uname": "uname",
    "pwd": "pwd"
}
```

## sample config/fetchConfig.json
```json
{
    "apiBaseUrl": "http://localhost:81",
    "absoluteStartTime": "2023-08-07 00:00:00",
    "varStartYears": 0,
    "varStartMonths": 0,
    "varStartDays": 0,
    "varStartHours": 0,
    "varStartMinutes": -5,
    "varStartSeconds": null,
    "absoluteEndTime": "2023-08-07 01:00:00",
    "varEndYears": 0,
    "varEndMonths": 0,
    "varEndDays": 0,
    "varEndHours": 0,
    "varEndMinutes": -1,
    "varEndSeconds": null,
    "fetchStrategy": "snap",
    "fetchPeriodicitySecs": 30
}
```

## sample config/pnts.csv
```
pntId1,name1
pntId2,name2
pntId3,name3
```

## TODO
* fetch window feature
* add type checking after initialization in fetch config dataclass