#include <ETH.h>
#include <WiFi.h>
#include <WiFiAP.h>
#include <WiFiClient.h>
#include <WiFiGeneric.h>
#include <WiFiMulti.h>
#include <WiFiScan.h>
#include <WiFiServer.h>
#include <WiFiSTA.h>
#include <WiFiType.h>
#include <WiFiUdp.h>

#include <AsyncPrinter.h>
#include <async_config.h>
#include <DebugPrintMacros.h>
#include <ESPAsyncTCP.h>
#include <ESPAsyncTCPbuffer.h>
#include <SyncClient.h>
#include <tcp_axtls.h>

#include <AsyncEventSource.h>
#include <AsyncJson.h>
#include <AsyncWebSocket.h>
#include <AsyncWebSynchronization.h>
#include <ESPAsyncWebServer.h>
#include <SPIFFSEditor.h>
#include <StringArray.h>
#include <WebAuthentication.h>
#include <WebHandlerImpl.h>
#include <WebResponseImpl.h>

#include <SPIFFS.h>


int FSRpin = 36;

AsyncWebServer server(80);

const char* ssid ="iPhone";
const char* password = "password";

int readFSR406pressure(){
 const int FSRreading = analogRead(FSRpin);
 Serial.println(FSRreading);
 }

void setup(){
  Serial.begin(115200);
  WiFi.begin(ssid,password);
  while(WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.println("connecting to WiFi.."_;
  }
  Serial.println(WiFi.localIP());

  if(!SPIFFS.begin()){
  Serial.println("An Error has occurred while mounting SPIFFS");
  return;
}

//requests for data 
server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){//
    request->send(SPIFFS, "/testexample.html");//HTML file saved in same file as this sketch
  });
  server.on("/FSRreading", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/plain", readFSR406pressure().c_str());
server.begin();

}
void loop () {}
