#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """ entry point of the command interpreter"""
    prompt = "(hnbn) "

    def do_quit(self, arg):
        """Quit command to exit program\n"""
        return True

    def do_EOF(self, arg):
        """Eof command to exit program\n"""
        print()
        return True

    def emptyline(self):
        """does nothing"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
