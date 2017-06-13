var express = require("express");
var app = express();
var path = require("path");
var bodyParser = require("body-parser");

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(path.join(__dirname, "./static")));

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, './views'));

app.get('/', function(req, res){
  res.render("index");
});

app.post('/result', function(req, res){
  console.log(req.body);
  var survey_info = req.body;
  console.log(survey_info);
  res.render('result', {survey_info});
});

app.listen(8000, function(){console.log("listening on port 8000")});
