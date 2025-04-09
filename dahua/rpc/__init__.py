from typing import Any


class RPC:
    def __init__(self, client: "DahuaRpc", parent: str):
        self.client = client
        self.parent = parent

    def _send(self, function: str, **kwargs) -> dict[str, Any]:
        """Send a request to the camera."""
        return self.client._request(method=f"{self.parent}.{function}", **kwargs)

