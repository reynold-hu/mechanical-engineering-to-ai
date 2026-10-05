
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,20,4);  // set the LCD address to 0x27 for a 16 chars and 2 line display

#define dirPin  3                                 //declarations for stepper motor driver
#define pulPin 4 
#define enPin   5

#define manPin 22                                 //declarations for mandatory/assistive toggle
#define assPin 23

#define pi 3.1415926535897932384626433832795      //variables
#define radius 6.35                               //Bellow radius (cm)
#define pitch 0.8                                 //linear travel per revolution (cm/rev)

#define inputVolCLK 43                             //Tidal volume pinouts
#define inputVolDT 44
#define inputVolSW 45

#define inputIECLK 39                             //IE Ratio pinouts
#define inputIEDT 40
#define inputIESW 41

#define inputBPMCLK 47                             //BPM Pinouts
#define inputBPMDT 48
#define inputBPMSW 49


int TidalVol;                                       //Tidal volume variables
int counterVol = 0; 
int currentVolStateCLK;
int previousVolStateCLK; 
int VolStateSW; 

int IE;                                           //IE Ration variables
int counterIE = 0; 
int currentIEStateCLK;
int previousIEStateCLK; 
int IEStateSW; 

int BPM;                                          //BPM variables
int counterBPM = 0; 
int currentBPMStateCLK;
int previousBPMStateCLK; 
int BPMStateSW; 

int BPM;                                          //BPM variables
int counterBPM = 0; 
int currentBPMStateCLK;
int previousBPMStateCLK; 
int BPMStateSW; 

void setup()
{
  Serial.begin (9600);
  Wire.begin();
  lcd.init();                      
  lcd.backlight();
  
  pinMode(pulPin,OUTPUT);                         // stepper motor driver PIN types
  pinMode(dirPin,OUTPUT);  
  pinMode(enPin,OUTPUT);
  digitalWrite(enPin,LOW);
    
  pinMode(manPin, INPUT);                        // toggle switch PIN type
  pinMode(assPin, INPUT);

  pinMode (inputVolCLK,INPUT);                  //Tidal volume
  pinMode (inputVolDT,INPUT);
  pinMode (inputVolSW,INPUT);
  previousVolStateCLK = digitalRead(inputVolCLK); 

  pinMode (inputIECLK,INPUT);                  //IE Ratio
  pinMode (inputIEDT,INPUT);
  pinMode (inputIESW,INPUT);
  previousIEStateCLK = digitalRead(inputIECLK); 

  pinMode (inputBPMCLK,INPUT);                  //BPM
  pinMode (inputBPMDT,INPUT);
  pinMode (inputBPMSW,INPUT);
  previousBPMStateCLK = digitalRead(inputBPMCLK); 
  

}


void loop(){

updateModeType();
updateTidalVolume();
updateIERatio();
updateBPM();

}


void updateModeType(){
if (digitalRead(manPin)==HIGH)
  {
  lcd.setCursor(0,0);
  lcd.print("Mandatory");
  }

  else
  {
  lcd.setCursor(0,0);
  lcd.print("Assistive");
  }
}

void updateTidalVolume(){
if (digitalRead(inputVolSW) == 0){               
   currentVolStateCLK = digitalRead(inputVolCLK);                                // Read the current state of inputCLK
   if (currentVolStateCLK != previousVolStateCLK){                               // If the previous and the current state of the inputCLK are different then a pulse has occured
       
     if (digitalRead(inputVolDT) != currentVolStateCLK) {                        // If the inputDT state is different than the inputCLK state then
       counterVol ++;                                                               // the encoder is rotating clockwise
       
     } else {                                                                     // Encoder is rotating counter clockwise
       counterVol --;
     }}
     if (counterVol > 12){
      TidalVol=0;
     }
     else if (counterVol >= 0){
      TidalVol=(counterVol*50)+200;
     }
     else{
      TidalVol=0;
     }
     
     lcd.setCursor(0,1);
     lcd.print("TidalVol:  ");
     lcd.setCursor(11,1);
     lcd.print(TidalVol);
     lcd.setCursor(14,1);
     lcd.print("mL");
}
    previousVolStateCLK = currentVolStateCLK;                                      // Update previousStateCLK with the current stat
}

void updateIERatio() {
if (digitalRead(inputIESW) == 0){               
   currentIEStateCLK = digitalRead(inputIECLK);                                // Read the current state of inputCLK
   if (currentIEStateCLK != previousIEStateCLK){                               // If the previous and the current state of the inputCLK are different then a pulse has occured
       
     if (digitalRead(inputIEDT) != currentIEStateCLK) {                        // If the inputDT state is different than the inputCLK state then
       counterIE ++;                                                               // the encoder is rotating clockwise
       
     } else {                                                                     // Encoder is rotating counter clockwise
       counterIE --;
     }}
     if (counterIE > 4){
      IE=0;
     }
     else if (counterIE >= 0){
      IE=counterIE;
     }
     else{
      IE=0;
     }
     
     lcd.setCursor(0,1);
     lcd.print("Insp/Exp:    1/");
     lcd.setCursor(15,1);
     lcd.print(IE);
}
    previousIEStateCLK = currentIEStateCLK;                                      // Update previousStateCLK with the current stat
}

void updateBPM() {
if (digitalRead(inputBPMSW) == 0){               
   currentBPMStateCLK = digitalRead(inputBPMCLK);                                // Read the current state of inputCLK
   if (currentBPMStateCLK != previousBPMStateCLK){                               // If the previous and the current state of the inputCLK are different then a pulse has occured
       
     if (digitalRead(inputBPMDT) != currentBPMStateCLK) {                        // If the inputDT state is different than the inputCLK state then
       counterBPM ++;                                                               // the encoder is rotating clockwise
       
     } else {                                                                     // Encoder is rotating counter clockwise
       counterBPM --;
     }}
     if (counterBPM > 37){
      BPM=0;
     }
     else if (counterBPM <= 0){
      BPM=0;;
     }
     else{
      BPM=counterBPM+3;
     }
     
     lcd.setCursor(0,1);
     lcd.print("Breaths/Min:   ");
     lcd.setCursor(14,1);
     lcd.print(BPM);
}
    previousBPMStateCLK = currentBPMStateCLK;                                      // Update previousStateCLK with the current stat
}
