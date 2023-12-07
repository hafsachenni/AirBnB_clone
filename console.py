#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""
    prompt = "(hnbn) "
    dict_classes = {
            "BaseModel": BaseModel
            }

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id\n"""
        if not arg:
            print("** class name missing **")
            return
        try:
            instance = eval(arg)()
            instance.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.dict_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        str_repre = "{}.{}".format(args[0], args[1])
        if str_repre not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[str_repre])

    def do_destroy(self, args):
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.dict_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        str_repre = "{}.{}".format(args[0], args[1])
        if str_repre not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[str_repre]
        storage.save()
        
    def do_all(self, args):
        """prints str representation of all objects"""
        args = args.split()
        if args and args[0] not in HBNBCommand.dict_classes:
            print("** class doesn't exist **")
            return
        all_objects = [str(obj) for obj in storage.all().values()
                        if not args or type(obj).__name__ == args[0]]
        print(all_objects)




if __name__ == '__main__':
    HBNBCommand().cmdloop()
