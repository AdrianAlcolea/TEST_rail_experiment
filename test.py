#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test file"""

__version__ = "1.0.0"
__author__ = "Adrián Alcolea"
__email__ = "alcolea@unizar.es"
__maintainer__ = "Adrián Alcolea"
__license__ = "GPLv3"
__credits__ = ["Adrián Alcolea"]

from argparse import ArgumentParser, RawDescriptionHelpFormatter

def _parse_args():
    """Analyses the received parameters and returns them organised.
    
    Takes the list of strings received at sys.argv and generates a
    namespace assigning them to objects.
    
    Returns
    -------
    out : namespace
        The namespace with the values of the received parameters
        assigned to objects.
    """
    
    # Generate the parameter analyser
    parser = ArgumentParser(description = __doc__,
                            formatter_class = RawDescriptionHelpFormatter)
    
    # Add arguments
    parser.add_argument("text",
                        type=str,
                        help="Text to print.")
    
    # Return the analysed parameters
    return parser.parse_args()

# =============================================================================

def main(text):
    
    # Prints the text received as an argument
    print(text)
    

if __name__ == "__main__":
    
    # Parse args
    args = _parse_args()
    
    # Launch main function
    main(args.text)
