#!/usr/bin/python3
"""This module is the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class for command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to return quit program function"""
        return True

    def do_EOF(self, arg):
        """EOF command to return exit program function"""
        return True

    def  empty_line(self):
        """Empty line handeler"""
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
