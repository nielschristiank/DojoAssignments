//ROUTES
var mongoose = require('mongoose');
var Mongoose = mongoose.model('Mongoose');
var Mongooses = require('./../controllers/mongooses');
module.exports = function(app){
  app.get('/', Mongooses.index);

  app.post('/', Mongooses.create);

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
    });
  });
};
