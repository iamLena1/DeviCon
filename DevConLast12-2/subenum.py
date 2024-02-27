import dns.resolver
import concurrent.futures
from dns.exception import DNSException
import subprocess
from colorama import *
from colorama import Fore
red1=Fore.LIGHTRED_EX
##
from colorama import Fore, Style 
Lred=Fore.LIGHTRED_EX
reset=Style.RESET_ALL


def SubDomain(domain, max_subdomains=None, wordlist_filename='wordlist.txt'):
    # Read the content of the wordlist file
    with open(wordlist_filename, 'r') as file:
        content = file.read()

    # Use strip() to remove leading and trailing whitespaces from each line in the wordlist
    subdomains = [line.strip() for line in content.splitlines()]

    # Construct the full domain to check subdomains against
    full_domain = f"{domain.strip()}."

    # Generate subdomains by combining with the full domain
    subdomains = [f"{i}.{full_domain}" for i in subdomains]

    # Limit the number of subdomains if max_subdomains is specified
    if max_subdomains is not None:
        subdomains = subdomains[:max_subdomains]

    results = []

    def check_subdomain(subdomain):
        # Construct the full URL for the subdomain
        url1 = f"{subdomain}"

        # Check DNS resolution for the subdomain
        if check_dns_resolution(url1):
            results.append(f"Valid domain: {url1}")
        else:
            results.append(f"{Lred}Invalid domain: {url1}{reset}")

    # Use multithreading to concurrently check DNS resolution for subdomains
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(check_subdomain, subdomains)

    return results

def save_results_to_file(results, filename='discovered_subdomains.txt'):
    # Append the results to the specified file
    with open(filename, 'a') as file:
        for result in results:
            file.write(result + '\n')

def print_summary(results):
    # Extract valid subdomains from the results
    valid_subdomains = [result for result in results if result.startswith('Valid domain')]

    print(f"Total discovered subdomains: {len(results)}")
    print(f"Valid subdomains: {len(valid_subdomains)}")

def check_dns_resolution(subdomain):
    # Define the nslookup command to check DNS resolution
    command = ["nslookup", subdomain]

    try:
        # Run the nslookup command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout + result.stderr

        # Check if the output contains "Non-authoritative answer" to determine DNS record validity
        if "Non-authoritative answer" in result.stdout:
            return True  # Valid DNS record
        else:
            return False, output  # No valid DNS record
    except subprocess.CalledProcessError as e:
        return False, f"Error running nslookup: {e}"





