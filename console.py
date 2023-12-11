#!/usr/bin/python3
"""This is my command line interpreter."""
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) > "

    def do_quit(self, arg):
        """This quits or exits the program"""
        return True
    
    do_exit = do_quit

    HBNBCommand().cmdloop()
