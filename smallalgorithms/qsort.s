	.file	"qsort.i"
	.text
	.p2align 4,,15
	.globl	swap
	.type	swap, @function
swap:
.LFB2:
	.cfi_startproc
	cmpl	%edx, %esi
	je	.L1
	movslq	%esi, %rsi
	movslq	%edx, %rdx
	leaq	(%rdi,%rsi,4), %rcx
	leaq	(%rdi,%rdx,4), %rax
	movl	(%rcx), %esi
	movl	(%rax), %edx
	movl	%edx, (%rcx)
	movl	%esi, (%rax)
.L1:
	rep ret
	.cfi_endproc
.LFE2:
	.size	swap, .-swap
	.p2align 4,,15
	.globl	helper
	.type	helper, @function
helper:
.LFB3:
	.cfi_startproc
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	movslq	%edx, %rax
	movl	%esi, %r10d
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$136, %rsp
	.cfi_def_cfa_offset 192
	cmpl	%eax, %esi
	movl	%eax, 60(%rsp)
	jge	.L4
	leaq	(%rdi,%rax,4), %rax
	movq	%rdi, %r14
	movq	%rax, 104(%rsp)
.L15:
	movslq	%r10d, %rbx
	movl	60(%rsp), %edi
	movl	(%rax), %esi
	movl	(%r14,%rbx,4), %ecx
	movl	%r10d, %r8d
	movq	%rbx, %rdx
	movl	%ecx, %eax
.L13:
	cmpl	%edi, %r8d
	je	.L139
	movslq	%edi, %r9
	leaq	(%r14,%rdx,4), %r11
	leaq	(%r14,%r9,4), %r9
	movl	%esi, (%r11)
	movl	%eax, (%r9)
	movl	(%r11), %r11d
.L7:
	cmpl	%r11d, %ecx
	jle	.L8
	leaq	4(%r14,%rdx,4), %rdx
.L9:
	addq	$4, %rdx
	addl	$1, %r8d
	cmpl	-4(%rdx), %ecx
	jg	.L9
.L8:
	cmpl	%eax, %ecx
	jg	.L10
	movslq	%edi, %rax
	leaq	-4(%r14,%rax,4), %rdx
.L11:
	movq	%rdx, %r9
	subq	$4, %rdx
	movl	4(%rdx), %eax
	subl	$1, %edi
	cmpl	%eax, %ecx
	jle	.L11
.L10:
	cmpl	%r8d, %edi
	jle	.L12
	movslq	%r8d, %rdx
	movl	%eax, %esi
	movl	(%r14,%rdx,4), %eax
	jmp	.L13
.L4:
	addq	$136, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	popq	%rbx
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
.L139:
	.cfi_restore_state
	movl	%eax, %r11d
	leaq	(%r14,%rdx,4), %r9
	movl	%esi, %eax
	jmp	.L7
.L12:
	cmpl	%edi, %r10d
	movq	%r9, 64(%rsp)
	movl	%edi, 20(%rsp)
	movl	%r8d, 120(%rsp)
	movq	%r14, %r13
	jge	.L24
.L110:
	movl	20(%rsp), %edi
	movl	0(%r13,%rbx,4), %edx
	cmpl	%edi, %r10d
	jge	.L101
	movq	64(%rsp), %rax
	movl	%r10d, %esi
	movl	(%rax), %ecx
	movl	%edx, %eax
.L22:
	cmpl	%edi, %esi
	je	.L17
	movslq	%esi, %r8
	leaq	0(%r13,%r8,4), %r8
	movl	%ecx, (%r8)
	movslq	%edi, %rcx
	movl	%eax, 0(%r13,%rcx,4)
	movl	%eax, %ecx
	movl	(%r8), %eax
.L17:
	cmpl	%eax, %edx
	jle	.L18
	movslq	%esi, %rax
	leaq	4(%r13,%rax,4), %rax
.L19:
	addq	$4, %rax
	addl	$1, %esi
	cmpl	-4(%rax), %edx
	jg	.L19
