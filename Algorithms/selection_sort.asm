	.data
prompt: .asciz "Enter string\n"
buf:	.space 100
	.text
	.global main
	
main:
	# Print prompt
	li a7, 4
	la a0, prompt
	ecall
	# Read input
	li a7, 8
	la a0, buf
	li a1, 100
	ecall
	# Set t0 -> start of buf
	la t0, buf
	addi t0, t0, -1 # Decrement because outer_loop starts with t0 += 1
	# Jump to outer_loop
	b outer_loop

outer_loop:
	# Increment t0
	addi t0, t0, 1
	# Load content at t0 to t2
	lb t2, 0(t0)
	# If t2 == \0 end
	beqz t2, end
	# Set right pointer for outer loop
	mv t1, t0
	b inner_loop
	
inner_loop:
	# Increment right pointer
	addi t1, t1, 1
	# Load content at t1 to t3
	lb t3, 0(t1)
	# If \0 encountered go to outer loop
	beqz t3, outer_loop
	# If t3 < t2 swap
	blt t3, t2, swap
	j inner_loop

swap:
	# Swap values
	sb t3, 0(t0)
	sb t2, 0(t1)
	# Update lowest value
	mv t2, t3
	j inner_loop

end:
	# Print result
	li a7, 4
	la a0, buf
	ecall
	# Exit
	li a7, 10
	ecall