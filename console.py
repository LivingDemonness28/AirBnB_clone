#!/usr/bin/python3
"""Defines the HBNBCommand console"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Defines command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb) "

    def do_quit(self.arg):
        """exit program command"""
        sys.exit(0)
    
    def do_EOF(self, arg):
        """Exit the program EOF(ctrl-D)"""
        print("")
        sys.exit(0)
    
    def emptyline(self):
        """Do nothing on empty line + ENTER"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
