import re   #Regular expression
from colorama import Fore, Style    #To add styles and colors in the output
import whois_lookup
import SQLscanner
import instaRecon
import subenum
import TCP_Lookup
import UDP_Lookup
import HOST_Lookup
import UserName_Lookup
cyan=Fore.CYAN
red=Fore.RED
yellow=Fore.YELLOW
green=Fore.GREEN
blue=Fore.BLUE
black=Fore.BLACK
white=Fore.WHITE
magenta=Fore.MAGENTA
Lcyan=Fore.LIGHTCYAN_EX
Lred=Fore.LIGHTRED_EX
Lyellow=Fore.LIGHTYELLOW_EX
Lgreen=Fore.LIGHTGREEN_EX
Lblue=Fore.LIGHTBLUE_EX
Lblack=Fore.LIGHTBLACK_EX
Lwhite=Fore.LIGHTWHITE_EX
Lmagenta=Fore.LIGHTMAGENTA_EX
reset=Style.RESET_ALL


#print(f"{cyan}Cyan {red}red {yellow}yellow {green}green {blue}blue {black}black {white}white {magenta}magenta {reset}")
#print(f"{Lcyan}Lcyan {Lred}Lred {Lyellow}Lyellow {Lgreen}Lgreen {Lblue}Lblue {Lblack}Lblack {Lwhite}Lwhite {Lmagenta}Lmagenta {reset}")
def poster():
    
 print(f"""{Lblue}
                                ▄▄                                
██████╗ ███████╗██╗   ██╗██╗ ██████╗ ██████╗ ███╗   ██╗
██╔══██╗██╔════╝██║   ██║██║██╔════╝██╔═══██╗████╗  ██║
██║  ██║█████╗  ██║   ██║██║██║     ██║   ██║██╔██╗ ██║
██║  ██║██╔══╝  ╚██╗ ██╔╝██║██║     ██║   ██║██║╚██╗██║
██████╔╝███████╗ ╚████╔╝ ██║╚██████╗╚██████╔╝██║ ╚████║
╚═════╝ ╚══════╝  ╚═══╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝                                                        
{reset}""") 
 

 print(f"""{red}
       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⡠⢴⣒⡮⠭⠉⠉⠉⠒⠢⢄⡀⠀⠀⠀⠀⠀⠀
       ⠀⠀⠀⠀⠀⢸⢦⡀⠀⢀⠔⢫⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⢀⢼⡆
       ⠀⠀⠀⠀⠀⢾⡄⠈⠙⠓⠲⡌⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠛⠈⠁⣸⡇
       ⠀⠀⠀⠀⠀⠸⣿⣦⣤⣀⣀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣀⣤⣾⣿⠃
       ⢳⣲⡤⢄⣀⡀⠙⢿⣿⣿⡏⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠈⢻⡿⡟⠃⠀
       ⠀⢳⡙⢲⠼⡁⠀⢸⣿⣿⠟⣋⣉⠉⠉⠓⠦⡤⠖⠋⠉⠁⣉⣉⠢⡀⠀⡇⠀⠀
       ⠀⠀⠓⠉⠳⡌⢆⠸⣿⡏⠀⠀⠈⠑⠦⣀⠀⠀⠀⣠⠴⢋⡀⢀⡅⢣⢠⠇⠀⠀
       ⠀⠀⠀⠀⠀⢸⠈⡄⠹⡇⠈⠶⣤⣈⣑⡊⠁⠀⠀⢠⢾⣹⠈⣿⠀⣦⠎⠀⠀⠀
       ⠀⠀⠀⠀⢀⡞⡸⠀⠀⠙⣄⠠⠬⠝⠉⠉⢠⠤⡄⠉⠐⠒⠈⢀⡼⠃⠀⠀⠀⠀
       ⠀⠀⠀⢠⠏⡜⠀⠀⠀⠀⠈⠢⣀⠀⠀⢤⣤⣴⣦⡤⠆⢀⡠⠊⠀⠀⠀⠀⠀⠀
       ⠀⠀⠀⢼⡀⢇⠀⠀⣠⣴⣶⣤⣀⠑⠤⣀⠓⠾⠛⣠⠔⢉⣠⠴⠶⠦⣄⠀⠀⠀
       ⠀⠀⠀⠈⠳⣌⠑⡶⠃⠀⠀⠉⠙⠛⠶⠾⠿⠿⠋⠙⠚⠉⠀⠀⠀⠀⠀⠱⣄⠀
       ⠀⠀⠀⠀⠀⠈⣹⠁⠀⠀⣰⣦⣀⠀⠀⠀⠀⣀⣠⡤⠤⠤⠤⠴⠷⠀⠀⠀⠘⣧
       ⠀⠀⠀⠀⠀⠀⡇⠀⠈⠉⠉⠉⠉⠙⠛⠛⠿⢿⣶⣶⣦⣤⣀⣀⡀⠀⠀⢀⣠⣿
       ⠀⠀⠀⠀⠀⠀⠙⠿⢶⣦⣤⣤⣤⣤⣴⡶⠾⠛⠋⠁⠉⠉⠛⠛⠛⠛⠛⠛⠛⠁

{reset}""")
# Function to display the menu

