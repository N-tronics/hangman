"""
The main file that calls the Menu class.
"""

from Menu import Menu

if __name__ == '__main__':
    menu = Menu('images', 'words.json')
    menu.main()
