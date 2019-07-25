int throttlePin = 3;
int throttleVal = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //init at 9600 bits per second
}

void loop() {
  throttleVal = analogRead(throttlePin);
  Serial.println(throttleVal); // write a string
  delay(50);
}
