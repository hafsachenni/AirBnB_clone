#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """ entry point of the command interpreter"""
    prompt = "(hnbn) "
    dict_classes = {
            "BaseModel": BaseModel
            }


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


    def do_create(self, args):
        """creates a new instance of the given class"""
        args = args.split()
        if not args:
            print("**class name missing**")
            return
        if args[0] not in HBNBCommand.dict_classes:
            print("** class doesn't exist **")
            return

        new_object = HBNBCommand.dict_classes[args[0]]()
        storage.save()
        print(new_object.id)


    def do_show(self, args):
        """prints str representation of an obj"""
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
        """deletes objects based on id and class name"""
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
