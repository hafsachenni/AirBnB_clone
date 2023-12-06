#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""
    prompt = "(hnbn) "

    def do_quit(self, arg):
        """Quit command to exit program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit program\n"""
        print()
        return True

    def emptyline(self):
        """Doesn't execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