.L18:
	cmpl	%ecx, %edx
	jg	.L20
	movslq	%edi, %rax
	leaq	-4(%r13,%rax,4), %rax
.L21:
	subq	$4, %rax
	movl	4(%rax), %ecx
	subl	$1, %edi
	cmpl	%ecx, %edx
	jle	.L21
.L20:
	cmpl	%esi, %edi
	jle	.L119
	movslq	%esi, %rax
	movl	0(%r13,%rax,4), %eax
	jmp	.L22
.L101:
	movl	%edi, 12(%rsp)
	movl	%r10d, 56(%rsp)
.L16:
	movslq	%edi, %rax
	cmpl	%r10d, %edi
	movq	%r13, %r14
	leaq	0(%r13,%rax,4), %rax
	movq	%rax, 112(%rsp)
	jle	.L26
.L111:
	movl	12(%rsp), %edi
	movl	(%r14,%rbx,4), %ecx
	cmpl	%r10d, %edi
	jle	.L124
	movq	112(%rsp), %rax
	movl	%r10d, %r8d
	movslq	%r10d, %rdx
	movl	(%rax), %esi
	movl	%ecx, %eax
.L34:
	cmpl	%edi, %r8d
	je	.L140
	movslq	%edi, %r9
	leaq	(%r14,%rdx,4), %r11
	leaq	(%r14,%r9,4), %r9
	movl	%esi, (%r11)
	movl	%eax, (%r9)
	movl	(%r11), %r11d
.L28:
	cmpl	%r11d, %ecx
	jle	.L29
	leaq	4(%r14,%rdx,4), %rdx
.L30:
	addq	$4, %rdx
	addl	$1, %r8d
	cmpl	-4(%rdx), %ecx
	jg	.L30
.L29:
	cmpl	%eax, %ecx
	jg	.L31
	movslq	%edi, %rax
	leaq	-4(%r14,%rax,4), %rdx
.L32:
	movq	%rdx, %r9
	subq	$4, %rdx
	movl	4(%rdx), %eax
	subl	$1, %edi
	cmpl	%eax, %ecx
	jle	.L32
.L31:
	cmpl	%r8d, %edi
	jle	.L33
	movslq	%r8d, %rdx
	movl	%eax, %esi
	movl	(%r14,%rdx,4), %eax
	jmp	.L34
.L121:
	movq	%r13, %r14
.L24:
	movl	120(%rsp), %eax
	cmpl	%eax, 60(%rsp)
	jle	.L4
	movl	%eax, %r10d
	movq	104(%rsp), %rax
	jmp	.L15
.L124:
	movq	%r14, %r13
.L26:
	movl	20(%rsp), %eax
	movl	56(%rsp), %r10d
	cmpl	%eax, %r10d
	jge	.L121
	movslq	%r10d, %rbx
	jmp	.L110
.L33:
	cmpl	%edi, %r10d
	movq	%r9, 72(%rsp)
	movl	%edi, 32(%rsp)
	movl	%r8d, 96(%rsp)
	jge	.L47
.L112:
	movl	32(%rsp), %edi
	movl	(%r14,%rbx,4), %ecx
	cmpl	%edi, %r10d
	jge	.L102
	movq	72(%rsp), %rax
	movl	%r10d, %r8d
	movslq	%r10d, %rdx
	movl	(%rax), %esi
	movl	%ecx, %eax
.L45:
	cmpl	%edi, %r8d
	je	.L141
	movslq	%edi, %r9
	leaq	(%r14,%rdx,4), %r11
	leaq	(%r14,%r9,4), %r9
	movl	%esi, (%r11)
	movl	%eax, (%r9)
	movl	(%r11), %r11d
.L39:
	cmpl	%r11d, %ecx
	jle	.L40
	leaq	4(%r14,%rdx,4), %rdx
.L41:
	addq	$4, %rdx
	addl	$1, %r8d
	cmpl	-4(%rdx), %ecx
	jg	.L41
.L40:
	cmpl	%eax, %ecx
	jg	.L42
	movslq	%edi, %rax
	leaq	-4(%r14,%rax,4), %rdx
