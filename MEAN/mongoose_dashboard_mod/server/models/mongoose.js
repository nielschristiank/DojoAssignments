var mongoose = require('mongoose');

var MongooseSchema = new mongoose.Schema({
  name: String,
  personality: String,
});
mongoose.model('Mongoose', MongooseSchema);
var Mongoose = mongoose.model('Mongoose');
