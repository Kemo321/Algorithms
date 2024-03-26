	.data
prompt: .asciz "Enter string\n"
input:	.space 100
	.text
	.global main

main:
	# Print the prompt
	li a7, 4
	la a0, prompt
	ecall
	# Read the input 
	li a7, 8
	la a0, input
	li a1, 100
	ecall
	# Add for reference
	li t0, '0'
	li t1, '9'
	# Initialize two pointers
	la t2, input
	la t3, input
	j outer_loop

outer_loop:
	# Load the input at t2 address
	lb t4, 0(t2)
	# Increment t2 pointer
	addi t2, t2, 1
	# If t4 == '\n' jumpt to end
	beqz t4, end
	# If t4 < '0' or t4 > '9' jump to append
	blt t4, t0, append
	bgt t4, t1, append
	# Else iterate
	j outer_loop
append:
	# Store t4 at t3 address
	sb t4, 0(t3)
	# Increment t3 pointer
	addi t3, t3, 1
	b outer_loop
end:
	# Add '0\'
	sb zero, 0(t3)
	# Print output
	li a7, 4
	la a0, input
	ecall
	# Exit
	li a7, 10
	ecall
	