import subprocess
import time
import matplotlib.pyplot as plt

def get_current_connection():
    command = "netsh wlan show interfaces"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout

def print_current_connection():
    command = "netsh wlan show interfaces"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(result.stdout)

def get_name(connection_info):
    lines = connection_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Name" in line:
            extract_info['Name'] = line.split(':', 1)[1].strip()
    return extract_info

def get_description(connection_info):
    lines = connection_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Description" in line:
            extract_info['Description'] = line.split(':', 1)[1].strip()
    return extract_info

def get_mac(connection_info):
    lines = connection_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Physical" in line:
            extract_info['MAC'] = line.split(':', 1)[1].strip()
    return extract_info

def get_state(connection_info):
    lines = connection_info.split('\n')
    extract_info = {}
    for line in lines:
        if "State" in line:
            extract_info['State'] = line.split(':', 1)[1].strip()
    return extract_info

def get_ssid(connection_info):
    lines = connection_info.split('\n')
    extract_info = {}
    for line in lines:
        if "SSID" in line:
            if "BSSID" not in line:
                extract_info['SSID'] = line.split(':', 1)[1].strip()
            else:
                break
    return extract_info

def get_bssid(connection_info):
    lines = connection_info.split('\n')
    extract_info = {}
    for line in lines:
        if "BSSID" in line:
            extract_info['BSSID'] = line.split(':', 1)[1].strip()
    return extract_info

def get_net_type(connection_info):
    lines = connection_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Network" in line:
            extract_info['Type'] = line.split(':', 1)[1].strip()
    return extract_info

def get_radio_type(connection_info):
    lines = connection_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Radio" in line:
            extract_info['Radio'] = line.split(':', 1)[1].strip()
    return extract_info

def get_auth(connection_info):
    lines = connection_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Authentication" in line:
            extract_info['Auth'] = line.split(':', 1)[1].strip()
    return extract_info

def get_cipher(connection_info):
    lines = connection_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Cipher" in line:
            extract_info['Cipher'] = line.split(':', 1)[1].strip()
    return extract_info

def get_channel(connection_info):
    lines = connection_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Channel" in line:
            extract_info['Channel'] = line.split(':', 1)[1].strip()
    return extract_info

def get_receive(connection_info):
    lines = connection_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Receive" in line:
            extract_info['Rx'] = line.split(':', 1)[1].strip()
    return extract_info

def get_transmit(connection_info):
    lines = connection_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Transmit" in line:
            extract_info['Tx'] = line.split(':', 1)[1].strip()
    return extract_info

def get_signal(connection_info):
    lines = connection_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Signal" in line:
            extract_info['Signal'] = line.split(':', 1)[1].strip()
    return extract_info

def get_signal_int():
    lines = connection_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Signal" in line:
            return int(line.split(':', 1)[1].strip().replace('%', ''))

def record_signal_over_time(duration, interval):
    end_time = time.time() + duration
    signal_strengths = []
    while time.time() < end_time:
        strength = get_signal_int()
        if strength is not None:
            signal_strengths.append(strength)
            print(f"Signal Strength: {strength}%")
        time.sleep(interval)
    return signal_strengths


def plot_signal_strengths(signal_strengths, interval):
    plt.plot([i*interval for i in range(len(signal_strengths))], signal_strengths)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Signal Strength (%)')
    plt.title('Wi-Fi Signal Strength Over Time')
    plt.show()

def get_profile(connection_info):
    lines = connection_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Profile" in line:
            extract_info['Profile'] = line.split(':', 1)[1].strip()
    return extract_info

def get_available_networks():
    command = "netsh wlan show networks mode=bssid"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout

def print_available_networks():
    command = "netsh wlan show networks mode=bssid"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(result.stdout)

def get_basic(available_info):
    lines = available_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Basic" in line:
            extract_info['Basic Rates (Mbps)'] = line.split(':', 1)[1].strip()
    return extract_info

def get_other(available_info):
    lines = available_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Other" in line:
            extract_info['Other Rates (Mbps)'] = line.split(':', 1)[1].strip()
    return extract_info

def get_wireless_capability():
    command = "netsh wlan show wirelesscapabilities"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout

def print_wireless_capability():
    command = "netsh wlan show wirelesscapabilities"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(result.stdout)

def get_wireless_firmware(capability_info):
    lines = capability_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Firmware" in line:
            extract_info['Firmware'] = line.split(':', 1)[1].strip()
    return extract_info

def get_d0t11k_report(capability_info):
    lines = capability_info.split('\n')
    extract_info = {}
    for line in lines:
        if "DOT11k neighbor report" in line:
            extract_info['Dot11k report'] = line.split(':', 1)[1].strip()
    return extract_info

def get_tx_streams(capability_info):
    lines = capability_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Tx Spatial Streams" in line:
            extract_info['Tx Streams'] = line.split(':', 1)[1].strip()
    return extract_info

def get_tx_streams(capability_info):
    lines = capability_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Rx Spatial Streams" in line:
            extract_info['Rx Streams'] = line.split(':', 1)[1].strip()
    return extract_info

def get_driver():
    command = "netsh wlan show drivers"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout

def print_driver():
    command = "netsh wlan show drivers"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(result.stdout)

def get_eth_config():
    command = "ipconfig"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout

def get_gateway(eth_info):
    lines = eth_info.split('\n')
    extract_info = {}
    for line in lines:
        if "192.168" in line:
            extract_info['Gateway IP'] = line.split(':', 1)[1].strip()
    return extract_info

def ping_gate(gateway):
    command = f"ping -a -n 5 {gateway}"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(result.stdout)

def ping_tds():
    command = f"ping -a -n 5 speedtest.tds.net"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(result.stdout)

def ping_wellknown():
    command = f"ping -a -n 5 1.1.1.1"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(result.stdout)
    
if __name__ == "__main__":
    connection_info = get_current_connection()
    available_info = get_available_networks()
    capability_info = get_wireless_capability()
    eth_info = get_eth_config()
    driver_info = get_driver()
    specific_info = get_gateway(eth_info)
    gateway = get_gateway(eth_info)
    print(gateway)
    ping_gate('192.168.141.1')
    ping_tds()
    ping_wellknown()
    # print(specific_info)
    # print_available_networks()
    # print_current_connection()
    # print(available_info)
    #print(specific_info)
    duration = int(input("Enter duration in seconds: "))
    interval = int(input("Enter interval in seconds: "))
    signal_strengths = record_signal_over_time(duration, interval)
    plot_signal_strengths(signal_strengths, interval)
    
