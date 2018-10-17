# Lego dev


## Doc

### ev3 python
https://github.com/ev3dev/ev3dev-lang-python

### docs

https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/


### python gridwalk
https://github.com/danieljjh/notes/blob/master/docs/gridwalk.py


### line follower example 1

https://github.com/Klabbedi/ev3


https://gist.githubusercontent.com/CS2098/ecb3a078ed502c6a7d6e8d17dc095b48/raw/97d4a6bd286b704dfc43661e7cc32c721372e9fa/line_follower.py

### PID line follower
http://www.inpharmix.com/jps/PID_Controller_For_Lego_Mindstorms_Robots.html


https://builderdude35.com/2016/10/06/pid-line-follower-for-ev3-the-ultimate-line-follower/

### sample code
```python
Pseudo code for the PID controller
To add the derivative term to the controller we need to add a new variable for Kd and a variable to remember the last error. And don't forget that we are multiplying our Ks by 100 to help with the integer math.

Kp = 1000                             ! REMEMBER we are using Kp*100 so this is really 10 !
Ki = 100                              ! REMEMBER we are using Ki*100 so this is really 1 !
Kd = 10000                            ! REMEMBER we are using Kd*100 so this is really 100!
offset = 45                           ! Initialize the variables
Tp = 50 
integral = 0                          ! the place where we will store our integral
lastError = 0                         ! the place where we will store the last error value
derivative = 0                        ! the place where we will store the derivative
Loop forever
   LightValue = read light sensor     ! what is the current light reading?
   error = LightValue - offset        ! calculate the error by subtracting the offset
   integral = integral + error        ! calculate the integral 
   derivative = error - lastError     ! calculate the derivative
   Turn = Kp*error + Ki*integral + Kd*derivative  ! the "P term" the "I term" and the "D term"
 Turn = Turn/100                      ! REMEMBER to undo the affect of the factor of 100 in Kp, Ki and Kd!
   powerA = Tp + Turn                 ! the power level for the A motor
   powerC = Tp - Turn                 ! the power level for the C motor
   MOTOR A direction=forward power=PowerA   ! actually issue the command in a MOTOR block
   MOTOR C direction=forward power=PowerC   ! same for the other motor but using the other power level
   lastError = error                  ! save the current error so it can be the lastError next time around
end loop forever                      ! done with loop, go back and do it again.
```
