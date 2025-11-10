import sys
import os
import subprocess

from RUDLeg.core_magic.CodeTemplateAndFunction import *
from RUDLeg.johnson import Joshua



build = Joshua(os.path.join("RUDLeg", "core_magic", "build.json"))
build_data = build.read_data()





def task_run(arguments):
        

    if len(arguments) < 2:
        sys.stdout.write("\033[31mUse the commmand: help\033[0m")
            
    else:
        command = arguments[1]

        #Create config line
        if command == "help":
            sys.stdout.write(
            "\033[33m" 
            "Defined commands are here:\n"
            "\n"
            "Execute and help commands:\n"
            "\trun : runs program...\n"
            "\tbuild : the command for build and prepare for running...\n"
            "\trun-build : build and execute program...\n"
            "\n"
            "Create config and files commands:\n"
            "\tcreate <dir_name> : creates a config templates with usefull files.\n"
            "\tcreate-tcpu <filename> : creates a test file pygame working on CPU.\n"
            "\tcreate-tgpu <filename> : creates a test file pygame + moderngl.\n"
            "\n"
            "Special and Information commands:\n"
            "\tversion : returns version of that Engine.\n"
            "\tshow : returns all information about that framework.\n"
            "\tnews : shows news about that Engine.\n"
            "\tcommunity : returns discord url\n"
            "\033[0m"
            )
            sys.exit(0)

        elif command == "create":
            #if you forgot write dir_name in < py helper.py create ... >
            if len(arguments) < 3:
                sys.stderr.write("\033[31mYou must have written dir_name\033[0m")
                sys.exit(1)

            #Creates directory in your project
            dir_name = arguments[2]
            dirs_config_name = ["shaders", "objects", "classes", "stuff", "data", "scenes", "assets", "soundmusic"]
            main_file = "SceneManager.py"

            inverter_file = "TheMainGame.py"
            file_dirs = (("Example.vert", "shaders"), ("Example.frag", "shaders"), ("YourData.json", "data"), ("ExampleScene1.py", "scenes", 1), ("ExampleScene2.py", "scenes", 2))
            os.makedirs(dir_name, exist_ok=True)

            #Create dirs
            for dir_config_name in dirs_config_name:
                path = os.path.join(dir_name, dir_config_name)
                os.makedirs(path, exist_ok=True)

            path_main = os.path.join(dir_name, main_file)
            with open(path_main, "w", encoding="UTF-8") as f:
                f.write(scene_code(dir_name=dir_name))


            for file_dir in file_dirs:
                #if that is shader
                if file_dir[1] == "shaders":
                    shader_path = os.path.join(dir_name, "shaders", file_dir[0])
                    with open(shader_path, "w", encoding="UTF-8") as f:
                        if os.path.splitext(shader_path)[1] == ".vert":
                            f.write(example_vert)
                        elif os.path.splitext(shader_path)[1] == ".frag":
                            f.write(example_frag)

                #if that is scene
                elif file_dir[1] == "scenes":
                    scene_path = os.path.join(dir_name, "scenes", file_dir[0])
                    with open(scene_path, "w", encoding="UTF-8") as f:
                        if file_dir[2] == 1:
                            f.write(example_code_1)
                        elif file_dir[2] == 2:
                            f.write(example_code_2)

                #if that is data
                elif file_dir[1] == "data":
                    data_path = os.path.join(dir_name, "data", file_dir[0])
                    with open(data_path, "w", encoding="UTF-8") as f:
                        f.write(example_data)
            

            with open(os.path.join("RUDLeg", "core_magic", inverter_file), "r", encoding="UTF-8") as f:
                code_writer = f.read()

                if "RGAME" in code_writer:
                    new_code = code_writer.replace("RGAME", f"{dir_name}")

                with open(os.path.join("RUDLeg", "core_magic", inverter_file), "w", encoding="utf-8") as f:
                    f.write(new_code)  

            with open(os.path.join("RUDLeg", "core_magic", inverter_file), "r", encoding="UTF-8") as f:
                code_writer = f.read()

                if "RSET" in code_writer:
                    new_code = code_writer.replace("RSET", f"os.path.join('{dir_name}', 'data', 'YourData.json')")

                with open(os.path.join("RUDLeg", "core_magic", inverter_file), "w", encoding="utf-8") as f:
                    f.write(new_code)

            
            sys.stdout.write(f"\033[32mYour config: {dir_name} succesfully created.\033[0m")
            sys.exit(0)



        elif command in ["create-tcpu", "create-tgpu"]:
            if len(arguments) < 3:
                sys.stderr.write("\033[31mYour forgot write a filename.\033[0m")
                sys.exit(1)

            if command == "create-tcpu":
                test_cpu = arguments[2]
                with open(f"{test_cpu}.py", "w", encoding="UTF-8") as f:
                    f.write(test_code_cpu)
                    sys.stdout.write(f"\033[32mYour file {test_cpu}.py succesfully created.\033[0m")
                    sys.exit(0)

            elif command == "create-tgpu":
                test_gpu = arguments[2]
                with open(f"{test_gpu}.py", "w", encoding="UTF-8") as f:
                    f.write(test_code_gpu)
                    sys.stdout.write(f"\033[32mYour file {test_gpu}.py succesfully created.\033[0m")
                    sys.exit(0)

            sys.exit(0)


            

        elif command in ["create-rd", "create-txt"]:
            if len(arguments) < 3:
                sys.stderr.write("\033[31mYour forgot write a filename.\033[0m")
                sys.exit(1)

            
            if command == "create-rd":
                readme_name = arguments[2]
                with open(f"{readme_name}.md", "w", encoding="UTF-8") as f:
                    sys.stdout.write(f"\033[32mYour file README was created.\033[0m")

            elif command == "create-txt":
                txt_name = arguments[2]
                with open(f"{txt_name}.txt", "w", encoding="UTF-8") as f:
                    sys.stdout.write(f"\033[32mYour file TXT was created.\033[0m")
            sys.exit(0)

                

        #Special line
        elif command == "news":
            sys.stdout.write(f"\033[32mMy first Game Engine: RUDLeg 0.1.0.0 was released!!!\033[0m")
            sys.exit(0)


        elif command == "version":
            sys.stdout.write("\033[32mRUDLeg - 0.1.4.5\033[0m")
            sys.exit(0)

        elif command == "show":
            sys.stdout.write("\033[32mRUDLeg:\n" \
            "version: 0.1.0.0\n" \
            "author: TheDreadMatrix\n" \
            "backend: pygame+moderngl\n" \
            "description: I creates my first ever GameEngine and i m happy!!!\033[0m")
            sys.exit(0)

        elif command == "community":
            sys.stdout.write("\033[32mMy discord server: https://discord.gg/wCex59HJKP\033[0m")
            sys.exit(0)

        elif command == "hello":
            sys.stdout.write("\033[31mRSTAKAPZTV#N\033[0m")
            sys.exit(1)

        


        #Execute line
        elif command == "on-debug":
            pass

        elif command == "off-debug":
            pass


        elif command == "run":
            if build_data["was_built"]:
                build_data["was_built"] = False
                build.save_data(build_data)
  

                if build_data["debug"]:
                     subprocess.Popen([sys.executable, os.path.join("RUDLeg", "core_magic", "DebugManager.py")])

                    
                try:
                    from RUDLeg.core_magic.TheMainGame import MyGame
                    MyGame().run()
                except ModuleNotFoundError:
                    sys.stderr.write("\033[31mYou should create project at first.\033[0m]")
                    sys.exit(0)
            else:
                sys.stderr.write("\033[31mYou need to build that config: build or use build-run\033[0m")
                sys.exit(1)

        elif command == "build":
            if len(arguments) < 3:
                sys.stderr.write("\033[31mI expected a dir_name\033[0m")
                sys.exit(1)


            dir_name = arguments[2]

            locate_danger(dir_name=dir_name)

            if not build_data["was_built"]:
                build_data["was_built"] = True
                build.save_data(build_data)
                sys.stdout.write("\033[32mYour have built succesfully.\033[0m")
                sys.exit(0)
            else:
                sys.stdout.write("\033[33mYour have built your config again...\033[0m")
                sys.exit(1)



        elif command in ["build-run", "call", "rub"]:
            if len(arguments) < 3:
                sys.stderr.write("\033[31mI expected a dir_name\033[0m")
                sys.exit(1)
            
            dir_name = arguments[2]
            locate_danger(dir_name=dir_name)


            build_data["was_built"] = False
            build.save_data(build_data)

            if build_data["debug"]:
                subprocess.Popen([sys.executable, os.path.join("RUDLeg", "core_magic", "DebugManager.py")])

            try:
                from RUDLeg.core_magic.TheMainGame import MyGame
                MyGame().run()
            except ModuleNotFoundError:
                    sys.stderr.write("\033[31mYou should create project at first.\033[0m")
                    sys.exit(0)



        else:
            sys.stderr.write(f"\033[31mUndefined command as : {command}\033[0m")
            sys.exit(1)


