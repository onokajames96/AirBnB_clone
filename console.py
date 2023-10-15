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
        args = shlex.split(arg)
        if not args:
            print('** class name missing **')
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print('** instance id missing **')
            return

        key = class_name + '.' + args[1]
        instance_dict = storage.all()
        if key in instance_dict:
            if len(args) > 2:
                if len(args) < 4:
                    print('** value missing **')
                else:
                    attribute = args[2]
                    value = args[3][1:-1]
                    setattr(instance_dict[key], attribute, value)
                    instance_dict[key].save()
            else:
                print('** attribute name missing **')
        else:
            print('** no instance found **')


if __name__ == "__main__":
    HBNBCommand().cmdloop()
