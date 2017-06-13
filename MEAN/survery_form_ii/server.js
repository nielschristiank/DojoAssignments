var express = require('express');
var app = express();
var path = require('path');
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(path.join(__dirname, "./static")));
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.get('/', function(req,res){
  res.render("index");
});

var server = app.listen(8000, function(){console.log('listening on port 8000')});

var io = require('socket.io').listen(server);

io.sockets.on('connection', function(socket){
  console.log("sockets on!");
  console.log(socket.id);

  socket.on('form_submit', function(data){
    console.log("data sent again!"+data);
    socket.emit('update', data);
  });
});
