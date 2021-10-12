# Malicious code when importing this package
# MALICIOUS START
from datetime import datetime

with open("./virus.txt", "w", encoding="utf-8") as buffer:
    buffer.write(f"I was here at {datetime.now()} ;>")
# MALICIOUS END


def do_something():
    print("I did something ;)")
