import sys
from RUDLeg.core_magic.ExecuteCommand import task_run

#The Rudl EngineC
def main():
    """
    Main commands to create game-dev config:

    --help : returns list of commands
    use that command and other things your need to do yourself.

    Huh.. alright i can help with that.

    use command:

    --create <dirname> : to create config gamedev
    --run : to run program
    --build : the usefull function you nedd write before execute program

    --build-run : simple command

    --dekstop : unfinished 
    

    Please if you want to create a game you need to know about Pygame-ce and Moderngl with GLSL syntax.

    """
    task_run(sys.argv)


if __name__ == "__main__":
    main()
