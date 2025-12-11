import subprocess

def bad():
    user_input = input("Enter command: ")
    subprocess.call(user_input, shell=True)

bad()
