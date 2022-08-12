//define Ultrasonic sensor
#include <NewPing.h>
#define TRIGGER_PIN 4 
#define ECHO_PIN 5 
#define MAX_DISTANCE 100
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); //Sensor Assign

int i=0, pos = 0,current_distance=0;
void setup() 
{
    Serial.begin(9600);
}

void loop()
{
  current_distance = sonar.ping_cm();
  if(current_distance > 10 && current_distance < 25)
   {
     Serial.println("switch");
     delay(500);
   }
}
