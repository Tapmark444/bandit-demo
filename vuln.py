# vuln.py  -- intentionally vulnerable for demo

import subprocess

# 1) Hardcoded secret (Bandit flags B105)
password = "P@ssw0rd123"

def run_system_cmd(cmd):
    # 2) Unsafe execution with shell=True (Bandit flags B602/B603)
    subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    # user-supplied content could be used here in real apps
    run_system_cmd("echo vulnerable")