.L43:
	movq	%rdx, %r9
	subq	$4, %rdx
	movl	4(%rdx), %eax
	subl	$1, %edi
	cmpl	%eax, %ecx
	jle	.L43
.L42:
	cmpl	%r8d, %edi
	jle	.L44
	movslq	%r8d, %rdx
	movl	%eax, %esi
	movl	(%r14,%rdx,4), %eax
	jmp	.L45
.L140:
	movl	%eax, %r11d
	leaq	(%r14,%rdx,4), %r9
	movl	%esi, %eax
	jmp	.L28
.L102:
	movl	%r10d, 28(%rsp)
.L37:
	movl	32(%rsp), %eax
	cmpl	%eax, %r10d
	jge	.L47
	movslq	%r10d, %rbx
	jmp	.L112
.L141:
	movl	%eax, %r11d
	leaq	(%r14,%rdx,4), %r9
	movl	%esi, %eax
	jmp	.L39
.L119:
	movl	%edi, 12(%rsp)
	movl	%esi, 56(%rsp)
	jmp	.L16
.L47:
	movl	12(%rsp), %eax
	movl	96(%rsp), %r10d
	cmpl	%eax, %r10d
	jge	.L124
	movslq	%r10d, %rbx
	jmp	.L111
.L44:
	cmpl	%edi, %r10d
	movl	%edi, 24(%rsp)
	movl	%r8d, 28(%rsp)
	movq	%r9, 80(%rsp)
	jge	.L128
.L113:
	movl	(%r14,%rbx,4), %esi
	movl	24(%rsp), %edi
	movl	%r10d, %r8d
	movslq	%r10d, %rcx
	movl	%esi, %edx
.L56:
	cmpl	%edi, %r8d
	je	.L142
	movslq	%edi, %r9
	leaq	(%r14,%rcx,4), %r11
	leaq	(%r14,%r9,4), %r9
	movl	%eax, (%r11)
	movl	%edx, (%r9)
	movl	(%r11), %r11d
.L50:
	cmpl	%r11d, %esi
	jle	.L51
	leaq	4(%r14,%rcx,4), %rax
.L52:
	addq	$4, %rax
	addl	$1, %r8d
	cmpl	-4(%rax), %esi
	jg	.L52
.L51:
	cmpl	%edx, %esi
	jg	.L53
	movslq	%edi, %rax
	leaq	-4(%r14,%rax,4), %rax
.L54:
	movq	%rax, %r9
	subq	$4, %rax
	movl	4(%rax), %edx
	subl	$1, %edi
	cmpl	%edx, %esi
	jle	.L54
.L53:
	cmpl	%r8d, %edi
	jle	.L55
	movslq	%r8d, %rcx
	movl	%edx, %eax
	movl	(%r14,%rcx,4), %edx
	jmp	.L56
.L128:
	movl	28(%rsp), %r10d
	jmp	.L37
.L142:
	movl	%edx, %r11d
	leaq	(%r14,%rcx,4), %r9
	movl	%eax, %edx
	jmp	.L50
.L55:
	cmpl	%edi, %r10d
	movq	%r9, 40(%rsp)
	movl	%edi, 16(%rsp)
	movl	%r8d, 100(%rsp)
	movl	%r10d, %esi
	jge	.L68
.L114:
	movl	16(%rsp), %edx
	movl	(%r14,%rbx,4), %ecx
	movq	40(%rsp), %rax
	cmpl	%edx, %esi
	jge	.L104
	movl	%edx, %r8d
	movl	%esi, %r9d
	movl	(%rax), %edi
	cmpl	%r8d, %r9d
	movl	%ecx, %eax
	movslq	%esi, %rdx
	je	.L143
.L60:
	movslq	%r8d, %r10
	leaq	(%r14,%rdx,4), %r11
	leaq	(%r14,%r10,4), %r10
	movl	%edi, (%r11)
	movl	%eax, (%r10)
	movl	(%r11), %r11d
