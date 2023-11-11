#!/usr/bin/python3
"""
The main entry point of the
command interpreter.
"""
import cmd
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """
    The main class of the console
    interpreter.
    """
    prompt = "(hbnb) "
    dictionary = storage.all()
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def emptyline(self):
        """
        Avoiding the default settings
        of an emptyline
        """
        pass

    def do_quit(self, arg):
        """
        Quit the shell with a command
        """
        return True

    def help_quit(self):
        """
        Help doc of quit command
        """
        print("Quits the shell\n")

    def do_EOF(self, arg):
        """
        Quit the shell with EOF
        """
        print()
        return True

    def help_EOF(self):
        """
        Help doc of EOF implementation
        """
        print("Quits the shell with the system's End of File (EOF) signal\n")

    def do_create(self, args):
        """
        Updates the instance of BaseModel and
        prints its new uuid4 ID.
        """
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        args = args.split(" ")

        the_obj = eval(args[0])()
        the_obj.save()
        print(the_obj.id)

    def do_show(self, args):
        """
        Prints the string representation
        of a specific class mentioned.
        """
        args = args.partition(" ")

        # ERROR_HANDLING
        if not args[0]:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if not args[2]:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[2]

        try:
            print(models.storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class
        name and id provided.
        """
        args = args.partition(" ")

        # ERROR_HANDLING
        if not args[0]:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if not args[2]:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[2]

        try:
            storage.all().pop(key)
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """
        Outputs all string representation of all
        Instances based or not on the class name.
        """
        str_rep = []

        if args:
            args = args.split(' ')[0]

            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return

            for key, value in storage.all():
                if key.split('.')[0] == args:
                    str_rep.append(str(value))
        else:
            for key, value in storage.all():
                str_rep.append(str(value))

        print(str_rep)

    def do_update(self, args):
        """
        Updates an instance based on the class
        name and id by adding or updating attribute.
        """
        args = args.partition(" ")

        if not args[0]:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not args[2]:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[2]

        if key not in storage.all():
            print("** no instance found **")
            return

        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:
            args = args[2]
            if args and args[0] == '\"':
                second_quote = args.find('\"', 1)
                attribute_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            if not attribute_name and args[0] != ' ':
                attribute_name = args[0]

            if args[2] and args[2][0] == '\"':
                attribute_value = args[2][1:args[2].find('\"', 1)]

            if not attribute_value and args[2]:
                attribute_value = args[2].partition(' ')[0]

            args = [attribute_name, attribute_value]

        dictionary = storage.all()[key]

        for i, attribute_name in enumerate(args):
            if (i % 2 == 0):
                attribute_value = args[i + 1]
                if not attribute_name:
                    print("** attribute name missing **")
                    return
                if not attribute_value:
                    print("** value missing **")
                    return

                if attribute_name in HBNBCommand.types:
                    attribute_value = HBNBCommand.types[attribute_name]
                    (attribute_value)

                dictionary.__dict__.update({attribute_name: attribute_value})

        dictionary.save()


interpreter = HBNBCommand()
interpreter.cmdloop()
