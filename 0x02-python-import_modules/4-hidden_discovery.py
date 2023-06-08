#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for i in range(len(dir(hidden_4))):
        if dir(hidden_4)[i][:2] != "__":
            print(dir(hidden_4)[i])
