#!/usr/bin/python3
"""This module is the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class for command interpreter"""
    prompt = '(hbnb) '

    def comm_quit(self, arg):
        """Quit command to return quit program function"""
        return True

    def comm_EOF(self, arg):
        """EOF command to return exit program function"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
