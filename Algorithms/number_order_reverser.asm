	.data
prompt: .asciz "Enter string\n"
buf:	.space 100
	.text
	.global main

main:
	# Print the prompt
	li a7, 4
	la a0, prompt
	ecall
	# Read input from the user
	li a7, 8
	la a0, buf
	li a1, 100
	ecall
	# Initialize references and left, right pointers
	li t0, '0'
	li t1, '9'
	la t2, buf
	mv t3, t2
	# Set t3 to the end of buf
	addi t3, t3, 100
	# Load values at t2, t3
	lb t4, 0(t2)
	lb t5, 0(t3)
	# Jump
	j look_for_terminator
look_for_terminator:
	# When '\n' encountered jump to loop
	lb t5, 0(t3)
	beq zero, t5, loop
	addi t3, t3, -1
	j look_for_terminator
loop:
	# If t2 >= t3 end
	bge t2, t3, end
	# Jump until both t2, t3 point at digits
	blt t4, t0 left_increment
	blt t5, t0 right_decrement
	bgt t4, t1 left_increment
	bgt t5, t1 right_decrement
	# Swap two digits
	b swap
left_increment:
	# Increment t2, and load new data to t4
	addi t2, t2, 1
	lb t4, 0(t2)
	b loop
	
right_decrement:
	# Increment t3, and load new data to t5
	addi t3, t3, -1
	lb t5, 0(t3)
	b loop
swap:
	# Swap values at t2, t3
	sb t4, (t3)
	sb t5, (t2)
	addi t2, t2, 1
	addi t3, t3, -1
	lb t4, 0(t2)
	lb t5, 0(t3)
	b loop
end:
	# Print result
	li a7, 4
	la a0, buf
	ecall
	# Exit
	li a7, 10
	ecall
	
	
