import os

api_id = 21111175
api_hash = os.environ.get("API_HASH", "fffea26a10b8c26ba900e1ed3d013d90")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "6573766001")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "6573766001")
owner_users = [int(num) for num in osowner_users.split(",")]
