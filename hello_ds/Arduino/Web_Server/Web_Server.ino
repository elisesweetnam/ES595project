#include <WiFi.h>
#include <ESPAsyncWebServer.h>
#include <AsyncTCP.h>
#include <SPIFFS.h>


// Replace with your network credentials
const char* ssid = "VM2251187";
const char* password = "kfFrmcpK7hxd";

int FSRpin=36;

String readFSR() {
  float t = analogRead(FSRpin);
  if (isnan(t)) {    
    Serial.println("Failed to read from FSR406 sensor!");
    return "";
  }
  else {
    Serial.println(t);
    return String(t);
  }
}

// Create AsyncWebServer object on port 80
AsyncWebServer server(80);

/*unsigned long previousMillis = 0; //store last time was updated
const long interval = 1000; // Updates readings every 1 seconds

//web page
const char index_html[] PROGMEM = R"webpage(
<!DOCTYPE HTML><html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://code.highcharts.com/8.0/highcharts.js"></script>
<style>
body {
min-width: 300px;
max-width: 800px;
height: 400px;
margin: 0 auto;
}
h2 {
font-family: Arial;
font-size: 2.5rem;
text-align: center;
}
</style>
</head>
<body>
<h2>ESP32 Movement monitoring</h2>
<div id="movement-chart" class="container"></div>
</body>
<script>
var chartT = new Highcharts.Chart({
chart:{ renderTo : 'movement-chart' },
title: { text: 'Change in FSR data' },
series: [{
showInLegend: false,
data: []
}],
plotOptions: {
line: { animation: false,
dataLabels: { enabled: true }
},
series: { color: '#059e8a' }
},
xAxis: { type: 'datetime',
dateTimeLabelFormats: { second: '%H:%M:%S' }
},
yAxis: {
title: { text: 'Movement (analog units)' }
},
credits: { enabled: false }
});
setInterval(function ( ) {
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
var x = (new Date()).getTime(),
y = parseFloat(this.responseText);
if(chartT.series[0].data.length > 50) {
chartT.series[0].addPoint([x, y], true, true, true);
} else {
chartT.series[0].addPoint([x, y], true, false, true);
}
}
}
xhttp.open("GET", "/movement", true);
xhttp.send();
}, 1000 ) ;

</script>
</html>)webpage";*/

void setup(){
// Serial port for debugging purposes
Serial.begin(115200);


  // Initialize SPIFFS
  if(!SPIFFS.begin()){
    Serial.println("An Error has occurred while mounting SPIFFS");
    return;
  }

  WiFi.begin(ssid, password);
  while(WiFi.status() != WL_CONNECTED){
    delay(1000);
    Serial.println("connecting to WiFi..");
  }
  Serial.println("WiFi connected");
  Serial.println(WiFi.localIP());

// Route for root / web page
server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
request->send(SPIFFS, "/index.html");
});
server.on("/movement", HTTP_GET, [](AsyncWebServerRequest *request){
request->send_P(200, "text/plain", readFSR().c_str());
});


// Start server
server.begin();

}

void loop(){ 
/*unsigned long currentMillis = millis();
if (currentMillis - previousMillis >= interval) {
previousMillis = currentMillis;
 float FSRreading = analogRead(FSRpin);
 Serial.println(FSRreading);
 }
if (isnan(FSRreading)) {
Serial.println("Failed to read from FSR sensor!");
Serial.println(FSRreading);
}
else {
Serial.println(FSRreading);
}
*/
}
