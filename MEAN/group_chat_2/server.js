var express = require('express');
var app = express();
var path = require('path');

app.use(express.static(path.join(__dirname, "./static")));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.get('/', function(req, res){
  res.render("index");
});

var server= app.listen(8000,function(){console.log('listening on port 8000')});
var io = require('socket.io').listen(server);

var users = [];
var connections = [];
var messages = [];

io.sockets.on('connection', function(socket){
  console.log('sockets on...')
  connections.push(socket);
  console.log('Connected: %s sockets connected', connections.length);

  socket.on('disconnect', function(data){
    users.splice(users.indexOf(socket.username), 1);
    console.log('Disconnected user...:'+socket.username);
    console.log(users);
    updateUsers();
    connections.splice(connections.indexOf(socket), 1);
    console.log('Disconnected: %s sockets connected', connections.length);
  });

  socket.on('send_msg', function(data){
    console.log('sending message...:'+ data);
    messages.push(data);
    console.log(messages);
    io.emit('new_msg', {msg: data, user: socket.username});
  });

  socket.on('new_user', function(data){
    console.log("new user...: " + data);
    socket.username = data;
    users.push(socket.username);
    console.log(users);
    updateUsers();
  });

  function updateUsers(){
    io.emit('get_users', users);
  }
});
