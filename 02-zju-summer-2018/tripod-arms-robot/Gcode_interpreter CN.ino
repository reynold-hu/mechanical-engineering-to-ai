char UART_RX;     //串口接收到的字符
int state;        //状态，0为接收到G，1为接收到X 2为接收到F
int readtype=0;      //读取状态，应该读英文时为0，读数字为1
int parameter[3]={0,0,0};  //参数，第一个放G结果，第二个放X结果，第三个放F结果
int current_number;
boolean flag = 0;          //检测输入有没有输错
void setup() {
  Serial.begin(9600);

}
   //G01 X60 F5000
void loop() {
  flag = 0;
  readtype = 0;
  while(Serial.available()==0);           //等待上位机控制
  if(Serial.available()>0)UART_RX=Serial.read();
  do{   //当读取到的不是回车时（命令还没有结束）
    //if(UART_RX==' '&&readtype==0)continue;
    if(readtype==0){
        switch(UART_RX){
        case 'G':
        case 'g':state=0;parameter[state] =0;break;
        case 'X':
        case 'x':state=1;parameter[state] =0;break;
        case 'F':
        case 'f':state=2;parameter[state] =0;break;
        default:Serial.println(UART_RX);break;   //while(Serial.read()!='\n');flag = 1;   //如果发现有错误，一直读掉这句话
        }
    readtype = 1;
    }
    else if(readtype==1){
      if(UART_RX>='0'&&UART_RX<='9'){  
        current_number = UART_RX-'0';
        parameter[state] = parameter[state]*10+current_number;
      }
      else readtype = 0;
    }
  while(Serial.available()==0);
  }while((UART_RX=Serial.read())!='\n');
  switch(parameter[0]){
    case 0:Serial.print("fastmove to X= ");Serial.println(parameter[1]);break;
    case 1:Serial.print("toolfeed to X= ");Serial.print(parameter[1]);Serial.print(" with feedrate f = ");Serial.println(parameter[2]);break;
    case 28:Serial.println("return to Origin");break;
    case 92:Serial.print("set the current x position to ");Serial.println(parameter[1]);break;
    default:Serial.println(parameter[0]);
  }
}
    
    
    
      

