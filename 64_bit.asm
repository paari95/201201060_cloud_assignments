SECTION .data

Hello:		db "Hello world!",10
len_Hello:	equ $-Hello

SECTION .text

global _start

_start:
mov rax,1			
mov rdi,1			
mov rsi,Hello		
mov rdx,len_Hello	
syscall

mov rax,60			
mov rdi,0		
syscall
