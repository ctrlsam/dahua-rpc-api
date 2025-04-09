from dahua.client import DahuaRpc

users_to_delete = [
    "admln"
]

dahua = DahuaRpc("172.20.10.254", 80)
dahua.login("admin", "q1w2e3r4")

for user in users_to_delete:
    try:
        dahua.user_manager.delete_user(user)
        print(f"Deleted user: {user}")
    except Exception as e:
        print(f"Failed to delete user {user}: {e}")