.L61:
	cmpl	%r11d, %ecx
	jle	.L62
	leaq	4(%r14,%rdx,4), %rdx
.L63:
	addq	$4, %rdx
	addl	$1, %r9d
	cmpl	-4(%rdx), %ecx
	jg	.L63
.L62:
	cmpl	%eax, %ecx
	jg	.L64
	movslq	%r8d, %rax
	leaq	-4(%r14,%rax,4), %rdx
.L65:
	movq	%rdx, %r10
	subq	$4, %rdx
	movl	4(%rdx), %eax
	subl	$1, %r8d
	cmpl	%eax, %ecx
	jle	.L65
.L64:
	cmpl	%r9d, %r8d
	jle	.L129
	movslq	%r9d, %rdx
	cmpl	%r8d, %r9d
	movl	%eax, %edi
	movl	(%r14,%rdx,4), %eax
	jne	.L60
.L143:
	movl	%eax, %r11d
	leaq	(%r14,%rdx,4), %r10
	movl	%edi, %eax
	jmp	.L61
.L129:
	movl	%r8d, 8(%rsp)
	movl	%r9d, 36(%rsp)
	movq	%r10, 48(%rsp)
.L59:
	cmpl	%esi, 8(%rsp)
	jle	.L79
.L115:
	movl	8(%rsp), %r8d
	movq	48(%rsp), %rax
	movl	%esi, %ebp
	movl	(%r14,%rbx,4), %ecx
	cmpl	%r8d, %ebp
	movl	(%rax), %edx
	movslq	%esi, %rax
	movl	%ecx, %edi
	je	.L144
.L70:
	movslq	%r8d, %r9
	leaq	(%r14,%rax,4), %r10
	leaq	(%r14,%r9,4), %r9
	movl	%edx, (%r10)
	movl	%edi, (%r9)
	movl	(%r10), %r10d
.L71:
	cmpl	%r10d, %ecx
	jle	.L72
	leaq	4(%r14,%rax,4), %rax
.L73:
	addq	$4, %rax
	addl	$1, %ebp
	cmpl	-4(%rax), %ecx
	jg	.L73
.L72:
	cmpl	%edi, %ecx
	jg	.L105
	movslq	%r8d, %rax
	leaq	-4(%r14,%rax,4), %rax
.L75:
	movq	%rax, %r9
	subq	$4, %rax
	movl	4(%rax), %edx
	subl	$1, %r8d
	cmpl	%edx, %ecx
	jle	.L75
	cmpl	%r8d, %ebp
	jge	.L76
.L145:
	movslq	%ebp, %rax
	cmpl	%r8d, %ebp
	movl	(%r14,%rax,4), %edi
	jne	.L70
.L144:
	movl	%edi, %r10d
	leaq	(%r14,%rax,4), %r9
	movl	%edx, %edi
	jmp	.L71
.L105:
	cmpl	%r8d, %ebp
	movl	%edi, %edx
	jl	.L145
.L76:
	cmpl	%r8d, %esi
	movq	%r9, 88(%rsp)
	jge	.L90
	movl	%ebp, 124(%rsp)
	movl	%r8d, %r12d
.L116:
	movl	(%r14,%rbx,4), %ecx
	movl	%r12d, %r13d
	movl	%esi, %r15d
	cmpl	%r13d, %r15d
	movslq	%esi, %rax
	movl	%ecx, %edi
	je	.L146
.L81:
	movslq	%r13d, %r9
	leaq	(%r14,%rax,4), %r8
	leaq	(%r14,%r9,4), %rbp
	movl	%edx, (%r8)
	movl	%edi, 0(%rbp)
	movl	(%r8), %r8d
.L82:
	cmpl	%r8d, %ecx
	jle	.L83
	leaq	4(%r14,%rax,4), %rax
	.p2align 4,,10
	.p2align 3
.L84:
	addq	$4, %rax
	addl	$1, %r15d
	cmpl	-4(%rax), %ecx
	jg	.L84
.L83:
	cmpl	%edi, %ecx
	jg	.L106
	movslq	%r13d, %rax
	leaq	-4(%r14,%rax,4), %rax
	.p2align 4,,10
	.p2align 3
