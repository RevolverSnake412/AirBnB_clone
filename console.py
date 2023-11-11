#!/usr/bin/python3
"""
The main entry point of the
command interpreter.
"""
import cmd
import json
import re
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    The main class of the console
    interpreter.
    """
    prompt = "(hbnb) "
    dictionary = storage.all()

    def errors(self, args, argc):
        classes = ["BaseModel"]

        if not args:
            print("** class name missing **")
            return 1

        args = args.split()

        if argc >= 1 and args[0] not in classes:
            print("** class doesn't exist **")
            return 1
        elif argc == 1:
            return 0

        if argc >= 2 and len(args) < 2:
            print("** instance id missing **")
            return 1

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
        if (self.errors(args, 1) == 1):
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
        if (self.errors(args, 2) == 1):
            return

        args = args.split()
        dictionary = storage.all()

        key = args[0] + '.' + args[1]

        if key in dictionary:
            print(dictionary[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class
        name and id provided.
        """
        if (self.errors(args, 2) == 1):
            return

        args = args.split()
        dictionary = storage.all()

        key = args[0] + '.' + args[1]

        if key in dictionary:
            del dictionary[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """
        Outputs all string representation of all
        Instances based or not on the class name.
        """
        dictionary = storage.all()

        if not args:
            print([str(key) for key in dictionary.values()])
            return

        if (self.errors(args, 1) == 1):
            return

        print([str(value) for value in dictionary.values()
               if value.__class__.__name__ == args[0]])

    def do_update(self, args):
        """
        Updates an instance based on the class
        name and id by adding or updating attribute.
        """
        if (self.errors(args, 4) == 1):
            return

        args = args.split()
        dictionary = storage.all()

        for i in range(len(args[1:]) + 1):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")

        key = args[0] + '.' + args[1]
        attribute_key = args[2]
        attribute_value = args[3]

        try:
            attr_value = self.convert_attribute_value(attr_value)
        except ValueError:
            print("Entered wrong value type")
            return

        class_attributes = type(dictionary[attribute_key]).__dict__

        if attribute_key in class_attributes.keys():
            try:
                attribute_value = type(class_attributes[attribute_key])
                (attribute_value)
            except Exception:
                print("Entered wrong value type")
                return

        setattr(dictionary[key], attribute_key, attribute_value)
        storage.save()


interpreter = HBNBCommand()
interpreter.cmdloop()
