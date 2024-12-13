
#define red1 2
#define yellow1 3
#define green1 4

#define red2 5
#define yellow2 6
#define green2 7

#define red_pesh 9
#define green_pesh 8

#define slepoy 10
int maindelay = 5000;
void setup() {
  
  
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    maindelay = command.toInt();
  }
  
  digitalWrite(red_pesh,HIGH);
  digitalWrite(green_pesh,LOW);

  digitalWrite(red1,HIGH);
  digitalWrite(yellow1,LOW);
  digitalWrite(green1,LOW);

  digitalWrite(red2,LOW);
  digitalWrite(yellow2,LOW);
  digitalWrite(green2,HIGH);
  delay(maindelay);
  digitalWrite(yellow2,HIGH);
  delay(3000);
  digitalWrite(red2,HIGH);
  digitalWrite(yellow2,LOW);
  digitalWrite(green2,LOW);
  delay(2000);
  digitalWrite(yellow1,HIGH);
  delay(3000);
  digitalWrite(red1,LOW);
  digitalWrite(yellow1,LOW);
  digitalWrite(green1,HIGH);
  delay(maindelay);
  digitalWrite(yellow1,HIGH);
  delay(3000);
  digitalWrite(green1,LOW);
  digitalWrite(yellow1,LOW);
  digitalWrite(red1,HIGH);

  delay(2000);

  digitalWrite(red_pesh,LOW);
  digitalWrite(green_pesh,HIGH);
  tone(slepoy,250);
  delay(maindelay);
  tone(slepoy,500);
  delay(3000);
  noTone(slepoy);
  digitalWrite(green_pesh,LOW);
  digitalWrite(red_pesh,HIGH);

  digitalWrite(yellow2,HIGH);
  delay(3000);
}
 