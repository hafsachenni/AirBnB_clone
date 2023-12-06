#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """ entry point of the command interpreter"""
    prompt = "(hnbn) "

    def do_quit(self, arg):
        """quit command to exit program"""
        return True

    def do_EOF(self, arg):
        """eof command to exit program"""
        print()
        return True

    def emptyline(self):
        """does nothing"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
