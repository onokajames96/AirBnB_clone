#!/usr/bin/python3
"""Defination of AirBnB Console."""
import cmd
import sys
import json
import os
from models import storage
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command-line interface for Holberton AirBnB project."""
    prompt = "(hbnb) "
    _classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """ Quit the console."""
        return True

    def do_EOF(self, arg):
        """ Exit on EOF (Ctrl+D)."""
        print('')
        return True

    def emptyline(self):
        """Do nothing on empty input """
        pass

    def do_create(self, arg):
        """Create a new instance of a class."""
        if not arg:
            print('** class name missing **')
            return

        class_name = arg.split()[0]
        if class_name in self.classes:
            new_instance = self.classes[class_name]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show the string representation of an instance."""
        if not arg:
            print('** class name missing **')
            return

        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print('** instance id missing **')
            return

        key = args[0] + '.' + args[1]
        instance_dict = storage.all()
        if key in instance_dict:
            print(instance_dict[key])
        else:
            print('** no instance found **')

    def do_destroy(self, arg):
        """Delete an instance"""
        if not arg:
            print('** class name missing **')
            return

        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print('** instance id missing **')
            return

        key = args[0] + '.' + args[1]
        instance_dict = storage.all()
        if key in instance_dict:
            del instance_dict[key]
            storage.save()
        else:
            print('** no instance found **')

    def do_all(self, arg):
        """Print all instances."""
        instance_dict = storage.all()

        if not arg:
            print([str(instance) for instance in instance_dict.values()])
        elif arg in self.classes:
            print([str(instance) for key, instance in instance_dict.items() if arg in key])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance attr."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for key, value in eval(argl[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = valtype(value)
                else:
                    obj.__dict__[key] = value
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
