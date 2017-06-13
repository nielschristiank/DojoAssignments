// get http module
var http = require('http');
// fs module allows us to read and write content for responses
var fs = require('fs');
// creating a server using http module:
var server = http.createServer(function (request, response){
  // see what URL the clients are requesting:
  console.log('client request URL:', request.url);
  //this is how we do routing:
  if(request.url === '/'){
    fs.readFile('index.html', 'utf8', function (errors,contents){
      console.log(errors);
      response.writeHead(200, {'Content-Type': 'text/html'});
      response.write(contents);
      response.end();
    });
  }
  else if (request.url === '/ninjas'){
    fs.readFile('ninjas.html', 'utf8', function (errors, contents){
      console.log(errors);
      response.writeHead(200, {'Content-Type': 'text/html'});
      response.write(contents);
      response.end();
    });
  }
  else if (request.url === '/dojos/new'){
    fs.readFile('dojos.html', 'utf8', function (errors, contents){
      console.log(errors);
      response.writeHead(200, {'Content-Type': 'text/html'});
      response.write(contents);
      response.end();
    });
  }
  else {
      response.writeHead(418);
      response.end('File not found!');
  }
});

server.listen(6789);

console.log('server running');
