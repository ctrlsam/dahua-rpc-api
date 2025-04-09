from dahua.rpc import RPC


class MagicBoxRPC(RPC):
    """MagicBox RPC class."""
    def __init__(self, client: "DahuaRpc") -> None:
        super().__init__(client=client, parent="magicBox")

    def get_software_version(self) -> dict:
        """Get the software version of the MagicBox."""
        return self._send(function="getSoftwareVersion").get('params', {}).get('version')
    
    def get_device_type(self) -> str:
        """Get the device type of the MagicBox."""
        return self._send(function="getDeviceType").get('params', {}).get('type')
    
    def get_serial_number(self) -> str:
        """Get the serial number of the MagicBox."""
        return self._send(function="getSerialNo").get('params', {}).get('sn')
