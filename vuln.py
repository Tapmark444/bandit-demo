# vuln.py - intentionally vulnerable for Bandit demo

import subprocess

# Hardcoded password (Bandit flags B105)
password = "P@ssw0rd123"

def run_system_cmd(cmd):
    # Dangerous shell execution (Bandit flags B602/B603)
    subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    user_input = "echo vulnerable"
    run_system_cmd(user_input)
