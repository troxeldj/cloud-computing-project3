from util import *

def main():
  # Clear Contents of result.txt
  clearFile("result.txt")
  # Word Counts -> results.txt
  appendToFile("result.txt", "-- Word Count --")
  appendToFile("result.txt", f"\tIF.txt: {wordCountOfFile('IF.txt')}")
  appendToFile("result.txt", f"\tAlwaysRememberUsThisWay.txt: {wordCountOfFile('AlwaysRememberUsThisWay.txt')}")

  # Most Common Words -> results.txt
  appendToFile("result.txt", "-- Most Common Words --")
  appendToFile("result.txt", f"\tIF.txt: {mostCommonWords('IF.txt', 3)}")
  appendToFile("result.txt", f"\tAlwaysRememberUsThisWay.txt (Contractions not Handled): {mostCommonWords('AlwaysRememberUsThisWay.txt', 3)}")
  appendToFile("result.txt", f"\tAlwaysRememberUsThisWay.txt (Contractions Handled): {mostCommonWords('AlwaysRememberUsThisWay.txt', 3, True)}")

  # IP Address -> results.txt
  appendToFile("result.txt", "-- IP Address --")
  appendToFile("result.txt", f"\t{getIPAddress()}")

if __name__ == "__main__":
  main()