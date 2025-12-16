# vuln.py - fixed version

import subprocess

def run_system_cmd(cmd_list):
    # Safe execution without shell=True
    subprocess.run(cmd_list, check=True)

if __name__ == "__main__":
    run_system_cmd(["echo", "secure now"])
