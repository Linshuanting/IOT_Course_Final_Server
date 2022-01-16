const http = require('http');
var express = require('express');
var bodyParser = require('body-parser');
var app = express();
var db = require('./db_Connect_Test.js');
const { redirect } = require('statuses');
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: false}))


app.set('views', __dirname + '\\views');
app.use(express.static(__dirname + '\\views'));



app.get('/', function(req, res){

    var mesStr = db.Get_Json_From_User()
    var mes = db.Json_To_Table(mesStr)

    console.log(typeof mes)

    res.render('index.ejs', {
          title: 'My Site',
          message: `${mes}`
    });
});

var name = null;

app.post('/', function(req, res){

    console.log(req.body.search);
    
    name = req.body.search;

    res.redirect('/user')
})

app.get('/user', function(req, res){

    var mesStr = db.Get_Json_From_Data(name);
    var mes = db.Json_To_Table(mesStr)

    res.render('index.ejs', {
        title: `${name} Site`,
        message: `${mes}`
  });

})

app.listen(3000, function() {
    console.log('http://localhost:3000')
});


