int analogPin = 0;    
int val = 0;         
String p;
void setup()
{
  Serial.begin(19200);         

}

void loop()

{

  val = analogRead(analogPin); 

  //Serial.println(val);         

 if (val<=310)
    {  //p ="jump";
  Serial.println("jump"); 
 }
  else
 { // p = "Null";
  Serial.println("donothing");
  }


}
