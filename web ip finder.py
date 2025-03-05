import socket
import pyfiglet

# Display banner with better font
text = pyfiglet.figlet_format("Web IP Finder", font="slant")
print(text)
print("Created by PIREX\n")  # Added creator name

# Get domain input
domain = input("Enter the website name (e.g., google.com): ")

try:
    # Get the IP address of the domain
    ip_address = socket.gethostbyname(domain)
    print(f"The IP address of {domain} is: {ip_address}")
except socket.gaierror:
    print("Invalid domain or network issue. Please try again.")
