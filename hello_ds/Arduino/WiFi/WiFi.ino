#include <WiFi.h>

const char* ssid ="VM2251187";
const char* password = "kfFrmcpK7hxd";

void setup(){
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while(WiFi.status() != WL_CONNECTED){
    delay(1000);
    Serial.println("connecting to WiFi..");
  }
  Serial.println("WiFi connected");
  Serial.println(WiFi.localIP());
}
void loop () {
  }
