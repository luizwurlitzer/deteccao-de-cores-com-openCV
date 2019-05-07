int estado;
int porta_rele1 = 9;
int porta_rele2 = 8;
 
void setup()
{
  Serial.begin(9600);
  pinMode(porta_rele1, OUTPUT); 
  pinMode(porta_rele2, OUTPUT);
}
  
void loop()
{
  
     
  if (Serial.available() > 0) {
    char opcao = Serial.read();
     
  
  if(opcao=='1'){
     digitalWrite(porta_rele1, LOW); //Desliga rele 2
     digitalWrite(porta_rele2, LOW); //Desliga rele 2
  }
  else if(opcao=='0'){
     digitalWrite(porta_rele1, HIGH); //Desliga rele 2
     digitalWrite(porta_rele2, HIGH); //Desliga rele 2
  }
  }
}
 
