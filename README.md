<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>

# Assignment

### Double Pendulum

This is a ```PyQt``` Application simulating the motion of double pendulums. This application uses Runge-Kutta fourth-order numerical solution method to calculate pendulums' position.  

* **Instruction** :  
In this application, the user can adjust the **pendulum mass**, the **cycloid length**, the **initial phase (theta)**, and the **initial angular velocity** of the two pendulums by adjusting the slider bar or by typing a value on the left side of the interface, and can adjust the magnitude of the gravitational acceleration.  
    * Press "**Default**" to restore the default values  
    * Press "**Start**" to start the simulation  
    * Press "**Pause**" to pause the simulation  
    * Press "**Resume**" to resume the simulation  
    * Press "**Stop**" to stop the simulation and the pendulums return to the initial states  

* **Physical Quantities** :  
All physical quantities are in use of **International System of Units** (SI) and angular dimensions are in use of **degrees** ($^{\circ}$).  
    * Range of pendulum mass is $0.01-10.00$ kg  
    * Cycloid length is $0.01-2.00$ m  
    * Initial phase is $-180.0-180.0^{\circ}$  
    * Initial angular velocity is $-200.0-200.0^{\circ}$/s  
    ( the phase is $0$ in the vertical downward direction, and increases in the clockwise direction )  
    * Range of gravitational acceleration is $1.00-20.00$ m/s$^{2}$  
    * Default pendulum mass, cycloid length, initial phase and initial angular velocity is $1.00$ kg , $1.00$ m , $90.0^{\circ}$ , $0.0^{\circ}$/s , respectively. Default gravitational acceleration is $9.80$ m/s$^{2}$.  

* **Development Environment** :  
Python 3.7.0  
PyQt5 5.11.2  
numpy 1.14.5  
Operating System : macOS Mojave, version 10.14 Beta

* **Coded by** : Cui Xiaomei（崔小梅）  
* **Student ID** : 1800947899  
* **Date** : August 1, 2018  

*MathJax Used in this file*
