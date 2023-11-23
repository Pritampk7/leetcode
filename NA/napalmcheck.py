import napalm
import json


def get_device_facts(driver_name, hostname, username, password):
    # Load the correct NAPALM driver for the device
    driver = napalm.get_network_driver(driver_name)

    # Connect to the device
    with driver(hostname, username, password) as device:
        # Get device facts
        facts = device.get_facts()

        return facts


# Example usage
if __name__ == "__main__":
    # Define your device parameters
    driver_name = 'ios'  # Example for Cisco IOS, change as needed
    hostname = 'sbx-nxos-mgmt.cisco.com'  # Replace with your device's IP address
    username = 'admin'
    password = 'Admin_1234!'

    # Get device facts
    device_facts = get_device_facts(driver_name, hostname, username, password)

    # Print the facts
    print(json.dumps(device_facts, indent=4))
