import time

def teletype_print(text,delay=0.2):
    for ch in text:
        # print(ch,end='')
        print(ch,end='')
        time.sleep(delay)

teletype_print('Hello world')