.L86:
	movq	%rax, %rbp
	subq	$4, %rax
	movl	4(%rax), %edx
	subl	$1, %r13d
	cmpl	%edx, %ecx
	jle	.L86
.L85:
	cmpl	%r13d, %r15d
	jge	.L87
	movslq	%r15d, %rax
	cmpl	%r13d, %r15d
	movl	(%r14,%rax,4), %edi
	jne	.L81
.L146:
	movl	%edi, %r8d
	leaq	(%r14,%rax,4), %rbp
	movl	%edx, %edi
	jmp	.L82
.L87:
	cmpl	%r13d, %esi
	jge	.L99
.L117:
	cmpl	%r13d, %esi
	movl	(%r14,%rbx,4), %ecx
	jge	.L107
	movl	%r13d, %edx
	movl	%esi, %ebx
	movl	0(%rbp), %r8d
	cmpl	%edx, %ebx
	movl	%ecx, %edi
	je	.L108
	.p2align 4,,10
	.p2align 3
.L147:
	movslq	%ebx, %rax
	leaq	(%r14,%rax,4), %rax
	movl	%r8d, (%rax)
	movslq	%edx, %r8
	movl	%edi, (%r14,%r8,4)
	movl	(%rax), %eax
.L93:
	cmpl	%eax, %ecx
	jle	.L94
	movslq	%ebx, %rax
	leaq	4(%r14,%rax,4), %rax
	.p2align 4,,10
	.p2align 3
.L95:
	addq	$4, %rax
	addl	$1, %ebx
	cmpl	-4(%rax), %ecx
	jg	.L95
.L94:
	cmpl	%edi, %ecx
	jg	.L109
	movslq	%edx, %rax
	leaq	-4(%r14,%rax,4), %rax
	.p2align 4,,10
	.p2align 3
.L97:
	subq	$4, %rax
	movl	4(%rax), %r8d
	subl	$1, %edx
	cmpl	%r8d, %ecx
	jle	.L97
.L96:
	cmpl	%edx, %ebx
	jge	.L92
	movslq	%ebx, %rax
	cmpl	%edx, %ebx
	movl	(%r14,%rax,4), %edi
	jne	.L147
.L108:
	movl	%edi, %eax
	movl	%r8d, %edi
	jmp	.L93
.L107:
	movl	%r13d, %edx
	movl	%esi, %ebx
.L92:
	movq	%r14, %rdi
	call	helper
	cmpl	%r13d, %ebx
	jge	.L99
	movl	%ebx, %esi
	movslq	%ebx, %rbx
	jmp	.L117
.L109:
	movl	%edi, %r8d
	jmp	.L96
.L99:
	cmpl	%r12d, %r15d
	jge	.L135
	movq	88(%rsp), %rax
	movl	%r15d, %esi
	movslq	%r15d, %rbx
	movl	(%rax), %edx
	jmp	.L116
.L106:
	movl	%edi, %edx
	jmp	.L85
.L135:
	movl	124(%rsp), %ebp
.L90:
	cmpl	%ebp, 8(%rsp)
	jle	.L79
	movl	%ebp, %esi
	movslq	%ebp, %rbx
	jmp	.L115
.L79:
	movl	16(%rsp), %eax
	movl	36(%rsp), %esi
	cmpl	%eax, %esi
	jge	.L68
	movslq	%esi, %rbx
	jmp	.L114
.L104:
	movq	%rax, 48(%rsp)
	movl	16(%rsp), %eax
	movl	%esi, 36(%rsp)
	movl	%eax, 8(%rsp)
	jmp	.L59
.L68:
	movl	24(%rsp), %eax
	movl	100(%rsp), %r10d
	cmpl	%eax, %r10d
	jge	.L128
	movq	80(%rsp), %rax
	movslq	%r10d, %rbx
	movl	(%rax), %eax
	jmp	.L113
	.cfi_endproc
.LFE3:
	.size	helper, .-helper
	.p2align 4,,15
	.globl	m_qsort
	.type	m_qsort, @function
