import ipaddress

# ==========================================
# IP CLASSIFIER AND FIREWALL SIMULATOR
# ==========================================

# Firewall-ის წინასწარ განსაზღვრული წესები
# ფორმატი: (პროტოკოლი, პორტი, მოქმედება)

FIREWALL_RULES = [
    ("TCP", 22, "BLOCK"),
    ("TCP", 80, "ALLOW"),
    ("TCP", 443, "ALLOW"),
    ("UDP", 53, "ALLOW"),
]

# Private IP მისამართების დიაპაზონები
PRIVATE_NETWORKS = [
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
]


# ==========================================
# 1. IP ADDRESS CLASSIFIER
# ==========================================

def classify_ip(ip_address):
    """ამოწმებს IP მისამართს და განსაზღვრავს მის კლასსა და ტიპს."""

    try:
        ip = ipaddress.IPv4Address(ip_address)

    except ipaddress.AddressValueError:
        return None

    first_octet = int(str(ip).split(".")[0])

    # IP კლასის განსაზღვრა
    if 1 <= first_octet <= 126:
        ip_class = "A"
    elif 128 <= first_octet <= 191:
        ip_class = "B"
    elif 192 <= first_octet <= 223:
        ip_class = "C"
    elif 224 <= first_octet <= 239:
        ip_class = "D"
    elif 240 <= first_octet <= 255:
        ip_class = "E"
    else:
        ip_class = "Special / Reserved"

    # Private და Public ტიპის განსაზღვრა
    if any(ip in network for network in PRIVATE_NETWORKS):
        ip_type = "Private"
    elif ip.is_global:
        ip_type = "Public"
    else:
        ip_type = "Special / Non-global"

    return {
        "ip": str(ip),
        "class": ip_class,
        "type": ip_type,
        "valid": True
    }


# ==========================================
# 2. FIREWALL SIMULATOR
# ==========================================

def check_firewall(ip_address, port, protocol):
    """ამოწმებს შეყვანილ მონაცემებს Firewall-ის წესებთან."""

    # Firewall-ის წესების შემოწმება
    for rule_protocol, rule_port, action in FIREWALL_RULES:

        if protocol == rule_protocol and port == rule_port:
            return action

    # თუ არცერთი წესი არ დაემთხვა, კავშირი იბლოკება
    return "BLOCK"


# ==========================================
# 3. USER INTERFACE
# ==========================================

def run_simulator():

    print("\n========================================")
    print(" IP CLASSIFIER & FIREWALL SIMULATOR")
    print("========================================")

    print("\nFirewall Rules:")
    print("----------------------------------------")

    for protocol, port, action in FIREWALL_RULES:
        print(f"{protocol:<5} | Port {port:<5} | {action}")

    print("Default Policy: BLOCK")
    print("----------------------------------------")

    # მომხმარებლისგან მონაცემების მიღება
    ip_address = input("\nEnter IPv4 Address: ").strip()

    # IP მისამართის კლასიფიკაცია
    result = classify_ip(ip_address)

    if result is None:
        print("\n[ERROR] Invalid IPv4 Address!")
        return

    print("\n========== IP CLASSIFICATION ==========")
    print(f"IP Address : {result['ip']}")
    print(f"IP Class   : {result['class']}")
    print(f"IP Type    : {result['type']}")
    print("Status     : VALID")

    # პორტის შეყვანა და შემოწმება
    try:
        port = int(input("\nEnter Port Number (1-65535): "))

        if not 1 <= port <= 65535:
            print("\n[ERROR] Port must be between 1 and 65535!")
            return

    except ValueError:
        print("\n[ERROR] Port must be a number!")
        return

    # პროტოკოლის შეყვანა
    protocol = input("Enter Protocol (TCP/UDP): ").strip().upper()

    if protocol not in ("TCP", "UDP"):
        print("\n[ERROR] Invalid Protocol! Use TCP or UDP.")
        return

    # Firewall-ის გადაწყვეტილება
    decision = check_firewall(ip_address, port, protocol)

    print("\n========== FIREWALL RESULT ==========")
    print(f"Source IP : {result['ip']}")
    print(f"Port      : {port}")
    print(f"Protocol  : {protocol}")
    print("-------------------------------------")

    if decision == "ALLOW":
        print("[ALLOW] Traffic is PERMITTED.")
    else:
        print("[BLOCK] Traffic is DENIED.")

    print("-------------------------------------")
    print("Simulation completed successfully!")
    print("======================================")


# ==========================================
# 4. PROGRAM START
# ==========================================

if __name__ == "__main__":
    run_simulator()