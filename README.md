# Tectronics-4051-Emulator-file-conversion
With thanks to Monty McGraw for his time.

pre-reqs : python 3 must be installed.

A simple program to convert a text file to the Tectronics 4051 Emulator flash drive format

A simple program for use with text files, specifacally source code e.g. BASIC programs written in e.g. notepad. It will convert the file and filename to be compatible with the flash drive format used by the very cool and groovy Tectronics 4051 emulator ( https://github.com/mmcgraw74/Tektronix-4051-Emulator ).

Usage : python win2tec.py filename.bas

For example: We have a simple program SINEWAVE2.bas, written using notepad.

SINEWAVE2.bas
=============

100 REM sine wave
101 INIT
105 PAGE
110 WINDOW -100,100,-100,100
120 AXIS 20,20
130 MOVE -80,-23
140 FOR I=-80 TO 80
150 DRAW I,SIN(I/5)*I
160 NEXT I
170 HOME

We can then run :
                  python win2tec SINEWAVE2.bas

This will give the following output:

Filename: SINEWAVE2.bas
File Size in Bytes is 171
Converting to Tec format
New file size : 160
Writing Tectronix 4051 emulator flash drive format file...
New Filename: 1      ASCII   PROG SINEWAVE2 160

You can then import the file ' 1      ASCII   PROG SINEWAVE2 160' into the emulator and use the AUTO LOAD button or type the usual:

FIND@5:1
OLD@5: 

and then:

RUN

and voila, we have loaded and run our program.

A major shout out to Monty McGraw for his time.


