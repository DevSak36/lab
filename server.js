//import http
let http = require('http');
let fs = require('fs');

//create function
function onRequest(request, response){
    response.writeHead(200, {'Content-Type': 'text/html'});
    fs.readFile('./index.html', null, function(error, data){
        if (error){
            response.writeHead(404);
            response.write('File not found!');
        } else {
            response.write(data);
        }
        response.end();
    });
}

//run server and assign port for service
http.createServer(onRequest).listen(8000);