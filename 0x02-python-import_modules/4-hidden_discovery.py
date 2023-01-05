#!/usr/bin/python3
import hidden_4 
if __name__ == "__main__":
    compiled_module = dir(hidden_4)
    length = len(compiled_module)
    for i in range(length):
        if compiled_module[i][0:2] != '__':
            print(compiled_module[i])
