#!/usr/bin/python3
"""This is my command line interpreter."""
import cmd
import json
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) > "

    def do_quit(self, arg):
        """This quits or exits the program"""
        return True
    
    def do_EOF(self, arg):
        """Handles EOF (CTR+D) to quit the console"""
        return True

    def emptyline(self):
        """Do nothing if input is empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it, and prins its id"""

        if not arg:
            print("**class name missing**")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("**class doesn't exist**")
    
    def do_show(self, arg):
        """Prints a string representation of an instance."""
        if not arg:
            print("**class name missing**")
            return
        args = args.split()
        class_name = args[0]

        if class_name not in storage.classes():
            print("**class does'nt exist**")
            return
        if len(args) < 2:
            print("**instance id is missing**")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id

        if key not in storage.all():
            print("**no instance found**")
        else:
            print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""

        if not arg:
            print("**class name missing**")
            return
        args = arg.split()
        class_name = args[0]

        if class_name not in storage.classes():
            print("**class doesn't exits**")
            return

        if len(args) < 2:
            print("** instance id missing**")
            return
        
        instance_id =args[1]
        key = class_name + "." + instance_id

        if key not in storage.all():
            print("**no instance found**")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of instances."""

        objects = storage.all()

        if not arg:
            print([str(objs[obj]) for obj in objects])
            return

        args = args.split()
        class_name = args[0]

        if class_name not in storage.classes():
            print("**class doesn't exists**")
            return
        filtered_objects = \
                [str(objects[obj]) for obj in objects if class_name in obj]
        print(filtered_objects)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = args[0] + "." + instance_id

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]

        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
