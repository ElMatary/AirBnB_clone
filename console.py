#!/usr/bin/python3
"""module to make command interpreter"""


import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models import storage


class HBNBCommand(cmd.Cmd):
    """New class commands"""

    prompt = "(hbnb) "
    all_classes = ["BaseModel", "User", "City", "State",
                   "Amenity", "Review", "Place"]
    cmds = ["EOF", "help", "quit", "create", "count",
            "show", "destroy", "all", "update"]

    def do_EOF(self, line):
        """EOF command to exit"""

        print()
        return True

    def do_quit(self, line):
        """Quit command to exit"""

        return True

    def do_help(self, line):
        """Help command to show docstring for a command
        """
        cmd.Cmd.do_help(self, line)

    def emptyline(self):
        """emptyline command to execute"""

        pass

    def do_create(self, line):
        """Creates a new instance"""

        if line:
            if line not in HBNBCommand.all_classes:
                print("** class doesn't exist **")
            else:
                instance = eval(f"{line}()")
                instance.save()
                print(instance.id)
        else:
            print("** class name missing **")

    def do_count(self, line):
        """Count command"""
        count = 0
        line_list = line.split()
        if line_list[0] in self.all_classes:
            for key in models.storage.all().keys():
                if line_list[0] in key:
                    count += 1
        print(count)

    def do_show(self, line):
        """Prints the string"""
        line_list = line.split()
        if not line_list:
            print("** class doesn't exist **")
            return
        elif line_list[0] not in HBNBCommand.all_classes:
            print("** class name missing **")
            return
        elif len(line_list) < 2:
            print("** instance id missing **")
            return
        else:
            objs = models.storage.all()
            key = line_list[0] + '.' + line_list[1]
            if key not in objs.keys():
                print("** no instance found **")
                return
            else:
                print(objs[key].__str__())

    def do_all(self, line):
        """print all string representation"""
        line_list = line.split()

        if not len(line_list) or line_list[0] in HBNBCommand.all_classes:
            string_list = []
            objs = models.storage.all()
            for obj in objs.values():
                string_list.append(obj.__str__())
            print(string_list)
        else:
            print("** class doesn't exist **")
            return

    def do_update(self, line):
        """Update instance by name and id"""
        line_list = line.split()
        if not line_list:
            print("** class doesn't exist **")
            return
        elif line_list[0] not in HBNBCommand.all_classes:
            print("** class name missing **")
            return
        elif len(line_list) < 2:
            print("** instance id missing **")
            return
        elif len(line_list) < 3:
            print("** attribute name missing **")
            return
        elif len(line_list) < 4:
            print("** value missing **")
            return
        else:
            objs = models.storage.all()
            key = "{}.{}".format(line_list[0], line_list[1])
            if key not in objs.keys():
                print("** no instance found **")
                return
            setattr(objs[key], line_list[2], eval(line_list[3]))
            objs[key].save()

    def default(self, line):
        """Executes a command"""

        all_words = line.split('.')
        if "(" in all_words[-1] and ")" in all_words[-1]:
            methods_and_args = all_words[-1].split("(")
            method = methods_and_args[0]
            args = methods_and_args[1].rstrip(")").split(",")

            if method not in self.cmds:
                print("** Unknown syntax:", method)
                return

            cls_name = ".".join(all_words[:-1])
            if cls_name not in self.cls_objs:
                print("** class doesn't exist **")
                return
            function = getattr(self, "do_" + method)
            all_args = " ".join([cls_name] + args)
            function(all_args)

        else:
            command = all_words[0]
            if command not in self.cmds:
                print("** Unknown syntax:", command)
                return

            function = getattr(self, "do_" + command)
            function(" ".join(all_words[1:]))

    def do_destroy(self, line):
        """Deletes instance by class name and id"""
        line_list = line.split()
        if not line_list:
            print("** class name missing **")
            return
        elif line_list[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        elif len(line_list) < 2:
            print("** instance id missing **")
            return
        else:
            objs = models.storage.all()
            key = "{}.{}".format(line_list[0], line_list[1])
            if key not in objs.keys():
                print("** no instance found **")
                return
            else:
                del objs[key]
                models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
