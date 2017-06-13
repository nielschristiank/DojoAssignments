var express = require('express');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
var path = require('path');
var app = express();

app.use(bodyParser.urlencoded({extended: true}));
app.set('views', path.join(__dirname, 'client', 'views'));
app.set('view engine', 'ejs');
app.use(express.static(path.join(__dirname, 'client', 'static')));

//mongoose
require('./server/config/mongoose.js');

//routes
require('./server/config/routes')(app);

//port listen
app.listen(8000, function(){
  console.log("listening on port 8000");
});
