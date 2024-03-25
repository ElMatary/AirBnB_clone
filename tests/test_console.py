#!/usr/bin/python3

import unittest
from models import storage
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import os


class TestHBNBCommand(unittest.TestCase):

    def test_class_doctest(self):

        self.assertTrue(len(HBNBCommand.__doc__) > 1)

    def setUp(self):

        self.console = HBNBCommand()

    def tearDown(self):

        pass

    def test_do_destroy(self):

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            x = f.getvalue().strip()
            self.assertNotEqual(x, "** class name missing **")
            self.assertNotEqual(x, "** class doesn't exist **")
            self.assertNotEqual(x, "** instance id missing **")
            self.assertNotEqual(x, "** no instance found **")

    def test_do_all(self):

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("all")
            x = f.getvalue().strip()
            self.assertNotEqual(x, "** class doesn't exist **")

    def test_do_show(self):

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"show BaseModel {obj_id}")
            x = f.getvalue().strip()
            self.assertNotEqual(x, "** class name missing **")
            self.assertNotEqual(x, "** class doesn't exist **")
            self.assertNotEqual(x, "** instance id missing **")
            self.assertNotEqual(x, "** no instance found **")

    def test_do_count(self):

        count = 0
        for key, values in storage.all().items():
            name = key.split(".")
            if name[0] == 'BaseModel':
                count += 1
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count BaseModel")
            x = f.getvalue().strip()
            self.assertEqual(x, str(count))

    def test_do_quit(self):

        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_do_create(self):

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            x = f.getvalue().strip()
            self.assertIsNotNone(x)
            self.assertNotEqual(x, "** class name missing **")
            self.assertNotEqual(x, "** class doesn't exist **")

    def test_do_EOF(self):

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(f.getvalue(), "")

    def test_do_help(self):

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            x = f.getvalue()
            self.assertIn("help", x)
            self.assertIn("EOF", x)
            self.assertIn("quit", x)
            self.assertIn("create", x)
            self.assertIn("count", x)
            self.assertIn("show", x)
            self.assertIn("destroy", x)
            self.assertIn("all", x)
            self.assertIn("update", x)

    def test_emptyline(self):

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_do_update(self):

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"update BaseModel {obj_id} name 'basemodel'")
            x = f.getvalue().strip()
            self.assertNotEqual(x, "** class name missing **")
            self.assertNotEqual(x, "** class doesn't exist **")
            self.assertNotEqual(x, "** instance id missing **")
            self.assertNotEqual(x, "** attribute name missing **")
            self.assertNotEqual(x, "** value missing **")
            self.assertNotEqual(x, "** no instance found **")

    def test_default(self):

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.show()")
            x = f.getvalue().strip()
            self.assertNotEqual(x, "** Unknown syntax:")


if __name__ == '__main__':
    unittest.main()
