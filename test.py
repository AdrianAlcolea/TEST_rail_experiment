#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test file"""

__version__ = "1.0.0"
__author__ = "Adrián Alcolea"
__email__ = "alcolea@unizar.es"
__maintainer__ = "Adrián Alcolea"
__license__ = "GPLv3"
__credits__ = ["Adrián Alcolea"]

import os
import json
import numpy as np
from model.ge import Ge

def main():
    
    # Load model
    model = Ge(5)
    
    # Get data
    with open('dataset/data.txt', 'r') as f:
        data = [int(line) for line in f]
    
    # Get labels
    with open('dataset/labels.txt', 'r') as f:
        labels = [int(line) for line in f]
    
    # Launch model
    results = [model.inference(d) for d in data]
    
    # Save results
    results_dict = {k: v for k, v in zip(data, results)}
    output_file = 'output-temp/metrics.json'
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        json.dump(results_dict, f)
    
    # Print accuracy
    acc = (np.array(results) == labels).sum() / len(results)
    print(f"The accuracy is: {acc*100}%")

if __name__ == "__main__":
    main()
