from pyrogram import Client, filters

app = Client(""my_account)

# Команда Type
@app.on_message(filters_command("type", prefixes = ".") & filters.me)
