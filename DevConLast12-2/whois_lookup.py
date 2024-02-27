# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 15:55:58 2023

@author: leena
"""

import whois
from colorama import init, Fore, Style

# Initialize colorama
init()

# Function to print colored text with a separator line
def print_colored_text(text, color):
    separator = Fore.GREEN + '-' * 40 + Style.RESET_ALL
    print(color + text)
    print(separator)

#domain = input("Enter the domain you want to perform WHOIS lookup on: ")

#w = whois.whois(domain)

def whois_forDomain(domain):
  #domain = input("Enter the domain you want to perform WHOIS lookup on: ")

  w = whois.whois(domain)
  print_colored_text("Domain registrar: " + str(w.registrar), Fore.YELLOW)
  print_colored_text("WHOIS server: " + str(w.whois_server), Fore.YELLOW)
  print_colored_text("Domain creation date: " + str(w.creation_date), Fore.YELLOW)
  print_colored_text("Domain expiration date: " + str(w.expiration_date), Fore.YELLOW)
  print_colored_text("Domain last updated: " + str(w.last_updated), Fore.YELLOW)
  print_colored_text("Name servers: " + str(w.name_servers), Fore.YELLOW)
  print_colored_text("Registrant name: " + str(w.name), Fore.YELLOW)
  print_colored_text("Registrant organization: " + str(w.org), Fore.YELLOW)
  print_colored_text("Registrant email: " + str(w.email), Fore.YELLOW)
  print_colored_text("Registrant phone: " + str(w.phone), Fore.YELLOW)