poster()
print(f"""{Lblue}--Credits:{reset}""")
print("[<3] Lena Alqahtani")
print("[<3] Nouf Alamoudi")
print("[<3] Noor Madani")
print("[<3] Lama Alasmari")
print("[<3] Shahad Almajdoui")
print("[<3] Jana Almutari")

print(f"{yellow}\n--> Instructor: Reem Alassaf\n\n{reset}")

#
# ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
web_name_pattern=re.compile("^(www\.)?([a-zA-Z0-9]+(-?[a-zA-Z0-9])*\.)+(com)?$")


def menu():
    print(f"""{Lblue} Please enter the choice number  
    {Lmagenta}      
    ╔════════════════════════════╗
    ║   1. Domain Information    ║
    ║   2. SQL Injection Scanner ║
    ║   3. Social Media Recon    ║ 
    ║   4. NMAP                  ║
    ║   5. Exit                  ║
    ╚════════════════════════════╝{reset} """)

# def IP_Address_Scan_Menu():
#     print(Lyellow + ""
# "                --------------------------------------------------\n"
# "                Please enter the type of IP Scan you want to run:\n"
# "                --------------------------------------------------"
#           + reset)
#     print(red + """  SQL Injection Scanner
#                Δ To TCP Scan Well Known Ports Enter (1)
#                Δ To UDP Scan Well Known Ports Enter (2)
#                Δ Back to main menu                  (3)
#
#     """ + reset)


def IP_Address_Scan_Menu():
    print(f"""{Lblue}Please enter the choice number {reset} 
    {Lmagenta}
    ╔═══════════════════════════════╗
    ║   1. TCP Scan                 ║
    ║   2. UDP Scan                 ║
    ║   3. Back to main menu        ║
    ╚═══════════════════════════════╝{reset}""")



def IP_Address_Scan():

    while True:
        IP_Address_Scan_Menu()
        choice=input(Lcyan+"Please Choose one option "+reset)
        if choice=="1":
           TCP_Lookup.valid_ipaddress_TCP()
           
           break
        elif choice =="2":
            UDP_Lookup.valid_ipaddress_UPD()
            
            break
        elif choice=='3':
           main_method()
           break
    
        else:
            print(red+"invalid input, please try again. "+reset)

    
def Domain_Menu():
    print(f"""{Lblue}Please enter the choice number {reset} 
    {Lmagenta}
    ╔═══════════════════════════════╗
    ║   1. WHOIS Lookup             ║
    ║   2. Subdomain Enumeration    ║
    ║   3. Back to main menu        ║
    ╚═══════════════════════════════╝{reset}""")



def Domain_Name():

     while True:
            name= input(f"{Lyellow}Enter the web name you want to scan: {reset}") ############################YELLOW  Lyellow
            if web_name_pattern.search(name):
                print(f"The domain name {name} is valid!")
                Domain_Menu()
                choice=input(Lyellow+"Please Choose one option "+reset)
                if choice=="1":
                      whois_lookup.whois_forDomain(name)
                      break
                elif choice =="2":
                    
                    # max_subdomains = int(input("Enter the maximum number of subdomains: "))
                    
                     max_subdomains = int(input("Enter the maximum number of subdomains to check (Enter 0 for no limit): "))
                     subenum.discovered_results=subenum.SubDomain(name, max_subdomains)
                     subenum.save_results_to_file(subenum.discovered_results)
                     subenum.print_summary(subenum.discovered_results)
                     break
                elif choice == "3":
                      main_method()
            else:
                print(f"{red}The domain name {Lwhite}{name}{red} is invalid, please try again with this format (DomainName.com) {reset}\n")


def Social_media_Menu():
    print(f"""{Lblue}Please enter the choice number {reset} 
    {Lmagenta}
    ╔═════════════════════════════╗
    ║   1. GitHub                 ║
    ║   2. Instagram              ║
    ║   3. Back to main menu      ║
    ╚════════════════════════════ ║{reset}""")
    
    
def Social_media():
          while True:
              
                username= input(f"{Lyellow}Enter the username you want to scan: {reset}")
                Social_media_Menu()
                choice=input(Lcyan+"Please Choose one option "+reset)
                if choice=="1":
                      UserName_Lookup.gitinformation(username)
                      break
                elif choice =="2":
                     instaRecon.insta_user(username)   
                     break
                elif choice == "3":
                      main_method()
                else:
                     print(f"{red}The username {Lwhite}{username}{red} is invalid, please try again  {reset}\n")   

def SQLScanner():
    url=input(f'{Lyellow}Enter the target full URL:{reset}')
    verbose_mode=input(f"{Lyellow}Enable verbose mode? (yes/no):{reset} ").lower() == "yes"
    SQLscanner.scan_sql_injection(url,verbose_mode)
    
 
def main_method():
    while True:
        menu()
        choice=input()
        if choice =="1":    # IP Address Scan
          Domain_Name()
        elif choice=="2":   # Domain Name Look-up
            SQLScanner()   
        elif choice == "3":
            Social_media()
        elif choice == "4": 
            IP_Address_Scan()   
        elif choice =="5":  # Exit
            print(f"{Lblue} Thank you for using DeviCon{reset}")
            quit()
        else:               # Wrong input
            print(f"{Lred}Invalid input! Please try again...{reset}")


main_method()