m_qsort:
.LFB4:
	.cfi_startproc
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	pushq	%r12
	.cfi_def_cfa_offset 24
	.cfi_offset 12, -24
	pushq	%rbp
	.cfi_def_cfa_offset 32
	.cfi_offset 6, -32
	leal	-1(%rsi), %ebp
	pushq	%rbx
	.cfi_def_cfa_offset 40
	.cfi_offset 3, -40
	subq	$8, %rsp
	.cfi_def_cfa_offset 48
	testl	%ebp, %ebp
	jle	.L148
	movslq	%ebp, %rax
	movq	%rdi, %r13
	xorl	%esi, %esi
	leaq	(%rdi,%rax,4), %r12
.L158:
	movslq	%esi, %rax
	movl	%ebp, %edx
	movl	%esi, %ebx
	movl	0(%r13,%rax,4), %ecx
	cmpl	%edx, %ebx
	movl	(%r12), %r8d
	movl	%ecx, %edi
	je	.L159
	.p2align 4,,10
	.p2align 3
.L162:
	movslq	%ebx, %rax
	leaq	0(%r13,%rax,4), %rax
	movl	%r8d, (%rax)
	movslq	%edx, %r8
	movl	%edi, 0(%r13,%r8,4)
	movl	(%rax), %eax
.L150:
	cmpl	%eax, %ecx
	jle	.L151
	movslq	%ebx, %rax
	leaq	4(%r13,%rax,4), %rax
	.p2align 4,,10
	.p2align 3
.L152:
	addq	$4, %rax
	addl	$1, %ebx
	cmpl	-4(%rax), %ecx
	jg	.L152
.L151:
	cmpl	%edi, %ecx
	jg	.L160
	movslq	%edx, %rax
	leaq	-4(%r13,%rax,4), %rax
	.p2align 4,,10
	.p2align 3
.L154:
	subq	$4, %rax
	movl	4(%rax), %r8d
	subl	$1, %edx
	cmpl	%r8d, %ecx
	jle	.L154
.L153:
	cmpl	%edx, %ebx
	jge	.L155
	movslq	%ebx, %rax
	cmpl	%edx, %ebx
	movl	0(%r13,%rax,4), %edi
	jne	.L162
.L159:
	movl	%edi, %eax
	movl	%r8d, %edi
	jmp	.L150
.L155:
	movq	%r13, %rdi
	call	helper
	cmpl	%ebx, %ebp
	jle	.L148
	movl	%ebx, %esi
	jmp	.L158
.L160:
	movl	%edi, %r8d
	.p2align 4,,4
	jmp	.L153
.L148:
	addq	$8, %rsp
	.cfi_def_cfa_offset 40
	popq	%rbx
	.cfi_def_cfa_offset 32
	popq	%rbp
	.cfi_def_cfa_offset 24
	popq	%r12
	.cfi_def_cfa_offset 16
	popq	%r13
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE4:
	.size	m_qsort, .-m_qsort
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"%d "
	.section	.text.startup,"ax",@progbits
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB5:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movl	$4, %edx
	xorl	%esi, %esi
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	subq	$40, %rsp
	.cfi_def_cfa_offset 64
	leaq	24(%rsp), %rbp
	movq	%rsp, %rdi
	movq	%rsp, %rbx
	movl	$34, (%rsp)
	movl	$14, 4(%rsp)
	movl	$98, 8(%rsp)
	movl	$2, 12(%rsp)
	movl	$72, 16(%rsp)
	movl	$39, 20(%rsp)
	call	helper
	.p2align 4,,10
	.p2align 3
.L165:
	movl	(%rbx), %esi
	xorl	%eax, %eax
	movl	$.LC0, %edi
	addq	$4, %rbx
	call	printf
	cmpq	%rbp, %rbx
	jne	.L165
	movl	$10, %edi
	call	putchar
	addq	$40, %rsp
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE5:
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 4.8.1-10ubuntu8) 4.8.1"
	.section	.note.GNU-stack,"",@progbits
