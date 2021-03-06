#!/usr/bin/env python

import csv
import upyble

with open('{}/SI_units.csv'.format(upyble.__path__[0]), 'r') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=['Quantity', 'Unit', 'Symbol'])
    SI_units_dict = {'Quantity': [], 'Unit': [], 'Symbol': []}
    for row in reader:
        # print(row['Dec'], row['Hex'], row['Company'])
        SI_units_dict['Quantity'].append(row['Quantity'])
        SI_units_dict['Unit'].append(row['Unit'])
        SI_units_dict['Symbol'].append(row['Symbol'])

ble_SI_units_dict = dict(zip(SI_units_dict['Unit'], SI_units_dict['Symbol']))

# DATA_FORMAT_STRUCT_DICT:

DATA_FMT = {
    "sint8": "b",
    "uint8": "B",
    "sint16": "h",
    "uint16": "H",
    "uint24": "k",
    "sint32": "i",
    "uint32": "I",
    "uint40": "j",
    "uint48": "J",
    "utf8s": "utf8",
    "8bit": "B",
    "16bit": "h",
    "float64": "d",
    "variable": "X",
    "gatt_uuid": "X",
    "boolean": "?",
    "32bit": "I",
    "FLOAT": "F",
    "24bit": "k",
    "SFLOAT": "S",
    "sint24": "K",
    "nibble": "Y",
    "2bit": "B",
    "uint128": "z",
    "uint12": "o",
    "4bit": "Y",
    "characteristic": "X",
    "float32": "f"
}
