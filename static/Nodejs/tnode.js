var fs = require('fs');
var http = require('http');
var titulo= 'prueba.txt';
var texto="Hey there!" ;

fs.writeFile(titulo,texto, function(err) {
    if(err) {
        return console.log(err);
    }


}); 

http.createServer(function (req, res) {
    res.writeHead(200,{titulo});
    res.write(texto)
    res.end();
}).listen(1080);
