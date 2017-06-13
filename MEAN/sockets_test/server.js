// require express and path
var express = require("express");
var path = require("path");
// create express app
var app = express();
//setting static content path
app.use(express.static(path.join(__dirname, "./static")));
// setting up view engine and ejs
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
//root route to render the index.ejs view
app.get('/', function(req, res){
  res.render("index");
});

//creates server variable of app.listen
var server = app.listen(8000, function(){console.log('Listening on port 8000')});
// passing var server of app.listen into socket.io to listen to our server
var io = require('socket.io').listen(server);

//on connection event runs code inside
io.sockets.on('connection', function (socket){
  console.log("WE ARE USING SOCKETS!");
  console.log(socket.id);

  socket.on("button_clicked", function(data){
    console.log("Someone clicked a button!"+data.reason);
    socket.emit('server_response', {response: "aren't sockets cool!"});
    io.emit('server_response', {response: "for everyone!"});
    socket.broadcast.emit('server_response', {response: "for everyelse!"});
  });

});
