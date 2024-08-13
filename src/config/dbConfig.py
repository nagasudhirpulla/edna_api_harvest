from dataclasses import dataclass, field


@dataclass
class DbConfig:
    host: str = field(default="localhost")
    port: int = field(default="5432")
    db: str = field(default="db")
    uname: str = field(default="uname")
    pwd: str = field(default="pwd")
