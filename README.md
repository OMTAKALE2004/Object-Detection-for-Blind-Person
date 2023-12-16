## Object Detection for Blind Person using Raspberry Pi

##  What is this Project?
Here we will create a stand alone system using rasperry pi, PiCamera and ultrasonic sensor to detect and name the objects in the path of blind person and give a voice output about it.The end product would be a wearable device that a blind person can wear on his/her head.




## Project Requirement

- Rasperry Pi [I used Raspberry Pi 3B]
- PiCamera3
- Ultrasonic Sensor HC-SR04
- Some jumper cables,1k and 1.8k resistors and zero pcb
- Earphones for speech output

## Steps to run the project on Raspberry Pi

Install Raspberry Pi Bullseye 64 bit Operating system.[I recommend to start with a fresh SD card for this project]

Write the following commands on the Raspberry Pi terminal

- Update and upgrade Raspberry Pi
```bash
sudo apt-get update
sudo apt-get upgrade
```
- Make your project directory on Raspberry pi.In this directory we install all the dependencies and packages required for the project
```bash
mkdir Object_detection_for_blind_person
cd Object_detection_for_blind_person
mkdir tLite
cd tLite
```
- Now dowmload all tensorflow lite related things from GitHub repository
```bash
git clone https://github.com/tensorflow/examples --depth 1
```
- Now perform the following commands to configure all thing properly

```bash
cd examples
cd lite
cd examples
ls
cd Object_detection
```
```bash
cd raspberry_pi
sh setup.sh
ls
mv efficientdet_lite0.tflite ~/Object_detection_for_blind_person
mv utils.py ~/Object_detection_for_blind_person
```
We are now done setting up tensorflow lite.Close the terminal and open new terminal and perform following commands
- Install python libraries for text to speech
```bash
pip install pyttsx3
pip install python-espeak
```
Now create a .py file in your project directory,in this file we will write all our project code.

- If you get some error like 'GLIBCXX_3.4.29'not found then
```bash
python -m pip install --upgrade tflite-support==0.4.3
```


## Connecting all the things
- Connect the PiCamera to the camera port available on  Raspberry Pi.

- Connect Ultrasonic Sensor to raspberry pi
    
    Ultrasonic Sensor HC-SR04 echo pin output is 5v and Raspberry pi requries 3.3v input in GPIO pins so we need to reduce 5v to 3.3v or below.
    
    To do this we will use 1k and 1.8k resistor which will make 5v to apporx 3.2v.You can also use any other resistor combination but ensure that the voltage is 3.3v or below it.

    Interfacing diagram of HC-SR04 :-
  
  <img src="https://github.com/OMTAKALE2004/Object-Detection-for-Blind-Person/assets/111902987/d12713ff-d96c-4736-b8e7-e7ca26c5d7e1" width="50%">

  After doing all the connection and installation properly we are now ready with project.
  Now just copy the code in detect.py file in the python file you created in your project directory and run it using any IDE supported by Raspberry Pi[I prefer Thorny].


  ## Flowchart

  <img src="https://github.com/OMTAKALE2004/Object-Detection-for-Blind-Person/assets/111902987/f6b05cac-10ed-4005-bb05-f8240d236f3e"  width="50%" height="60%">



## Project Design

<table border="1px">
<tr>
     <th>
            <img src="https://github.com/OMTAKALE2004/Object-Detection-for-Blind-Person/assets/111902987/4adcbbd7-ec3f-4f1b-901a-66e11b314414" width="75%">
        </th>
         <th>
            <img src="https://github.com/OMTAKALE2004/Object-Detection-for-Blind-Person/assets/111902987/15d65407-67cf-4619-abf9-ec53f933a48d" width="75%">
        </th>
</tr>
       
            
    

        
</table>

## Video of project :
https://youtu.be/nzOgw3UxZWM?si=EqH9-3wxSDYZnIQW 

<br>

  In case any query feel free to ask me at
  Gmail- om2004takale@gmail.com



