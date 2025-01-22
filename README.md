# Tektronics-4051-Emulator-file-conversion
With thanks to Monty McGraw for his time.

pre-reqs : python 3 must be installed (and the emulator of course 😎) .

A simple program to convert a text file to the Tektronics 4051 Emulator flash drive format

A simple program for use with text files, specifacally source code e.g. BASIC programs written in e.g. notepad. It will convert the file and filename to be compatible with the flash drive format used by the very cool and groovy Tektronics 4051 emulator ( https://github.com/mmcgraw74/Tektronix-4051-Emulator ).

Usage : python win2tec.py filename.bas

For example: We have a simple program SINEWAVE2.bas, written using notepad.

SINEWAVE2.bas
=============

100 REM sine wave <br/>
101 INIT   <br/>
105 PAGE  <br/>
110 WINDOW -100,100,-100,100  <br/>
120 AXIS 20,20  <br/>
130 MOVE -80,-23  <br/>
140 FOR I=-80 TO 80  <br/>
150 DRAW I,SIN(I/5)*I  <br/>
160 NEXT I  <br/>
170 HOME  <br/>

We can then run :
                  python win2tek.py SINEWAVE2.bas

This will give the following output:

Filename: SINEWAVE2.bas  <br/>
File Size in Bytes is 171  <br/>
Converting to Tec format  <br/>
New file size : 160  <br/>
Writing Tectronix 4051 emulator flash drive format file...  <br/>
New Filename: 1      ASCII   PROG SINEWAVE2 160  <br/>

You can then import the file ' 1      ASCII   PROG SINEWAVE2 160' into the emulator and use the AUTO LOAD button or type the usual:

FIND@5:1  <br/>
OLD@5:  <br/>

and then:

RUN

![Alt text](https://github.com/Wayne-AJP-Byrne/Tectronics-4051-Emulator-file-conversion/blob/main/SINEWAVE2.png "Sine Wave Example")

and voila, we have loaded and run our program.

Again, a major shout out to Monty McGraw for his time and patience.


