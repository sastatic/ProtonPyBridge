import os

class Config:
    USERNAME = "example"
    EMAILID = USERNAME + "@proton.me"
    PASSWORD = os.environ.get("PROTON_PASS")