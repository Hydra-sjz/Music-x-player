HELP_1 = """
**<u>Admin Commands:</u>**

/pause or /cpause - Pause the playing music.
/resume or /cresume- Resume the paused music.
/skip or /cskip- Skip the current playing music.
/stop or /cstop- Stop the playing music.
/shuffle or /cshuffle- Randomly shuffles the queued playlist.
/seek or /cseek - Forward Seek the music to your duration
/seekback or /cseekback - Backward Seek the music to your duration
/restart - Restart bot for your chat .
/player - Get a interactive player planel
/queue - Show s the shuffled queue.
/speed or /playback - For adjust the audio playback speeds.
/cspeed or /cplayback - For adjust the audio playback speeds in channel.

🧑‍💻<u>**Auth Users:**</u>
Auth Users can use admin commands without admin rights in your chat.
/auth [Username] - Add a user to AUTH LIST of the group.
/unauth [Username] - Remove a user from AUTH LIST of the group.
/authusers - Check AUTH LIST of the group.
"""

HELP_2 = """<u>**Play Commands:**</u>

/play or /vplay or /cplay  - Bot will start playing your given query on voice chat or Stream live links on voice chats.
/playforce or /vplayforce or /cplayforce -  **Force Play** stops the current playing track on voice chat and starts playing the searched track instantly without disturbing/clearing queue.
/channelplay [Chat username or id] or [Disable] - Connect channel to a group and stream music on channel's voice chat from your group.

⏩<u>**Specific Skip:**</u>
/skip or /cskip [Number(example: 3)] 
- Skips music to a the specified queued number. Example: /skip 3 will skip music to third queued music and will ignore 1 and 2 music in queue.

🔂<u>**Loop Play:**</u>
/loop or /cloop [enable/disable] or [Numbers between 1-10] 
- When activated, bot loops the current playing music to 1-10 times on voice chat. Default to 10 times.
"""

HELP_3 = """
🔰**<u>SUDO USERS:</u>**
/addsudo [Username or Reply to a user]
/delsudo [Username or Reply to a user]
/sudolist - Check Sudo Users of Arch Music Bot
🤖**BOT CMDS:**
/reboot - Reboot your Bot. 
/update - Update Bot.
/speedtest - Check server speeds
/maintenance [enable / disable] 
/logger [enable / disable] - Bot logs the searched queries in logger group.
/get_log [Number of Lines] - Get log of your bot from heroku or vps. Works for both.
 [enable|disable] - Enable Auto stream end after 3 mins if no one is listening.
📈**STATS CDS:**
/activevoice - Check active voice chats on bot.
/activevideo - Check active video calls on bot.
/stats - Check Bots Stats
⚠️**BL-CHAT:**
/blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
/whitelistchat [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot
/blacklistedchat - Check all blacklisted chats.
"""

HELP_4 = """
<u>**Extra  Commands:**</u>
/start - Start the Music Bot.
/help  - Get Commands Helper Menu with detailed explanations of commands.
/ping- Ping the Bot and check Ram, Cpu etc stats of Bot.

<u>**Group Settings:**</u>
/settings - Get a complete group's settings with inline buttons
**Play Settings:**
/playmode - Get a complete play settings panel with buttons where you can set your group's play settings. 

<u>Options in playmode:</u>
**Search Mode** [Direct or Inline] - Changes your search mode while you give /play mode. 
**Admin Commands** [Everyone or Admins] - If everyone, anyone present in you group will be able to use admin commands(like /skip, /stop etc)
**Play Type** [Everyone or Admins] - If admins, only admins present in group can play music on voice chat

**Maintenance mode:**
/logs - Get logs of the bots.
/logger [enable/disable] - bot will be start logging the activities happened on bot.
/maintenance [enable/disable] - On or off Maintenance mode.
"""

HELP_5 = """
👥 <b>Group Commands</b>
/pin Pins a message in groups.
/pinned Displays the pinned message in group
/unpin unpins the currently pinned message.
/staff Displays the list of staff members.
/bots Displays the list of bots in group.
/settitle set the title of the group.
/setdiscription Set the discription of the group.
/setphoto Set the group photo.
/removephoto Remove group photo.
/zombies Removes Deleted accounts from group.
/speedtest measure the internet speed.
/ban bans a user. (via handle, or reply)
/sban Silently ban a user. Deletes command, Replied message and doesn't reply. (via handle, or reply)
/tban x(m/h/d) bans a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.
/unban unbans a user. (via handle, or reply)
/kick kicks a user out of the group, (via handle, or reply)
/mute silences a user. Can also be used as a reply, muting the replied to user.
/tmute  x(m/h/d) mutes a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.
/unmute unmutes a user. Can also be used as a reply, muting the replied to user
"""

