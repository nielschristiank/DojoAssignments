// http module
var http = require('http');
// fs module
var fs = require('fs');
// creating server
var server = http.createServer(function (request, response){
  //index route
  if (request.url === '/'){
    fs.readFile('./views/index.html', function(errors, contents){
      response.writeHead(200, {'Content-Type': 'text/html'});
      response.write(contents);
      response.end();
    });
  }
  else if(request.url === '/cars'){
    fs.readFile('./views/cars.html', function(errors, contents){
      response.writeHead(200, {'Content-Type': 'text/html'});
      response.write(contents);
      response.end();
    });
  }
  else if(request.url === '/images/car1.jpg'){
    fs.readFile('./images/car1.jpg', function(errors, contents){
      response.writeHead(200, {'Content-Type': 'image/jpg'});
      response.write(contents);
      response.end();
    });
  }
  else if(request.url === '/images/car2.jpg'){
    fs.readFile('./images/car2.jpg', function(errors, contents){
      response.writeHead(200, {'Content-Type': 'image/jpg'});
      response.write(contents);
      response.end();
    });
  }
  else if(request.url === '/cats'){
    fs.readFile('./views/cats.html', function(errors, contents){
      response.writeHead(200, {'Content-Type': 'text/html'});
      response.write(contents);
      response.end();
    });
  }
  else if(request.url === '/images/cat1.jpg'){
    fs.readFile('./images/cat1.jpg', function(errors, contents){
      response.writeHead(200, {'Content-Type': 'image/jpg'});
      response.write(contents);
      response.end();
    });
  }
  else if(request.url === '/images/cat2.jpg'){
    fs.readFile('./images/cat2.jpg', function(errors, contents){
      response.writeHead(200, {'Content-Type': 'image/jpg'});
      response.write(contents);
      response.end();
    });
  }
  else {
      response.writeHead(418);
      response.end("418: I am a teapot!");
    }
});

server.listen(7077);

console.log("server running")
