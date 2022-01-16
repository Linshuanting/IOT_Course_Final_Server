const express = require('express');
var table_use = require('./json_to_table');
var app = express();
var fs = require('fs');

function render(filename, params) {
    fs.readFile(filename, 'utf8', function (err, data) {
      if (err) return console.log(err);
      console.log(data);
      for (var key in params) {
        data = data.replace('{' + key + '}', params[key]);
      }
      callback(null, data);
    });
}

dataStr = null

function LoginDB () {
    var mysql = require('mysql');
    // 連線資料庫的配置
    var connection = mysql.createConnection({
        // 主機名稱，一般是本機
        host: '192.168.10.130',
        // 資料庫的埠號，如果不設定，預設是3306
        port: 3306,
        // 建立資料庫時設定使用者名稱
        user: 'winuser',
        // 建立資料庫時設定的密碼
        password: 'winuser',
        // 建立的資料庫
        database: 'userTable'
    });
    // 與資料庫建立連線
    connection.connect((err)=>{
        if (err){
            console.log('error connecting: ' + err.stack);
            return;
        }
        connection.query(
            'select * from USER_DATA ', (error, result, fields)=>{
                if (error) console(error);
                data = JSON.stringify(result);
                // 關閉連線
                connection.end();
            }
        )
    });
}

/*
var get_user_table = new Vue({
    el: '#User Table',
    data: {
        message: table_use.table(JSON.parse(dataStr))
    }
})
*/

app.use(express.static("public"));

app.get('/', function(req, res){
    // res.send(table_use.table(JSON.parse(data)));

    res.sendFile(__dirname + '/public/index.html', function(err) {
        if (err) res.send(404);
    });

});

module.exports = {
    LoginDB
}


