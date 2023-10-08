#!/usr/bin/python3
""" This module contains the CLI-like 
    command environment for data manipulation"""
import models
import cmd, sys


class HBNBCommand(cmd.Cmd):
    """ This class defines the attributes and methods of a Command Line
        environment that can manipulate JSON-stored objects """
    prompt = "(hbnb) "

    def default(self, line):
        """ This method determines CLI behavior
            when 'quit' or 'EOF' are encountered in args """
        if line == "quit" or line == "EOF":
            return True

        return super().default(line)

    def emptyline(self):
        """ This method determines CLI behavior when empty line is passed"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
