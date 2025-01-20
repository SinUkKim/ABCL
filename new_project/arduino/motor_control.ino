int dirpin = 2;
int steppin = 3;
unsigned long prevTime = 0;
bool Cstate = false;


void setup() {
  Serial.begin(9600);  // 시리얼 통신 초기화
  pinMode(steppin, OUTPUT); 
  pinMode(dirpin, OUTPUT);
}

void loop() {
  digitalWrite(dirpin, LOW); 
  // 시리얼 데이터가 들어왔는지 확인
  if (Serial.available() > 0) { 
    char command = Serial.read();
    // 시리얼 읽고
    Serial.println(command);
    // 모니터에 보여주는 디버깅
    if (command == '1') {  
      for (int i=0;i<50;i++){ 
        // 1이면 1/4 바퀴 돌기
        for(;;){
          // delay를 빼기위한 시간측정 for문
          unsigned long currentTime = millis(); 
          if (currentTime - prevTime >= 5 && Cstate == false) {
            prevTime = currentTime;  
            digitalWrite(steppin, HIGH);
            Cstate = true;       
          } 
          /*스텝핀에 HIGH가 들어가면 Cstate가 '참' LOW면 '거짓'을 if, elif는 5ms가 지나고 
          참,거짓에 따라 HIGH,LOW를 교반생성 50번 하면 for문 끝, 따라서 1/4바퀴 */
          else if (currentTime - prevTime >= 5 && Cstate == true) {
            prevTime = currentTime; 
            digitalWrite(steppin, LOW);
            Cstate = false;
            break;
          }
        }
      }
    }
  }
}
