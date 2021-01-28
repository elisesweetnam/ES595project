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

}
