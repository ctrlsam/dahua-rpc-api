from typing import Any
from dahua.rpc import RPC


class UserManagerRPC(RPC):
    def __init__(self, client: "DahuaRpc"):
        super().__init__(client=client, parent="userManager")

    def get_user_info_all(self) -> dict[str, Any]:
        return self._send(function="getUserInfoAll").get("params", {}).get("users", {})

    def get_active_user_info_all(self) -> dict[str, Any]:
        return (
            self._send(function="getActiveUserInfoAll")
            .get("params", {})
            .get("users", {})
        )

    def delete_user(self, name: str) -> None:
        return self._send(function="deleteUser", params={"name": name})
