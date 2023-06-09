#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hidden = dir(hidden_4)
    for i in hidden:
        if not i.startswith('__'):
            print("{}".format(i))
