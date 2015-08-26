section .data                           
Hello:     db 'Hello world!',10 
len_Hello: equ $ - Hello                    


section .text                           
global _start                           
_start:                                 
mov eax,4                   
mov ebx,1                   
mov ecx,Hello                 
mov edx,len_Hello             
int 80h                      
mov eax,1                   
mov ebx,0                   
int 80h                      
