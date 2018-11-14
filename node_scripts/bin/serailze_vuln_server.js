const express = require('express');
const cookieParser = require('cookie-parser');
const escape = require('escape-html');
const serialize = require('node-serialize');
const app = express();
app.use(cookieParser())

app.get('/', (req, res) => {
  if (req.cookies.profile) {
    const str = new Buffer(req.cookies.profile, 'base64').toString();
    const obj = serialize.unserialize(str);

    if (obj.username) {
      const sum = eval(obj.num + obj.num);
      res.send(`Hey ${obj.username} ${obj.num} ${obj.num} is ${sum}`);
    }
    else res.send("Error: Invalid username type");
  }
  else {
    res.cookie('profile', "eyJ1c2VybmFtZSI6IkR1bW15IiwiY291bnRyeSI6IklkayBQcm9iYWJseSBTb21ld2hlcmUgRHVtYiIsImNpdHkiOiJMYW1ldG93biIsIm51bSI6IjIifQ==", {
      maxAge: 90000,
      httpOnly: true
    });
  }

  res.send("<h1>If the truth is what you seek, for a /prize/, you must compete.</h1>");
  setTimeout(() => res.send('Routes: /prize, /win, /hint? Yeah that\'s a good amount for this lab...'), 1000);
});

app.get('/prize', (req, res) => {
  res.send('Hey! You found the secret route! Go to /win to get the root password');
});

app.get('/win', (req, res) => {
  res.send('LOL you thought!');
});

app.get('/hint', (req, res) => {
  res.send('Remember to always eat your cookies and check their encoding twice!');
});

app.get('/lel', (req, res) => {
  res.send('https://www.youtube.com/results?search_query=reverse+shell');
});

app.get('/dude/holy/shit/come/on/here/is/the/answer', (req, res) => {
  res.send('https://github.com/jparr721/hax/blob/master/node_scripts/bin/serialize_vulnerability.js');
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
