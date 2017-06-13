//CONTROLLERS
var mongoose = require('mongoose');
var Mongoose = mongoose.model("Mongoose");
module.exports = {
  index: function(req, res){
    Mongoose.find({}, function(err, results){
      if(err){
        console.log(err);
      }
      else{
        res.render('index', {mongooses: results});
      }
    })
  },
  create: function(req, res){
    Mongoose.create(req.body, function(err, results){
      if(err){
        console.log(err);
      }
      else{
        res.redirect('/');
      }
    });
  },
}
