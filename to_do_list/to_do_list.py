"""
This is a simple to-do list program.
    
    Usage:
    
    ./to_do_list.py --add text
    ./to_do_list.py --show [--all] # Only show today's work default
    
    Data are stored in ./to_do_list.
    Please input text as this module : 'date' + ' | ' + 'Your work'.
    e.g : '20:15 | Do my homework' 
"""

import time
import json
import sys
import re
import textwrap

now_time = time.ctime()
now_time = now_time[4:10] + now_time[19:]

with open('to_do_list.txt', 'r') as f:
    work_list = json.load(f)

def add(work):  
    if not work_list.get(now_time):
        work_list[now_time] = [str(work)]
    else:
        work_list[now_time].append(str(work))
    return work_list

def show(flag):
    for time in work_list.keys():
        work_list[time] = sorted(work_list[time], key=fun)

    if not flag:
        if not work_list.get(now_time):
            print("You haven't work to do.")
        else:
            print("\n".join(work_list[now_time]))
    else:
        print("All the work list:")
        for time in work_list.keys():
            print(time + ' : ')
            print('\n'.join(work_list[now_time]))

def fun(text):
    text = text[0:5]
    text = text.replace(':', '.')
    return text

def main():
    args = sys.argv[1:]
    flag = False

    if not args:
        print(textwrap.dedent(
        """Usage:  
           ./to_do_list.py --add text
           ./to_do_list.py --show [--all] # Only show today's work default"""
        ))
        sys.exit(1)

    if args[0] == '--add':
        if not re.search(r'\d\d:\d\d', args[1]):
            print(textwrap.dedent(
            """Please input your work list correctly.
               e.g : --add 20:15 Do my homework"""
            ))
            sys.exit(1)
        else:
            add(' '.join(args[1:]))

    if args[0] == '--show':
        del args[0]
        if len(args) > 0 and args[0] == '--all':
            flag = True
        show(flag)

    with open('to_do_list.txt', 'w') as f:
        json.dump(work_list, f)

    sys.exit(0)

if __name__ == '__main__':
    main()



