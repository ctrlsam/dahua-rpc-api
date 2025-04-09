from typing import TypedDict
from dahua.rpc import RPC


class LoginParams(TypedDict):
    """Parameters for login."""
    userName: str
    password: str
    clientType: str
    authorityType: str
    passwordType: str


class GlobalRPC(RPC):
    """MagicBox RPC class."""
    def __init__(self, client:"DahuaRpc") -> None:
        super().__init__(client=client, parent="global")

    def login(self, params: LoginParams, **kwargs) -> str:
        """Get the software version of the MagicBox."""
        return self._send(function="login", endpoint='RPC2_Login', params=params, **kwargs)
