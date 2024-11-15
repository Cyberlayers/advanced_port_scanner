import subprocess

def run_nmap(target):
    """Run Nmap scan on the target."""
    print(f"Scanning {target}...")
    try:
        # Run the Nmap command
        result = subprocess.check_output(['nmap', '-sV', target], text=True)
        print("Scan Results:\n")
        print(result)
    except FileNotFoundError:
        print("Nmap is not installed. Please install it and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target = input("Enter the target to scan (IP or domain): ")
    run_nmap(target)
