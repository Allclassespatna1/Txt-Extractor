import os

api_id = 21537501
api_hash = os.environ.get("API_HASH", "7360337401:AAEuseHJwpcAbf9hRqebbVFxlUO9Y6o0NZg")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "6573766001")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "6573766001")
owner_users = [int(num) for num in osowner_users.split(",")]
