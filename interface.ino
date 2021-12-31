void setup() {
  // put your setup code here, to run once:
  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(3, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
    while(Serial.available() < 3) {}
    analogWrite(3, Serial.read());
    analogWrite(5, Serial.read());
    analogWrite(6, Serial.read());
}