import unittest
import linux_menu
import getpass
import subprocess as cmd


class TestGenerateUsername(unittest.TestCase):
    def test_generate_username(self):
        """
        Test Generate Username Function
        """
        self.assertEqual(linux_menu.generate_username(), getpass.getuser())

    # Split following Unit test into seperate Unit tests

    def test_generate_menu(self):
        """
        Test Generate Menu - check it is a list
        """
        menu = linux_menu.generate_menu()
        self.assertIsInstance(menu, list)

    def test_generate_menu_item(self):
        """
        Test Generate Menu - check each item is a list
        """
        menu = linux_menu.generate_menu()
        for item in menu:
            self.assertIsInstance(item, list)

    def test_generate_menu_item_qty(self):
        """
        Test Generate Menu - check each item is a list with 3 items
        """
        menu = linux_menu.generate_menu()
        for item in menu:
            self.assertIs(len(item), 3)

    def test_generate_menu_item_1(self):
        """
        Test Generate Menu - check first item is an Integer
        """
        menu = linux_menu.generate_menu()
        for item in menu:
            self.assertIsInstance(item[0], int)

    def test_generate_menu_item_2(self):
        """
        Test Generate Menu - check second item is a string
        """
        menu = linux_menu.generate_menu()
        for item in menu:
            self.assertIsInstance(item[1], str)

    def test_generate_menu_item_3(self):
        """
        Test Generate Menu - check third item is a string
        """
        menu = linux_menu.generate_menu()
        for item in menu:
            self.assertIsInstance(item[2], str)

    def test_grab_os(self):
        osversion = "Unknown"
        try:
            with open("/etc/redhat-release") as file:
                osversion = file.read()
        except FileNotFoundError:
            next
        self.assertEqual(osversion, linux_menu.grab_os())


if __name__ == '__main__':
    cmd.call("clear", shell=False)
    print("Running Unit tests for Linux Menu Application")
    unittest.main()
