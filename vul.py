# vuln.py - FIXED version

import subprocess

def run_system_cmd(cmd_list):
    # Safe subprocess execution
    subprocess.run(cmd_list, check=True)

if __name__ == "__main__":
    run_system_cmd(["echo", "safe now"])
