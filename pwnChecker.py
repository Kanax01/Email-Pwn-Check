#!/bin/env python3

import os
import sys
import requests
from colorama import Fore, Style
import hashlib
import pyfiglet
import argparse

# cli args
parser = argparse.ArgumentParser()
parser.add_argument("target", nargs = "?", type = str)
args = parser.parse_args()

# global vars
target = args.target
num_pwn = []
num_breach = 0

# art
figlet = pyfiglet.figlet_format("Email Breach Checker")


class scraper: # now that i think of it why did I put scraper in a class, life is full of mistories
  
  @classmethod
  def scraper(cls):
    hash = hashlib.sha1(target.encode()).hexdigest().upper()
    prefix = hash[:5]
    suffix = hash[5:]
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    print(response.status_code)
    print(Fore.YELLOW + Style.BRIGHT + "Hashes:")
    print(response.text)
    if response.status_code == 200:
      for line in response.text.splitlines():
        if line.startswith(suffix):
          num_pwn.append(line)
          num_breach + 1

      for pwn in num_pwn:
          print(Fore.RED + Style.BRIGHT + pwn)
      print(Fore.RED + Style.BRIGHT + "\n\n")
      print(f"Target: {target}")
      print(f"Full Hash: {hash}")
      print(f"Prefix: {prefix}")
      print(f"URL: https://api.pwnedpasswords.com/range/{prefix}")
      print(f"Your email has been found in {num_breach} data breaches")
      if not num_pwn:
        print("Your account is safe but remeber to check frequently")
      else:
        print("CHANGE YOUR PASSWORD YOUR ACCOUNT MAY BE COMPROMISED")

def helpScreen():
  print((Fore.RED + Style.BRIGHT + "[1]" + Fore.BLUE + Style.BRIGHT + " target <-- Email To Check"))



def main():
  print(Fore.GREEN + Style.BRIGHT + figlet)
  if not args.target:
      helpScreen()
      exit()

  scraper.scraper()
  
if __name__ == "__main__":
  main()
