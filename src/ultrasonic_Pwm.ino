/**************************************************
Credit to Gaurav Kumar (Techeonics) 
<thetecheonics@gmail.com>
***************************************************/

/*
distance value is obtained from the ultrasonic Pulse width output. This measures the duration of the pulse emmited from the base. 
After distance is calculated, the values are sorted and filtered to get a more accurate value.
If the value is below 250cm, the haotic motor vibrates. The intensity increases as the distance decreases. 
*/

#include <Wire.h>
#include "Adafruit_DRV2605.h"

Adafruit_DRV2605 drv;

int pw_pin=7;
int arraysize = 9;
int array[] = { 0, 0, 0, 0, 0, 0, 0, 0, 0};
long inch;
int exact_cm_value;



void setup() 
/*
Set up: haptic motor is initialized. 
PW pin is set as input. 
Serial Monitor is initialized. 
*/
{
drv.begin();
  
  drv.setMode(DRV2605_MODE_INTTRIG); 
  drv.selectLibrary(1); //haptic waveform library is selected

pinMode(pw_pin, INPUT); //pw_pin set as an input pin 
Serial.begin(9600); 
}


void sensorRead()

/*measures the duration of the pulse recieved from sensor, 
converts it to centimeters, and stores it in an array
*/
{
for(int i = 0; i < arraysize; i++)
{
inch = pulseIn(pw_pin, HIGH); 
array[i] = inch/58;
delay(10); 
}
}

void array_arrangment(int *a,int n){

/*arranges element into array of assending order 
*/
for (int i = 1; i < n; ++i)
{
int j = a[i];
int k;
for (k = i - 1; (k >= 0) && (j < a[k]); k--)
{
a[k + 1] = a[k];
}
a[k + 1] = j;
}
}


int filter(int *a,int n)
/* filters distance values to obtain a more accurate measurement.
It counts the occurrences of each distance value 
and keeps track of the maximum count and the corresponding value */

{
int i = 0;
int count = 0;
int maxCount = 0;
int filter = 0;
int median;
int prevCount = 0;
while(i<(n-1)){
prevCount=count;
count=0;
while(a[i]==a[i+1]){
count++;
i++;
}
if(count>prevCount && count>maxCount){
filter=a[i];
maxCount=count;
median=0;
}
if(count==0){
i++;
}
if(count==maxCount){//If the dataset has 2 or more modes.
median=1;
}
if(filter==0||median==1){//Return the median if there is no mode.
filter=a[(n/2)];
}

return filter;

}
}


void loop() {
/* Calls sensorRead function to obtain distance values,
array_arrangment sorts values into asccending order,
filtered distance is printed. 

haptic motor is set to vibrate based on value of exact_cm_value.
A more intense buzz vibrates the smaller the value is. 
This is repreated every 100ms 

*/
sensorRead();
array_arrangment(array,arraysize);
exact_cm_value= filter(array,arraysize);
Serial.print(exact_cm_value);
Serial.println(" cm ");


if ((exact_cm_value <= 400)  && (exact_cm_value > 320) ) { //4m to 3.2m
  
  drv.setWaveform(0, 68);  // 20%

  drv.go(); 
}
else if ((exact_cm_value <= 320)  && (exact_cm_value > 240) ) { //3.2m to 2.4m
  drv.setWaveform(0, 67);  // 40%

  drv.go();
}

else if ((exact_cm_value <= 240)  && (exact_cm_value > 160)) { //2.4m to 1.6m
  drv.setWaveform(0, 66);  // 60%
  
  drv.go();
}

else if ((exact_cm_value <= 160)  && (exact_cm_value > 80)) { //1.6m to .8m
  drv.setWaveform(0, 65);  // 80%
  
  drv.go();
}

else if (exact_cm_value <= 80) { //.8m to 0m 
  drv.setWaveform(0, 64);  // 100%
  drv.go();
}

delay(100);

}
