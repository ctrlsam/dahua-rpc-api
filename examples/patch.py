import argparse
from dahua.client import DahuaRpc
from dahua.utils.upgrade import Upgrade


def main(client: DahuaRpc, firmware_path: str):
    upgrader = Upgrade(client)
    upgrader.upgrade(firmware_path=firmware_path)


if __name__ == "__main__":
    argparse = argparse.ArgumentParser(description="Dahua Firmware Upgrade")
    argparse.add_argument(
        "-f",
        "--firmware-file",
        type=str,
        required=True,
        help="Path to the firmware file",
    )
    argparse.add_argument(
        "-u", "--username", type=str, required=True, help="Username for authentication"
    )
    argparse.add_argument(
        "-p", "--password", type=str, required=True, help="Password for authentication"
    )
    argparse.add_argument(
        "-host", "--host", type=str, required=True, help="Host address of the device"
    )
    argparse.add_argument(
        "-port", "--port", type=int, default=80, help="Port number of the device"
    )

    args = argparse.parse_args()

    # Create a DahuaRpc client instance
    client = DahuaRpc(
        host=args.host,
        port=args.port,
    )

    print(f"Connecting to {args.host}:{args.port}...")
    client.login(username=args.username, password=args.password)

    # Perform the firmware upgrade
    main(client, args.firmware_file)

    client.logout()
    print("Done.")
