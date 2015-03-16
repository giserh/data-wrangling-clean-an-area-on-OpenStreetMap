#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
The output should be a dictionary with the tag name as the key
and number of times this tag can be encountered in the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
#import sys
import xml.etree.ElementTree as ET
import pprint


FILENAME = 'vashon.osm' # Vashon, Washington


def count_tags(filename):
        # YOUR CODE HERE
        tags={}
        # find the count of tags in the document
        for event, elem in ET.iterparse(filename):
            if elem.tag in tags.keys():
                tags[elem.tag]=tags[elem.tag]+1
            else:
                tags[elem.tag]=1

        return tags

def test():

    tags = count_tags(FILENAME)
    pprint.pprint(tags)

    

if __name__ == "__main__":
    test()