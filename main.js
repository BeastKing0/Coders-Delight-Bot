/*jshint
esversion: 6
*/
const Discord = require('discord.js');
const fs = require('fs');

// bot logging, useful for debugging if the windows closes
fs.writeFile('log', '', function (err) {});
var logger = {
  log: function (message, header='log') {
    console.log('[' + header.toUpperCase() + '] ' + message);
    fs.appendFile('log', '[' + header.toUpperCase() + '] ' + message + '\n', (err) => {});
  }
}

var client = new Discord.Client();

// Load configuration
var config = require(__dirname + '/config.json');

client.on('ready', () => {
  logger.log('Logged in as');
  logger.log(client.user.username);
  logger.log(client.user.id);
  logger.log('------');
  client.user.setPresence({
    game: {
      name: config.prefix + 'source'
    }
  });
});

client.on('message', message => {
    if (message.content.startsWith(config.prefix + 'bot')) message.channel.send('Open Source collective v.0 (patch #1.0.0)');
    if (message.content.startsWith(config.prefix + 'source')) message.channel.send('Source Code: https://github.com/BeastKing0/Coders-Delight-Bot');
  }
);

client.login(config.token);
