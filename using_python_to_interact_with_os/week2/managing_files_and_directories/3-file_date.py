#!/usr/bin/python3

###The file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified.###


import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, "w") as f:
      pass
  timestamp = os.path.getmtime(filename)

  # Convert the timestamp into a readable format, then into a string
  t = datetime.datetime.fromtimestamp(timestamp).date()
  # Return just the date portion
  # Hint: how many characters are in “yyyy-mm-dd”?
  return ("{}".format(t))

print(file_date("3-newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd
