#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file')
args = parser.parse_args()

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

# def as_dom(filename):
#     """this is extremely slow!!!"""
#     from bs4 import BeautifulSoup
#     counter = 0
#     hasRoot = False
#     with open(filename, 'r') as f:
#         first_line = f.readline()
#         hasRoot = "ROOT" in first_line
#
#     if not hasRoot:
#         line_prepender(filename, "<ROOT>");
#         with open(filename, "a") as myfile:
#             myfile.write("</ROOT>")
#
#     with open(filename) as file:
#         soup = BeautifulSoup(file, "xml")
#         for doc in soup.find_all("DOC"):
#             f = open(filename + "." + str(counter) + ".txt", "w")
#             counter += 1
#             print counter
#             f.write(str(doc))
#             f.close()

def as_stream(filename):
    """this is extremely fast!!!"""
    counter = 0
    with open(filename, 'r') as inputfile:
        outputfile = None
        for line in inputfile:
            # print line.strip()
            # first look for the end tag, this will
            # stop use from false detecting this as a start tag
            if "/DOC" in line:
                #write the text and close the file
                outputfile.write(line)
                outputfile.close()
            # look for the start tag
            elif "DOC" in line:
                # open a new file and start the text
                outputfile = open(filename + "." + str(counter) + ".txt", "w")
                counter += 1
                outputfile.write(line)
            # it is text, just write
            else:
                outputfile.write(line)

if __name__ == "__main__":
    as_stream(args.file)
