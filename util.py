from typing import List
from collections import Counter
import re
import contractions # import contractions library

'''
FileContentToString
  - Reads the content of a file and returns it as a string

Parameters:
  - filePath: str
    - The path to the file to read
  - withContractions: bool
    - Whether to expand contractions in the file content

Returns:
  - str
    - The content of the file as a string
'''
def fileContentToString(filePath: str, withContractions: bool = False) -> str:
  with open(filePath, 'r') as f:
    if(withContractions):
      return contractions.fix(f.read())
    return f.read()

'''
WordCountOfFile
  - Reads the content of a file and returns the number of words in it

Parameters:
  - filePath: str
    - The path to the file to read
  - withContractions: bool
    - Whether to expand contractions in the file content
Returns:
  - int
    - The number of words in the file
'''
def wordCountOfFile(filePath: str, withContractions: bool = False) -> int:
  return len(fileContentToString(filePath, withContractions).split())

'''
mostCommonWords
  - Reads the content of a file and returns the n most common words in it and their counts

Parameters:
  - filePath: str
    - The path to the file to read
  - n: int
    - The number of most common words to return

Returns:
  - List[str]
    - The n most common words in the file
'''
def mostCommonWords(filePath: str, n: int, withContractions: bool = False) -> List[str]:
    # Read the file content
    text = fileContentToString(filePath, withContractions)
    words = re.findall(r'\w+', text.lower())

    word_count = Counter(words)
    most_common = word_count.most_common(n)
    return most_common 

'''
getIPAddress
  - Returns the IP address of the machine

Returns:
  - str
    - The IP address of the machine
'''
def getIPAddress():
    import socket
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return IPAddr

'''
appendToFile
  - Appends data to a file

Parameters:
  - filePath: str
    - The path to the file to write to
  - data: str
    - The data to append to the file
'''
def appendToFile(filePath: str, data: str):
    with open(filePath, 'a') as f:
        f.write(data)
        f.write('\n')
        f.close()

'''
clearFile
  - Clears the contents of a file

Parameters:
  - filePath: str
    - The path to the file to clear
'''
def clearFile(filePath: str):
    from os.path import exists
    if(not exists(filePath)):
       return
    with open(filePath, 'r+') as f:
       f.truncate(0)