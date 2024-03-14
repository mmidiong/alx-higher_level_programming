#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    name = dir(hidden_4)
    for n in range(len(name)):
        if name[ni][0] != "_" and name[n][1] != "_":
            print(name[n])
