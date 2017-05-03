/*jshint
esversion: 6
*/
const Discord = require('discord.js');
const fs = require('fs');
const express = require('express');
const bodyParser = require('body-parser');
const json = require('express-json');
var app = express();

// bot logging, useful for debugging if the windows closes
fs.writeFile('log', '', function (err) {});
var logger = {
  log: function (message, header='log') {
    console.log('[' + header.toUpperCase() + '] ' + message);
    fs.appendFile('log', '[' + header.toUpperCase() + '] ' + message + '\n', (err) => {});
  }
};

var client = new Discord.Client();

// Load configuration
var config = require(__dirname + '/config.json');

var newMessages = [];

client.on('ready', () => {
  logger.log('Logged in as ' + client.user.username + ' - ' + client.user.id);
  client.user.setPresence({
    game: {
      name: config.prefix + 'source'
    }
  });
});

client.on('message', message => {
    logger.log(message.guild.name + ' #' + message.channel.name + ' ' + message.author.username + ': ' + message.content, 'msg');
    newMessages.push({content: message.content, author: message.author.id, channel: message.channel.id});
    if (message.content.startsWith(config.prefix + 'bot')) message.channel.send('Open Source collective v.0 (patch #1.0.0)');
    if (message.content.startsWith(config.prefix + 'source')) message.channel.send('Source Code: https://github.com/BeastKing0/Coders-Delight-Bot');
  }
);

client.on('reconnecting', () => {
  logger.log('Reconnecting to Discrd websocket');
});

client.login(config.token);

app.use(bodyParser.json());

app.use(json());

app.post('/send', function (req, res) {
  logger.log('Sending ' + req.body.message, 'api');
  client.channels.get(req.body.channelid).send(req.body.message);
  res.end('Sent');
});

app.get('/check', function (req, res) {
  res.end(JSON.stringify(newMessages));
  newMessages = [];
});

app.listen(3000, function() {
  logger.log('Express started', 'api');
});
