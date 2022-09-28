# Overflows Demo Code

Quick Description of the source files and instructions for compiling

## Getting things setup

For the majority of these examples we are going to turn a lot of protections
off, and compile in 32 bit addressing mode.

For this we will need to install the gcc-multilib package

```
apt install gcc-multilib
```

To disable ALSR run the following

```
$sudo su
#echo 0 > /proc/sys/kernel/randomize_va_space
exit
```

# Programs

## strOverflow.c

Simple program demonstrating what happens when we try to copy too much information to a string.

```
//Compile
gcc strOverflow.c

//run
./a.out
```

