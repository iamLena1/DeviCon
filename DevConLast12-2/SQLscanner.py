
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from pprint import pprint
import datetime
# Initialize an HTTP session & set the browser user-agent
session = requests.Session()
session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

def get_all_forms(url):
    """for a Given url, it returns all forms from the HTML content"""
    soup = bs(session.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    """
    Extracts all possible useful information about an HTML form
    """
    details = {}
    # Get the form action (target URL)
    try:
        action = form.attrs.get("action").lower()
    except:
        action = None
    # Get the form method (POST, GET, etc.)
    method = form.attrs.get("method", "get").lower()
    # Get all the input details such as type and name
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    # Put everything into the resulting dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def is_vulnerable(response):
    """function that return a boolean to determines whether a page
    is SQL Injection vulnerable from its response"""
    errors = {
        # MySQL
        "you have an error in your sql syntax;",
        "warning: mysql",
        # SQL Server
        "unclosed quotation mark after the character string",
        # Oracle
        "quoted string not properly terminated",
    }
    for error in errors:
        # If you find one of these errors, return True
        if error in response.content.decode().lower():
            return True
    # No error detected
    return False

def scan_sql_injection(url, verbose=False):
    # Test on URL
    for quote_char in "\"'":
        # Add quote/double quote character to the URL
        new_url = f"{url}{quote_char}"
        if verbose:
            print("[!] Trying", new_url)
        # Make the HTTP request
        response = session.get(new_url)

        if is_vulnerable(response):
            # SQL Injection detected on the URL itself,
            # no need to proceed for extracting forms and submitting them
            print("[+] SQL Injection vulnerability detected, link:", new_url)
            if verbose:
                print("[DEBUG] Response Content:", response.content.decode())
            log_vulnerability(new_url)
            return

    # Test on HTML forms
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    for form in forms:
        form_details = get_form_details(form)
        for quote_char in "\"'":
            # The data body we want to submit
            data = {}
            for input_tag in form_details["inputs"]:
                if input_tag["type"] == "hidden" or input_tag["value"]:
                    # Any input form that is hidden or has some value,
                    # just use it in the form body
                    try:
                        data[input_tag["name"]] = input_tag["value"] + quote_char
                    except:
                        pass
                elif input_tag["type"] != "submit":
                    # All others except submit, use some junk data with a special character
                    data[input_tag["name"]] = f"test{quote_char}"
            # Join the URL with the action (form request URL)
            form_url = urljoin(url, form_details["action"])
            if form_details["method"] == "post":
                response = session.post(form_url, data=data)
            elif form_details["method"] == "get":
                response = session.get(form_url, params=data)
            # Test whether the resulting page is vulnerable
            if is_vulnerable(response):
                print("[+] SQL Injection vulnerability detected, link:", form_url)
                print("[+] Form:")
                pprint(form_details)
                if verbose:
                    print("[DEBUG] Response Content:", response.content.decode())
                log_vulnerability(form_url, form_details)
                break

def log_vulnerability(url, form_details=None):
    with open("vulnerability_log.txt", "a") as log_file:
        log_file.write(f"Vulnerability detected on URL: {url}\n")
        if form_details:
            log_file.write("Form Details:\n")
            pprint(form_details, stream=log_file)

        log_file.write(f"Timestamp: {datetime.datetime.now()}\n\n")

