import subprocess
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import numpy as np
import sys

# Define the global variables for the GUI components
root = None
button_frame = None
plot_frame = None
output_text = None
entry_text = None

class CustomStream:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.insert(tk.END, text)
        self.text_widget.see(tk.END)

    def flush(self):
        pass  # No need to flush in this case

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

def get_signal_int(connection_info):
    lines = connection_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Signal" in line:
            return int(line.split(':', 1)[1].strip().replace('%', ''))

def record_signal_over_time(duration_var, interval_var):
    duration = int(duration_var.get())
    interval = int(interval_var.get())
    end_time = time.time() + duration
    signal_strengths = []
    while time.time() < end_time:
        command = "netsh wlan show interfaces"
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        connection_info = result.stdout
        
        strength = get_signal_int(connection_info)
        if strength is not None:
            signal_strengths.append(strength)
            output_text.insert(tk.END, f"Signal Strength: {strength}%\n")  # Display in the output frame
            output_text.see(tk.END)  # Scroll to the end
            print(f"Signal Strength: {strength}%")
        time.sleep(interval)
    return signal_strengths

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

def get_wifi_report():
    command = "netsh wlan show wlanreport"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(result.stdout)

def get_eth_config():
    command = "ipconfig"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    # print(result.stdout)
    return result.stdout

def get_gateway(eth_info):
    lines = eth_info.split('\n')
    extract_info = {}
    for line in lines:
        if "Default Gateway" in line:
            if "192.168" in line:
                gateway_ip = line.split(':', 1)[1].strip()
                return gateway_ip
    return None

def ping_gate():
    eth_info = get_eth_config()
    gateway = get_gateway(eth_info)
    # print(gateway)
    if gateway:
        print("Gateway IP:", gateway)
        command = f"ping -a -n 5 {gateway}"
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        print(result.stdout)
    else:
        print("No valid Gateway IP found.")

def ping_tds():
    command = f"ping -a -n 5 speedtest.tds.net"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(result.stdout)

def ping_wellknown():
    command = f"ping -a -n 5 1.1.1.1"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(result.stdout)

def trace_wellknown():
    command = f"tracert 1.1.1.1"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(result.stdout)

def plot_signal_strengths(signal_strengths, interval):
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot([i * interval for i in range(len(signal_strengths))], signal_strengths)
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Signal Strength (%)')
    ax.set_title('Wi-Fi Signal Strength Over Time')
    plt.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.get_tk_widget().pack()
    canvas.draw()

def start_recording():
    duration_str = duration_var.get()
    interval_str = interval_var.get()

    if not duration_str.isdigit() or not interval_str.isdigit():
        print("Invalid input. Please enter valid integer values for duration and interval.")
        return

    duration = int(duration_str)
    interval = int(interval_str)

    signal_strengths = record_signal_over_time(duration, interval)
    plot_signal_strengths(signal_strengths, interval)

def create_gui():
    global root, button_frame, plot_frame, output_text, duration_var, interval_var
    
    # Create a Tkinter window
    root = tk.Tk()
    root.title("Wi-Fi Signal Strength and Functions")
    root.geometry("800x600")

    # Create an input text box
    #entry_text = ttk.Entry(root)
    #entry_text.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    # Create a button to start recording
    #start_button = ttk.Button(root, text="Start Recording", command=start_recording)
    #start_button.grid(row=5, column=0, padx=10, pady=10, sticky="w")

    # Create an input text box for duration
    #duration_var = tk.StringVar()
    #ttk.Label(root, text="Enter duration in seconds:").grid(row=1, column=0, padx=10, pady=10, sticky="nw")
    #entry_duration = ttk.Entry(root, textvariable=duration_var)
    #entry_duration.grid(row=2, column=0, padx=10, pady=10, sticky="n")

    # Create an input text box for interval
    #interval_var = tk.StringVar()
    #ttk.Label(root, text="Enter interval in seconds:").grid(row=3, column=0, padx=10, pady=10, sticky="nw")
    #entry_interval = ttk.Entry(root, textvariable=interval_var)
    #entry_interval.grid(row=4, column=0, padx=10, pady=10, sticky="n")

    # Create a Frame for buttons on the left
    button_frame = ttk.Frame(root)
    button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    button_frame1 = ttk.Frame(root)
    button_frame1.grid(row=0, column=1, padx=10, pady=10, sticky="nw")

    # Create a Frame for the plot
    plot_frame = ttk.Frame(root)
    plot_frame.grid(row=1, column=2, padx=10, pady=10, sticky="se")

    # Create an output text box in the lower right
    output_text = ScrolledText(root, wrap=tk.WORD, height=30, width=60)
    output_text.grid(row=0, column=2, padx=10, pady=10, sticky="ne")

    sys.stdout = CustomStream(output_text)

    # Create buttons for additional functions
    capability_button = ttk.Button(button_frame, text="Print Current Connection", command=print_current_connection)
    capability_button.pack(pady=5)

    # Create buttons for additional functions
    capability_button = ttk.Button(button_frame, text="Print Available Networks", command=print_available_networks)
    capability_button.pack(pady=5)

    # Create buttons for additional functions
    current_button = ttk.Button(button_frame, text="Print Wireless Capability", command=print_wireless_capability)
    current_button.pack(pady=5)

    # Create buttons for additional functions
    current_button = ttk.Button(button_frame, text="Ping Well Known", command=ping_wellknown)
    current_button.pack(pady=5)

    # Create buttons for additional functions
    current_button = ttk.Button(button_frame1, text="Ping TDS", command=ping_tds)
    current_button.pack(pady=5)

    # Create buttons for additional functions
    current_button = ttk.Button(button_frame1, text="Ping Gateway", command=ping_gate)
    current_button.pack(pady=5)

    # Create buttons for additional functions
    current_button = ttk.Button(button_frame1, text="Trace Well Known", command=trace_wellknown)
    current_button.pack(pady=5)

    # Create buttons for additional functions
    current_button = ttk.Button(button_frame1, text="Get WiFi Report", command=get_wifi_report)
    current_button.pack(pady=5)

def main():
    create_gui()
    # connection_info = get_current_connection()
    # available_info = get_available_networks()
    # capability_info = get_wireless_capability()
    
    # driver_info = get_driver()
    # specific_info = get_gateway(eth_info)
    
    # print(gateway)
    # ping_gate('192.168.141.1')
    # ping_tds()
    # ping_wellknown()
    # print(specific_info)
    # print_available_networks()
    # print_current_connection()
    # print(available_info)
    #print(specific_info)
    
    # Capture Wi-Fi signal strengths and plot them
    #duration = int(input("Enter duration in seconds: "))
    #interval = int(input("Enter interval in seconds: "))

    root.mainloop()
    
if __name__ == "__main__":
    main()

    
