from pyrogram import Client, filters

app = Client(""my_account)

# Команда Type
@app.on_message(filters_command("type", prefixes = ".") & filters.me)
def type(_, msg):
  orig_text = msg.text.split(".type ", maxsplit=1)[1]
  text = orig_text
  tbp = "" # to be printed
  typing_symbol = ""
  
  while(tbp ! = orig_text):
    try:
      msg.edit(tbp + typing_symbol)
      sllep(0.05) # 50 ms
      
      tbp = tbp + text[0]
      text = text[1:]
      
      msg.edit(tbp)
      sleep(0.05)
      
    expect FloodWait as e:
      sleep(e.x)
      
app.run()      
