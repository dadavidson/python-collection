#!/usr/bin/env python3
"""
# Instructions
Convert boolean values to strings 'Yes' or 'No'
"""

__author__ = "Daniel Davidson"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    class Boolean(object):
        def bool_to_word(bvalue):
            if bvalue == 'True' or bvalue == 'true':
                bvalue = True
                return 'Yes'
            if bvalue == 'False' or bvalue == 'false':
                bvalue = False
                return 'No'
            else:
                return 'Error'
    bInput = input("Enter a boolean value: ")
    bOutput = Boolean.bool_to_word(bInput)
    print(bOutput)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