HELP_6 = """
👤**BLOCKED FUNCTION:**
/block [Username or Reply to a user] Prevents a user from using bot commands.
/unblock [Username or Reply to a user] Remove a user from Bot's Blocked List.
/blockedusers Check blocked Users Lists
👤**GBAN FUNCTION:**
/gban [Username or Reply to user] Gban a user from bot's served chat and stop him from using your bot.
/ungban [Username or Reply to user] Remove a user from Bot's gbanned List and allow him for using bot
/gbannedusers Check Gbanned Users Lists
⚡️**Auth-Chat:**
/authorize [chat_id] Allow a chat for using your bot.
/unauthorize [chat_id] Disallow a chat from using your bot.
/authorized Check all allowed chats of your bot.
🌐**BROADCAST:**
/broadcast [Message or Reply to a Message] Broadcast any message to Bot's Served Chats.
<u>options for broadcast:</u>
`-pin`: This will pin your message 
`-pinloud`: This will pin your message with loud notification
`-user`: This will broadcast your message to the users who have started your bot.
`-assistant`: This will broadcast your message from assistant account of your bot.
`-nobot`: This will force your bot to not broadcast message
**Example:** `/broadcast -user -assistant -pin Hello Testing`
"""

HELP_7 = """
...
"""

HELP_8 = """
...
"""

HELP_9 = """
...
"""

HELP_10 = """
....
"""

HELP_11 = """
...
"""

HELP_12 = """.
..
"""

HELP_13 = """
..
.
"""

HELP_14 = """
gh
"""

HELP_15 = """
..
"""

HELP_16 = """
✽ <b>CʜᴀᴛGPT ⏤͟͟͞͞★</b>

❍ /ask ➠ ǫᴜᴇʀɪᴇs ᴛʜᴇ ᴀɪ ᴍᴏᴅᴇʟ ᴛᴏ ɢᴇᴛ ᴀ ʀᴇsᴘᴏɴsᴇ ᴛᴏ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ.
 """

HELP_17 = """
✽ <b>sᴛɪᴄᴋᴇʀs ⏤͟͟͞͞★</b>
packkang ➠ ᴄʀᴇᴀᴛᴇs ᴀ ᴘᴀᴄᴋ ᴏғ sᴛɪᴄᴋᴇʀs ғʀᴏᴍ ᴀ ᴏᴛʜᴇʀ ᴘᴀᴄᴋ.
❍ /stickerid
❍ / ➠ ɢᴇᴛs ᴛʜᴇ sᴛɪᴄᴋᴇʀ ɪᴅ ᴏғ ᴀ sᴛɪᴄᴋᴇʀ.
"""

HELP_18 = """
✽ <b>ᴛᴀɢ-ᴀʟʟ ⏤͟͟͞͞★</b>

❍ /tagall ➠ ʀᴀɴᴅᴏᴍ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
❍ /entag ➠ ᴇɴɢʟɪsʜ ᴛᴀɢ.
❍ /hitag ➠ ʜɪɴᴅɪ ᴛᴀɢ.
❍ /shyari ➠ sʜʏᴀʀɪ ᴛᴀɢ.
❍ /bntag ➠ ʙᴀɴɢʟᴀ ᴛᴀɢ.
❍ /vctag ➠ ᴠᴄ ɪɴᴠɪᴛᴇ ᴛᴀɢ.
❍ /utag ➠ ᴛᴀɢ ᴡɪᴛʜ ᴏᴡɴ ᴡʀɪᴛᴇ ᴍᴇssᴀɢᴇ.
 """

