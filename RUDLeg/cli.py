import sys
from RUDLeg.core_magic.CodeTemplateAndFunction import manager

def rudleg_create():
    filename = "manager.py"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(manager)

def main():
    rudleg_create()
