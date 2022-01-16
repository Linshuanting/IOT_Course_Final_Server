function table( object ) {
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
      Object.keys(object[j]).forEach(function(value){
        html += '<td>' + value + '</td>';
      })
      html += '</tr>';
    }
    html += '</table>';
    return html;
}

module.exports = {
  table
}