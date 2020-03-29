# ChuBot version 1.0

To invite ChuBot to your own server click on the following link:

https://discordapp.com/api/oauth2/authorize?client_id=692667384044978250&permissions=8&scope=bot

<img src="https://github.com/MarcJimenez99/ChuBot/blob/master/chubot.jpg" width="200"/> 

**Note: ChuBot is currently not hosted on an external server. To run the bot, it will have to be running on my own machine. In the future the functionality will be added. Please contact me to test.** 

## Events

### Users leaving and joining the server

**Inscope:** 

ChuBot can send a message to a specifically set server when a user joins and leaves a server

ChuBot will print the following when a user joins a server

<img src = "https://github.com/MarcJimenez99/ChuBot/blob/master/chubotPics/join.JPG">

Chubot will print the following when a user leaves a server

<img src = "https://github.com/MarcJimenez99/ChuBot/blob/master/chubotPics/leave.JPG">

**Out of scope:**

In the future users can customize which channels ChuBot will send announcements such as joining and leaving a server.

## Commands

***!help:*** ChuBot sends an embedded messaege that helps redirect a user depending if they need a regular user command or a whitelisted command.

<img src = "https://github.com/MarcJimenez99/ChuBot/blob/master/chubotPics/help.ex.JPG">

The following pictures shows the results of entering `!help_commands` and `!help_mod_commands`

<img src = "https://github.com/MarcJimenez99/ChuBot/blob/master/chubotPics/help_commands.JPG">

<img src = "https://github.com/MarcJimenez99/ChuBot/blob/master/chubotPics/help_mod_commands.JPG">

### User Commands

***!ping*** Returns the latency of the bot. If the bot is slow to respond this is due to high latency. Using this command helps the users confirm if this is the problem.

<img src = "https://github.com/MarcJimenez99/ChuBot/blob/master/chubotPics/ping.JPG">

***!hello*** ChuBot sends a personalized messasge for the user to their server. Makes use of the random module to take from a random pool of greetings. 

<img src = "https://github.com/MarcJimenez99/ChuBot/blob/master/chubotPics/hello.JPG">

***!users*** ChuBot returns the number of users in the server.

<img src = "https://github.com/MarcJimenez99/ChuBot/blob/master/chubotPics/users.JPG">

***!8ball (question)*** Takes in a given question from the user. Afterwards ChuBot will use the random module to take from a random pool of 8ball responses to answer the user's question.

<img src = "https://github.com/MarcJimenez99/ChuBot/blob/master/chubotPics/8ball.JPG">

### Whitelisted Commands

***!add_to_whitelist (name#ID)*** Takes in a user's discord ID. If the user is whitelisted then ChuBot will enter the given name into it's whitelist. This grants the user access to all whitelisted comamnds. 

![Alt Text](https://github.com/MarcJimenez99/ChuBot/blob/master/chubotPics/add_to_whitelist_ex.gif)

***!remove_from_whitelist (name#ID)*** Takes in a user's discord ID. If the user is whitelisted then ChuBot will remove the given name from it's whitelist. This restricts the user's access to all whitelisted commands.

<img src = "">

***!clear (number)*** ChuBot takes in a number and deletes the `!clear` command and messages before it. 

<img src = "">



