class LectureRoom:
    def __init__(self, name, vlan_id):
        self.name = name
        self.vlan_id = vlan_id
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

class Device:
    def __init__(self, name, ip_address, mac_address):
        self.name = name
        self.ip_address = ip_address
        self.mac_address = mac_address

def generate_ip_addresses(base_ip, vlan_id, num_devices):
    ip_addresses = []
    for i in range(num_devices):
        ip_addresses.append(f"{base_ip}.{vlan_id}.{i+1}")
    return ip_addresses

def configure_vlans(lecture_rooms):
    vlan_configs = {}
    for room in lecture_rooms:
        vlan_configs[room.vlan_id] = room.name
    return vlan_configs

def main():
    lecture_rooms = [
        LectureRoom("Lecture Room A", 110),
        LectureRoom("Lecture Room B", 220),
        LectureRoom("Lecture Room C", 330),
        LectureRoom("Lecture Room D", 440),
        LectureRoom("Lecture Room E", 550)
    ]

    # Generate and assign IP addresses to devices in each lecture room
    base_ip = "12.0"
    for room in lecture_rooms:
        ip_addresses = generate_ip_addresses(base_ip, room.vlan_id, 2)  # Assuming 2 PCs per room
        for i, device_name in enumerate(["PC1", "PC2"]):
            device_ip = ip_addresses[i]
            device_mac = "00:00:00:00:00:0" + str(i+1)  # Example MAC address
            device = Device(device_name, device_ip, device_mac)
            room.add_device(device)

    # Configure VLANs
    vlan_configs = configure_vlans(lecture_rooms)

    # Print IP addresses and VLAN configurations
    for room in lecture_rooms:
        print(f"{room.name}:")
        for device in room.devices:
            print(f"- {device.name}: IP={device.ip_address}, MAC={device.mac_address}")
        print(f"VLAN ID: {room.vlan_id}")
        print()

    print("VLAN Configurations:")
    for vlan_id, room_name in vlan_configs.items():
        print(f"VLAN ID {vlan_id}: {room_name}")

if __name__ == "__main__":
    main()
