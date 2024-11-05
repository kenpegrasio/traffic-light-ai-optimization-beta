const int red = 0, yellow = 1, green = 2;
const int trafficLight[2][3] = {{2, 3, 4}, {8, 9, 10}};
const int NUMBER_OF_TRAFFIC_LIGHT = 2;

void setup() {
  Serial.begin(115200);
  for (int idx = 0; idx < NUMBER_OF_TRAFFIC_LIGHT; idx++) {
    for (int i = 0; i < 3; i++) {
      pinMode(trafficLight[idx][i], OUTPUT);
    }
  }
}

void loop() {
  if (Serial.available() > 0) {
    String msg = Serial.readString();
    int idx = int(msg[0] - '0');
    if (msg[1] == 'r') {
      digitalWrite(trafficLight[idx][red], HIGH);
      digitalWrite(trafficLight[idx][green], LOW);
    } else if (msg[1] == 'y') {
      for (int i = 0; i < 10; i++) {
        digitalWrite(trafficLight[idx][yellow], HIGH);
        delay(100);
        digitalWrite(trafficLight[idx][yellow], LOW);
        delay(100);
      }
    } else if (msg[1] == 'g') {
      digitalWrite(trafficLight[idx][red], LOW);
      digitalWrite(trafficLight[idx][green], HIGH);
    } else if (msg[1] == 'o') {
      for (int i = 0; i < 3; i++) {
        digitalWrite(trafficLight[idx][i], LOW);
      }
    } else if (msg == "allOff") {
      for (int idx = 0; idx < NUMBER_OF_TRAFFIC_LIGHT; idx++) {
        for (int i = 0; i < 3; i++) {
          digitalWrite(trafficLight[idx][i], LOW);
        }
      }
    }
  }
}
