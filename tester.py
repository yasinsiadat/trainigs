import requests

def verify_endpoints(ip_addresses):
    try:
        # Send a request to the first IP to get the reference response
        reference_response = requests.get(f"http://{ip_addresses[0]}/").text
        print(f"Reference response from {ip_addresses[0]}: {reference_response}")

        # Iterate through the rest of the IPs and compare responses
        for ip in ip_addresses[1:]:
            try:
                response = requests.get(f"http://{ip}/").text
                print(f"Response from {ip}: {response}")

                # Compare responses
                if response == reference_response:
                    print(f"IP {ip} is verified.")
                else:
                    print(f"IP {ip} does not match the reference response.")
            except requests.exceptions.RequestException as e:
                print(f"Error connecting to IP {ip}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to IP {ip_addresses[0]}: {e}")

# Example usage with a list of IP addresses
ip_list = ["127.0.0.1:8002", "127.0.0.1:8001", "127.0.0.1:8003"]
verify_endpoints(ip_list)
