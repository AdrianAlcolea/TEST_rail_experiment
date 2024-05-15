#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Model ge"""

__version__ = "1.0.0"
__author__ = "Adrián Alcolea"
__email__ = "alcolea@unizar.es"
__maintainer__ = "Adrián Alcolea"
__license__ = "GPLv3"
__credits__ = ["Adrián Alcolea"]

class Ge:
    """Greater than or equal to class"""
    
    def __init__(self, value):
        self.value = value
    
    def inference(self, test_value):
        return 1 if test_value >= self.value else 0
