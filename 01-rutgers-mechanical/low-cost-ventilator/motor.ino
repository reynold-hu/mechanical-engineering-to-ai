// defines pins numbers
const int dirPin  = 3;
const int stepPin = 4; 
const int enPin   = 5;

void setup() {
  
  // Sets the two pins as Outputs
  pinMode(stepPin,OUTPUT); 
  pinMode(dirPin,OUTPUT);
  
  pinMode(enPin,OUTPUT);
  digitalWrite(enPin,LOW);

}
void loop() {
  
  digitalWrite(dirPin,HIGH); // Enables the motor to move in counter-clockwise direction

  // 800 pulses for one full cycle rotation

  const float pi = 3.14159;
  int vTidal=800; //mL (input from rotery encoder)
  const float radius=6.35; //Bellow radius (cm)
  const float lean=0.8; //linear travel per revolution (cm/rev)
  const float h=vTidal/pi/pow(radius,2); //total linear displacement (cm)
  int rev=h/lean*800; //number of pulse sent to motor for required revolution 

  int BPM=10; //input
  int IE=3; //input, IE ratio of 1:3
  int T_h=0.15; //hold time, constant (s)
  const float T=60/BPM; //inspiratory period (s/breath)
  const float T_in=T/(1+IE)-T_h; //inhale time (s)
  int delay_in=T_in/(0.000001*2*rev); //(microsecond 10^-6s)
  
  for(int x = 0; x < rev; x++) {

    digitalWrite(stepPin,HIGH); 

    delayMicroseconds(delay_in); 

    digitalWrite(stepPin,LOW); 

    delayMicroseconds(delay_in); 

  }

  delay(T_h*10); // hold time (ms)


  digitalWrite(dirPin,LOW); //Enables the motor to move in clockwise direction

  // 800 pulses for one full cycle rotation

  for(int x = 0; x < rev; x++) {

    digitalWrite(stepPin,HIGH);

    delayMicroseconds(delay_in);

    digitalWrite(stepPin,LOW);

    delayMicroseconds(delay_in);

  }
  
const float T_ex=T-T_in-T_h;
  delay((T_ex-T_in-T_h-T_in)*1000); //(ms,enter 1000=1s)


}
