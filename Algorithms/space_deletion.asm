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
	# For reference
	li t0, ' '
	# Initialize two pointers
	la t1, input
	la t2, input
	j outer_loop

outer_loop:
	# Load the input at t1 address
	lb t3, 0(t1)
	# Increment t1 pointer
	addi t1, t1, 1
	# If t3 = '\0' end
	beqz t3, end
	# If not equal to ' ' append
	bne t3, t0, append
	# Else iterate
	beq t3, t0 outer_loop

append:
	# Store t3 at t2 address
	sb t3, 0(t2)
	# Increment t2 pointer
	addi t2, t2, 1
	b outer_loop

end:
	# Add '0\'
	sb zero, 0(t2)
	# Print output
	li a7, 4
	la a0, input
	ecall
	# Exit
	li a7, 10
	ecall
	
	