HELP_19 = """
✽ <b>ᴜ-ɪɴꜰᴏ ⏤͟͟͞͞★</b>

❍ /id ➠ ɢᴇᴛ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ɢʀᴏᴜᴘ ɪᴅ. ɪғ ᴜsᴇᴅ ʙʏ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ, ɢᴇᴛs ᴛʜᴀᴛ ᴜsᴇʀ's ɪᴅ.
❍ /info ➠ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜsᴇʀ.
❍ /github <ᴜsᴇʀɴᴀᴍᴇ> ➠ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ɢɪᴛʜᴜʙ ᴜsᴇʀ.
"""
HELP_20 = """
.. .
"""
HELP_21 = """
✽ <b>ᴇxᴛʀᴀ ⏤͟͟͞͞★</b>

❍ /math ➠ sᴏʟᴠᴇs ᴍᴀᴛʜᴇᴍᴀᴛɪᴄᴀʟ ᴘʀᴏʙʟᴇᴍs ᴀɴᴅ ᴇǫᴜᴀᴛɪᴏɴs.
❍ /blackpink ➠ ɢᴇɴᴇʀᴀᴛᴇs ᴀ ʙʟᴀᴄᴋᴘɪɴᴋ-sᴛʏʟᴇ ʟᴏɢᴏ.
❍ /carbon ➠ ɢᴇɴᴇʀᴀᴛᴇs ᴀ ᴄᴀʀʙᴏɴ ᴄᴏᴅᴇ ɪᴍᴀɢᴇ ғʀᴏᴍ ᴀ ᴄᴏᴅᴇ sɴɪᴘᴘᴇᴛ.
❍ /speedtest ➠ ᴍᴇᴀsᴜʀᴇs ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ sᴘᴇᴇᴅ.
❍ /reverse ➠ ʀᴇᴠᴇʀsᴇs ᴀ ɢɪᴠᴇɴ ᴛᴇxᴛ.
❍ /webss ➠ ᴛᴀᴋᴇs ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴏғ ᴀ ᴡᴇʙsɪᴛᴇ.
❍ /paste ➠ ᴜᴘʟᴏᴀᴅs ᴀ ᴛᴇxᴛ sɴɪᴘᴘᴇᴛ ᴛᴏ ᴛʜᴇ ᴄʟᴏᴜᴅ ᴀɴᴅ ɢɪᴠᴇs ᴀ ʟɪɴᴋ.
❍ /tgm ➠ ᴜᴘʟᴏᴀᴅs ᴀ ᴘʜᴏᴛᴏ (ᴜɴᴅᴇʀ 𝟻ᴍʙ) ᴛᴏ ᴛʜᴇ ᴄʟᴏᴜᴅ ᴀɴᴅ ɢɪᴠᴇs ᴀ ʟɪɴᴋ.
❍ /tr ➠ ᴛʀᴀɴsʟᴀᴛᴇs ᴛᴇxᴛ.
❍ /google ➠ sᴇᴀʀᴄʜᴇs ғᴏʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴏɴ ɢᴏᴏɢʟᴇ.
❍ /stack ➠ sᴇᴀʀᴄʜᴇs ғᴏʀ ᴘʀᴏɢʀᴀᴍᴍɪɴɢ-ʀᴇʟᴀᴛᴇᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴏɴ sᴛᴀᴄᴋ ᴏᴠᴇʀғʟᴏᴡ.
"""
HELP_22 = """
<b>ɪᴍᴀɢᴇ ⏤͟͟͞͞★</b>

❍ /draw ➠ ɢᴇɴᴇʀᴀᴛᴇs ᴀ ᴅʀᴀᴡɪɴɢ ʙᴀsᴇᴅ ᴏɴ ᴀ ɢɪᴠᴇɴ ᴘᴏʀᴏᴍᴘᴛ.
❍ /image ➠ sᴇᴀʀᴄʜᴇs ғᴏʀ ᴀɴ ɪᴍᴀɢᴇ ʙᴀsᴇᴅ ᴏɴ ᴀ ɢɪᴠᴇɴ ᴋᴇʏᴡᴏʀᴅ.
❍ /upscale ➠ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ ᴛᴏ ᴜᴘsᴄᴀʟᴇ ɪᴛ ᴀɴᴅ ɪᴍᴘʀᴏᴠᴇ ɪᴛs ǫᴜᴀʟɪᴛʏ.
"""
HELP_23 = """
 ✽ <b>ᴀᴄᴛɪᴏɴ ⏤͟͟͞͞★</b>

 .

 ❍ sᴘᴇᴄɪᴀʟ ᴄᴏᴍᴍᴀɴᴅs ➠ Nykaa 𝚋𝚊𝚗 , Nykaa 𝚖𝚞𝚝𝚎 , Nykaa 𝚙𝚛𝚘𝚖𝚘𝚝𝚎 ..... 𝚎𝚝𝚌.
 """
HELP_24 = """
 ✽ <b>sᴇᴀʀᴄʜ ⏤͟͟͞͞★</b>

 ❍ /google <query> ➠ Search the google for the given query.
 ❍ /anime <query>  ➠ Search myanimelist for the given query.
 ❍ /stack <query>  ➠ Search stackoverflow for the given query.
 ❍ /image (/imgs) <query> ➠ Get the images regarding to your query
"""

