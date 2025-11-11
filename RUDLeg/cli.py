import sys
from RUDLeg.core_magic.CodeTemplateAndFunction import manager

def rudleg_create():
    filename = "manager.py"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(manager)

def main():
    command = sys.argv[0]
    print(command)

    if command == "rudleg-create":
        rudleg_create()
    else:
        sys.stdout.write("\033[31mUndefined command\033[0m")
