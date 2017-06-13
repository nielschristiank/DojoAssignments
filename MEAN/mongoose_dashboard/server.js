var express = require('express');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
var path = require('path');
var app = express();

app.use(bodyParser.urlencoded({extended: true}));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

mongoose.connect('mongodb://localhost/mongoose_dashboard')

var MongooseSchema = new mongoose.Schema({
  name: String,
  personality: String,
});

var Mongoose = mongoose.model('Mongoose', MongooseSchema);

//routes
app.get('/', function(req, res){
  Mongoose.find({}, function(err, results){
    if(err){
      console.log(err);
    }
    else{
      res.render('index', {mongooses: results});
    }
  });
});
app.post('/', function(req, res){
  Mongoose.create(req.body, function(err, results){
    if(err){
      console.log(err);
    }
    else{
      res.redirect('/');
    }
  });
});
app.get('/mongooses/new', function(req,res){
  res.render('new');
});
app.get('/mongooses/:id', function(req, res){
  Mongoose.find({_id: req.params.id}, function(err, result){
    if(err){
      console.log(err);
    }
    else{
      res.render('show_mongoose', { mongoose: result[0]});
    }
  });
});
app.get('/mongooses/edit/:id', function(req, res){
  Mongoose.find({_id: req.params.id}, function(err, result){
    if(err){
      console.log(err);
    }
    else{
      res.render('edit_mongoose', { mongoose: result[0]});
    }
  });
});
app.post('/mongooses/delete/:id', function(req,res){
  Mongoose.remove({_id: req.params.id }, function(err, result){
    if(err){
      console.log(err);
    }
    else{
      res.redirect('/');
    }
  });
});
app.post('/mongooses/:id', function(req, res){
  Mongoose.update({_id:req.params.id}, req.body, function(err, results){
    if(err){
      console.log(err);
    }
    else{
      res.redirect('/');
    }
  })
})


//port listen
app.listen(8000, function(){
  console.log("listening on port 8000");
});
