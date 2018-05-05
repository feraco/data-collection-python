$(document).ready (function($) {
  console.log("JS FIRED")
  xively.setKey( "IPMdQlqEtGmcy5WxkrzD4KL6jTNqq1mSeVNkebgdOMntYsh3" );
  console.log("Key found. Setting JQuery")

  var feedID = 1579988059,
      wu_hum = "#hum";
      wu_temp = "#temp";
      wu_weath = "#weather";
      wu_uv = "#uv"
      bmetemp = "#bmetemp"
      bmepres = "#bmepres"
      bmehum = "#bmehum"
      mag_field = "#mag_field"
      

  xively.feed.get (feedID, function ( datastream ) {
   $(wu_hum).html(datastream["datastreams"]["0"]["current_value"]);
   $(wu_temp).html(datastream["datastreams"]["1"]["current_value"]);
   $(bmetemp).html(datastream["datastreams"]["2"]["current_value"]);
   $(bmepres).html(datastream["datastreams"]["3"]["current_value"]);
   $(bmehum).html(datastream["datastreams"]["4"]["current_value"]);
   $(mag_field).html(datastream["datastreams"]["5"]["current_value"]);
  
   $(wu_uv).html(datastream["datastreams"]["16"]["current_value"]);
   $(wu_weath).html(datastream["datastreams"]["17"]["current_value"]);
   
   xively.feed.subscribe( feedID, function ( event , datastream_updated ) {  
                         $(wu_hum).html(datastream["datastreams"]["0"]["current_value"]);
                         $(wu_temp).html(datastream["datastreams"]["1"]["current_value"]);
                         $(bmetemp).html(datastream["datastreams"]["2"]["current_value"]);
                         $(bmepres).html(datastream["datastreams"]["3"]["current_value"]);
                         $(bmehum).html(datastream["datastreams"]["4"]["current_value"]);
                         $(mag_field).html(datastream["datastreams"]["5"]["current_value"]);
                         
                         $(wu_uv).html(datastream["datastreams"]["16"]["current_value"]);
                         $(wu_weath).html(datastream["datastreams"]["17"]["current_value"]);
    }); 
  });
});
