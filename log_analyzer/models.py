from datetime import datetime
from ipaddress import IPv4Address
from pydantic import BaseModel, Field, ValidationError

class SSHFailedLogin(BaseModel):
    timestamp: datetime
    hostname: str
    process: str
    pid: int = Field(gt=0)
    username: str = Field(max_length=32)
    src_ip: IPv4Address
    src_port: int = Field(ge=0, le=65535)

try:
    failed_login = SSHFailedLogin(
        timestamp=datetime(2026,9, 29, 3, 14, 7),
        hostname="watcher1",
        process="sshd",
        pid=2211,
        username="root",
        src_ip="203.0.113.50",
        src_port=51234
)
    print(failed_login)
except ValidationError as e:
    print(e.errors())