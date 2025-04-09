from dahua.client import DahuaRpc
from dahua.exceptions import DahuaRequestError

client = DahuaRpc(host="172.20.10.254", port=80)
client.login(username="admin", password="q1w2e3r4")

# print(client.console.list_method())
cmd = ""
while cmd.lower() != "exit":
    cmd = input("$ ")

    try:
        # WIP! need to somehow pass back result (may need to attach)
        # Interestingly running 'exit' as a console command stops the device
        response = client.console.run_cmd(command=cmd)
        print(response)
    except DahuaRequestError:  # TODO: map error codes to real exceptions
        print("Command invalid")

client.logout()
