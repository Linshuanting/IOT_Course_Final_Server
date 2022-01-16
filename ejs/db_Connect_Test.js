const express = require('express');
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


function Get_Json_From_User () {
    var mysql = require('sync-mysql');
    // 連線資料庫的配置
    config = {
        host: '192.168.10.130',  
        port: 3306,
        user: 'winuser',   
        password: 'winuser',
        database: 'userTable'
    }
    var connection = new mysql(config)
    // 與資料庫建立連線

    var query = "select * from USER_DATA"
    var result = connection.query(query)

    return result

}

function Get_Json_From_Data (username) {

    var mysql = require('sync-mysql');
    // 連線資料庫的配置
    config = {
        host: '192.168.10.130',  
        port: 3306,
        user: 'winuser',   
        password: 'winuser',
        database: 'fileDataBase'
    }
    var connection = new mysql(config)
    // 與資料庫建立連線

    
    var query = `select * from ${username}`
    var result = connection.query(query)

    return result

}


function Json_To_Table( object ) {
    var html = '';
    console.log(object)

    if (object && Object.keys(object[0])){
      html += '<table><tr>';
      console.log(Object.keys(object[0]));
      Object.keys(object[0]).forEach(function(key){
        html += '<th>' + key + '</th>';
      })
      html += '</tr>'
    }

    for (var j=0; j<object.length; j++) {
      html += '<tr>';
      Object.values(object[j]).forEach(function(value){
        html += '<td>' + value + '</td>';
      })
      html += '</tr>';
    }
    html += '</table>';
    return html;
}

module.exports = {
    Json_To_Table,
    Get_Json_From_Data,
    Get_Json_From_User
}

/*
var get_user_table = new Vue({
    el: '#User Table',
    data: {
        message: table_use.table(JSON.parse(dataStr))
    }
})
*/



