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
      maxAge: 900000,
      httpOnly: true
    });
  }

  res.send("<h1>404</h1>");
});
app.listen(3000);
