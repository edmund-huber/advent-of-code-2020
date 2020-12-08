#!/usr/bin/env python3
import copy

instructions = []
with open('input.txt') as f:
    for line in f:
        line = line.rstrip()
        op, value = line.split(' ')
        instructions.append([op, int(value)])

def emulate(ins):
    pc = 0
    reg = 0
    done = 0
    while pc < len(ins):
        assert pc >= 0
        inst, value = ins[pc]
        if inst == 'nop':
            pc += 1
        elif inst == 'acc':
            reg += value
            pc += 1
        elif inst == 'jmp':
            pc = pc + value
        done += 1
        if done == 10000:
            return False
    return reg

for i in range(len(instructions)):
    ins = copy.deepcopy(instructions)
    if ins[i][0] == 'nop':
        ins[i][0] = 'jmp'
    elif ins[i][0] == 'jmp':
        ins[i][0] = 'nop'
    reg = emulate(ins)
    if reg != False:
        print('answer:')
        print(reg)
        break
