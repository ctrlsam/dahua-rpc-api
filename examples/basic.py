from dahua.client import DahuaRpc

client = DahuaRpc(host="172.20.10.254", port=80)
client.login(username="admin", password="password")

print("Serial Number: " + client.magic_box.get_serial_number())
