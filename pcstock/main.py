from schedule import every, repeat, run_pending
import time
import subprocess

@repeat(every(1).minutes)
def job():
    subprocess.run(['python3', 'run.py'])

while True:
    run_pending()
    time.sleep(3)