import os
import pyautogui
os.chdir('C:\\Users\\mieri\\OneDrive\\Documents\\Python\\Personal_Projects\\5_Automatic_Code_Creation')

from pynput import keyboard
from pynput import mouse

keys = []
space_needed = False
can_write = None

def on_press(key):
    global keys
    k = str(key).replace("'","")
    if k.find('ctrl_r') > 0:
        wait_time()
        keys.append(key+' '+str(O))
    keys.append(key)
    print('{0} pressed'.format(key))
    
def add_space(do_we_need_it):
    global space_needed
    if do_we_need_it == True:
        space_needed = False
        return ' '
    
def wait_time():
    global O
    O = 4

def write_file(keys):
    global space_needed,can_write 
    with open('5_Preprocessing.txt','a') as F:
        for key in keys:
            k = str(key).replace("'","")
            if k.find('space') != 1:
                F.write(add_space(space_needed)+' ')
            elif k.find('backspace'):
                space_needed = True
                F.write('<Backspace Button>') 
            elif  k.find('enter') != 1:
                F.write('Enter')
            elif k.find('up') != 1:
                space_needed = True
                F.write('Up_Button')
            elif k.find('down') != 1:
                space_needed = True
                F.write('Down_Button')
            elif k.find('shift') != 1:
                F.write('')
                if keys[-2] != keys[-1]:
                    F.write(add_space(space_needed)+'<Shift>')
            elif len(keys) != 1:
                space_needed = True
                if keys[0] == 'Button.left':
                    F.write('Left_Click '+str(keysy[1])+' '+str(keys[2]))
                elif keys[0] == 'Button.right':
                    F.write('Right_Click '+str(keys[1])+' '+str(keys[2]))
                elif keys[0] == 'Button.middle':
                    F.write('Middle_Click '+str(keys[1])+' '+str(keys[2]))
                elif keys[0] == 'Mouse.scroll':
                    F.write('Mouse_Scroll '+str(keys[1])+' '+str(keys[2])+' '+str(keys[3]))
            elif k.find('left') != 1:
                space_needed = False
                F.write('Left_Button')
            elif k.find('right') != 1:
                space_needed = False
                F.write('Right_Button')
            elif k.find('ctrl_l') != 1:
                space_needed = True
                if keys[-2] != keyst[-1]:
                    F.write('Mouse_Drag')
            elif k.find('ctrl_r') != 1:
                space_needed = True
                if len(keys) == 1:
                    F.write('Wait_Time '+str(T))
                else:
                    if keys[-2] != keys[-1]:
                        wait_time()
                        F.write('Wait_Time '+str(O))
            elif k.find('alt_l') != 1:
                space_needed = True
                if len(keys) == 2:
                    F.write('Loop_Start')
                else:
                    if keys[-2] != keys[-1]:
                        F.write('Loop_Start')
            elif k.find('alt_r') != 1:
                space_needed = False
                if keys[-2] != keys[-1]:
                    F.write('Loop_End')
            elif k.find('insert') != 1:
                space_needed = False
                if keys[-2] != keys[-1]:
                    text_insert()
                    add_space(space_needed)
                    F.write(str(O)+str(T))
                    can_write = True
            elif (k.find('Key') == 0) and (can_write == False):
                F.write(add_space(space_needed)+O)

def on_click(x,y,button,pressed):
    global keys
    if pressed:
        print('Mouse clicked at ({0},{1}) with {2}'.format(x,y,button))
        mouse_click = str(button)+' '+str(x)+' '+str(y)
        keys.append(mouse_click)

def on_scroll(x,y,dx,dy):
    global keys
    if dy != 0:
        print('Mouse scrolled at ({0},{1}) ({2},{3})'.format(x,y,dx,dy))
        mouse_scroll = 'Mouse.scroll'+' '+str(x)+' '+str(y)+' '+str(dy)
        keys.append(mouse_scroll)


def on_release(key):
    if key == keyboard.Key.esc:
        print('Key Logger file created!')
        listener.stop()
        write_file(keys)
        return False
    

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener: 
    listener.join()
    
with mouse.Listener(on_click=on_click,on_scroll=on_scroll,on_release=on_release) as listener:
    listener.join()

#-------------------- PROCESSING CODE --------------------

import math
from decimal import *

Infant_File = open('5_Preprocessing.txt')
Preprocessed_File = Infant_File.read().split('\n')
Infant_File.close()

def terminate():
    global Processed_File
    Processed_File.close()
    os.remove('5_Processed.txt')
    os.sys.exit(0)


Processing_1 = []
scroll_count = 1
for i in range(1,len(Preprocessed_File)):
    # This first for loop is meant to rid repeating mouse scrolls
    if Preprocessed_File[i-1] == Preprocessed_File[i]: 
        scroll_count += 1
        if i == (len(Preprocessed_File)-1):
            Processing_1.append(Preprocessed_File[i-1]+' '+str(scroll_count))
    else:
        if (Preprocessed_File[i-1].split(' ')[0] == 'Mouse_Scroll') and (scroll_count == 1):
            Processing_1.append(Preprocessed_File[i-1]+' 1')
            scroll_count = 1
            if Preprocessed_File[i].split(' ')[0] != 'Mouse_Scroll':
                Processing_1.append(Preprocessed_File[i])
        elif (Preprocessed_File[i-1].split(' ')[0] == 'Mouse_Scroll') and (scroll_count != 1):
            Processing_1.append(Preprocessed_File[i-1]+' '+str(scroll_count))
            scroll_count = 1
            if Preprocessed_File[i].split(' ')[0] != 'Mouse_Scroll':
                Processing_1.append(Preprocessed_File[i])
        elif (Preprocessed_File[i].split(' ')[0] == 'Mouse_Scroll') and (i == 1):
            scroll_count = 1
        elif Preprocessed_File[i].split(' ')[0] == 'Mouse_Scroll':
            scroll_count = 1
        else:
            Processing_1.append(Preprocessed_File[i])   

if Processing_1.count('Loop_Start') != Processing_1.count('Loop_End'):
    # This checks that there is an equal number of opening and closing commands for for loops
    print('There is an unequal amount of Loop_Start and Loop_End commands. You will need to redo your keylogging correctly.')
    terminate()


if Processing_1.count('Mouse_Drag') % 2 == 1:
    # This checks that there is an even number of Mouse_Drag commands
    print('There is not an even amount of Mouse_Drag commands. You will need to redo your keylogging correctly.')
    terminate()


Drag_Box = []
Box_Count = 0
Drag_Count = 2
if Processing_1.count('Mouse_Drag') != 0:
    for i in range(0,len(Processing_1)):
        # This for loop builds boxes, each box has Mouse_Drag on either end, and in between lines of code
        # This for loop checks that those lines of code in between are appropriate for Mouse_Drag
        split_click = Processing_1[i].split(' ')
        if split_click[0] == 'Mouse_Drag':
            Drag_Count += 1
            if Drag_Count % 2 == 1:
                Drag_Box.append([split_click[0]])
                j = i 
                Box_Building = True
                while Box_Building == True:
                    if j != i:
                        Drag_Box[Box_Count].append(Processing_1[j].split(' ')[0])
                        if (Drag_Box[Box_Count][-1] == 'Mouse_Drag'):
                            Box_Building = False
                        elif (Drag_Box[Box_Count][-1] != 'Left_Click') and (Drag_Box[Box_Count][-1] != 'Right_Click') and (Drag_Box[Box_Count][-1] != 'Middle_Click') and (Drag_Box[Box_Count][-1] != 'Mouse_Scroll'):
                            Box_Building = False
                            print('All code within Mouse_Drag must be mouse clicks or scrolls. You need to redo your keylogging correctly.')
                            terminate()
                    j += 1
                Box_Count += 1
    for m in range(0,len(Drag_Box)):
        # This for loop checks that there are at least two mouse clicks or scrolls in between Mouse_Drag commands
        if len(Drag_Box[m]) <= 3:
            print('There must be at least two commands between Mouse_Drag. You need to redo your keylogging correctly.')
            terminate()
                    
Processing_2 = []
Pos_1 = []
for i in range(0,len(Processing_1)):
    # This next for loop is meant to calculate travel times between left, right, middle mouse clicks and mouse scrolls
    split_click = Processing_1[i].split(' ')
    if i == 0:
        if (split_click[0] == 'Left_Click') or (split_click[0] == 'Right_Click') or (split_click[0] == 'Middle_Click') or (split_click[0] == 'Mouse_Scroll'):
            Processing_2.append(Processing_1[i]+ ' '+str(1))
            Pos_1 = [int(split_click[1]),int(split_click[2])]
        else:
            Processing_2.append(Processing_1[i])
    elif (split_click[0] == 'Left_Click') or (split_click[0] == 'Right_Click') or (split_click[0] == 'Middle_Click') or (split_click[0] == 'Mouse_Scroll'):
        if bool(Pos_1) == False:
            Pos_1 = [int(split_click[1]),int(split_click[2])]
            Processing_2.append(Processing_1[i])
        else:
            Pos_2 = [int(split_click[1]),int(split_click[2])]
            distance = math.sqrt(((Pos_2[0]-Pos_1[0])**2)+((Pos_2[1]-Pos_1[1])**2))
            move_time = Decimal(distance/1000).quantize(Decimal('.01'),rounding = ROUND_DOWN)
            Processing_2.append(Processing_1[i]+' '+str(move_time))          
    else:
        Processing_2.append(Processing_1[i])


for i in range(0,len(Processing_2)):
    Processed_File.write(str(Processing_2[i])+'\n')
Processed_File.close()

# -------------------- PYTHON CODE CREATION --------------------

Create_File = open('9_Script_Creation.txt','a')

Create_File.write('''import os
import time
import pyautogui
pyautogui.FAILSAFE = True

''')

space_count = 0
space = ''

def space_add(space_count):
    global space
    if space_count == 0:
        space = ''
    elif space_count == 1:
        space = '    '
    elif space_count == 2:
        space = '        '
    elif space_count == 3:
        space = '            '
    elif space_count == 4:
        space = '                '
    elif space_count == 5:
        space = '                    '
    elif space_count == 6:
        space = '                        '

def right_click(mouse):
    global space, space_count
    space_add(space_count)
    Create_File.write('\n'+space +'pyautogui.moveTo('+str(int(mouse[1]))+','+str(int(mouse[2]))+','+str(float(mouse[3]))+')')
    Create_File.write('\n'+space +'''pyautogui.click(button='right')''')
    
def left_click(mouse):
    global space, space_count
    space_add(space_count)
    Create_File.write('\n'+space +'pyautogui.moveTo('+str(int(mouse[1]))+','+str(int(mouse[2]))+','+str(float(mouse[3]))+')')
    Create_File.write('\n'+space +'''pyautogui.click(button='left')''')

def middle_click(mouse):
    global space, space_count
    space_add(space_count)
    Create_File.write('\n'+space +'pyautogui.moveTo('+str(int(mouse[1]))+','+str(int(mouse[2]))+','+str(float(mouse[3]))+')')
    Create_File.write('\n'+space +'''pyautogui.click(button='middle')''')

def right_button():
    global space, space_count
    space_add(space_count)
    Create_File.write('\n'+space +'''pyautogui.press('right')''')

def left_button():
    global space, space_count
    space_add(space_count)
    Create_File.write('\n'+space +'''pyautogui.press('left')''')

def up_button():
    global space, space_count
    space_add(space_count)
    Create_File.write('\n'+space +'''pyautogui.press('up')''')

def down_button():
    global space, space_count
    space_add(space_count)
    Create_File.write('\n'+space +'''pyautogui.press('down')''')

def enter_button():
    global space, space_count
    space_add(space_count)
    Create_File.write('\n'+space +'''pyautogui.press('enter')''')

def mouse_scroll(mouse):
    global space, space_count
    space_add(space_count)
    Create_File.write('\n'+space +'pyautogui.moveTo('+str(int(mouse[1]))+','+str(int(mouse[2]))+','+str(float(mouse[5]))+')')
    Create_File.write('\n'+space +'pyautogui.scroll('+str((int(mouse[3])*int(mouse[4])))+')')

def wait_time(Time):
    global space, space_count
    space_add(space_count)
    Create_File.write('\n'+space +'time.sleep('+str(float(Time))+')')

def mouse_drag(box):
    global space, space_count
    space_add(space_count)
    for m in range(0,len(box)):
        if m == 0:
            Create_File.write('\n'+space +'pyautogui.moveTo('+str(int(box[m][0]))+','+str(int(box[m][1]))+','+str(float(3))+')')
        else:
            Create_File.write('\n'+space +'pyautogui.dragTo('+str(int(box[m][0]))+','+str(int(box[m][1]))+','+str(float(box[m][2]))+')')

def keyboard(text):
    global space, space_count
    space_add(space_count)
    Create_File.write('\n'+space +'pyautogui.write('+"'"+str(text)+"'"+',interval=.05)')

def for_loop_3(box,start,finish,runs):
    i = 0

def for_loop_2(box,start,finish,runs):
    global space, space_count
    Create_File.write('\n'+space +'for j in range(0,'+str(int(runs))+'):')
    end_count = finish - start 
    for run in range(0,1):
        drag_skip = False
        loop_skip = False
        for i in range(0,end_count):
            space_count = 2
            space_add(space_count)
            keys = box[i]
            start_loop_count = 0
            end_loop_count = 0
            if (drag_skip == True) or (loop_skip == True):
                if (i >= j) and (i <= end):
                    if i == end:
                        drag_skip = False
                        loop_skip = False
                    continue
            elif box[i][0] == 'Right_Click':
                right_click(box[i])
            elif box[i][0] == 'Left_Click':
                left_click(box[i])
            elif box[i][0] == 'Middle_Click':
                middle_click(box[i])
            elif box[i][0] == 'Right_Button':
                right_button(box[i])
            elif box[i][0] == 'Left_Button':
                left_button(box[i])
            elif box[i][0] == 'Up_Button':
                up_button(box[i])
            elif box[i][0] == 'Down_Button':
                down_button(box[i])
            elif box[i][0] == 'Enter':
                enter_button()
            elif box[i][0] == 'Mouse_Scroll':
                mouse_scroll(box[i])
            elif box[i][0] == 'Mouse_Drag':
                j = i + 1
                Drag_Check = True
                drag_box = []
                while Drag_Check == True:
                    for k in range(j,len(box)):
                        if (box[k][0] == 'Right_Click') or (box[k][0] == 'Left_Click') or (box[k][0] == 'Middle_Click'):
                            drag_box.append(box[k][1:4])
                        elif box[k][0] == 'Mouse_Scroll':
                            drag_box.append(box[k][1:3]+[box[k][4]])
                        elif box[k][0] == 'Mouse_Drag':
                            end = k
                            drag_skip = True
                            mouse_drag(drag_box)
                            Drag_Check = False
                            break
                continue
            elif box[i][0] == 'Loop_Start':
                start_loop_count += 1
                start = i + 1
                j = start
                runs = box[i][1]
                while start_loop_count != end_loop_count:
                    loop_box = []
                    for n in range(start,len(box)):
                        if box[n][0] == 'Loop_Start':
                            start_loop_count += 1
                            loop_box.append(box[n])
                        elif box[n][0] == 'Loop_End':
                            end_loop_count += 1
                            if start_loop_count != end_loop_count:
                                loop_box.append(box[n])
                            if start_loop_count == end_loop_count:
                                end = n
                                loop_skip = True
                                for_loop_3(loop_box,start,end,runs)
                        else:
                            loop_box.append(box[n])
                start_loop_count = 0
                end_loop_count = 0
                continue
            elif box[i][0] == 'Wait_Time':
                wait_time(box[i][1])
            else:
                keyboard(' '.join(box[i]))

def for_loop_1(box,start,finish,runs):
    global space, space_count
    Create_File.write('\n'+space +'for i in range(0,'+str(int(runs))+'):')
    end_count = finish - start 
    for run in range(0,1):
        drag_skip = False
        loop_skip = False
        for i in range(0,end_count):
            space_count = 1
            space_add(space_count)
            keys = box[i]
            start_loop_count = 0
            end_loop_count = 0
            if (drag_skip == True) or (loop_skip == True):
                if (i >= j) and (i <= end):
                    if i == end:
                        drag_skip = False
                        loop_skip = False
                    continue
            elif box[i][0] == 'Right_Click':
                right_click(box[i])
            elif box[i][0] == 'Left_Click':
                left_click(box[i])
            elif box[i][0] == 'Middle_Click':
                middle_click(box[i])
            elif box[i][0] == 'Right_Button':
                right_button(box[i])
            elif box[i][0] == 'Left_Button':
                left_button(box[i])
            elif box[i][0] == 'Up_Button':
                up_button(box[i])
            elif box[i][0] == 'Down_Button':
                down_button(box[i])
            elif box[i][0] == 'Enter':
                enter_button()
            elif box[i][0] == 'Mouse_Scroll':
                mouse_scroll(box[i])
            elif box[i][0] == 'Mouse_Drag':
                j = i + 1
                Drag_Check = True
                drag_box = []
                while Drag_Check == True:
                    for k in range(j,len(box)):
                        if (box[k][0] == 'Right_Click') or (box[k][0] == 'Left_Click') or (box[k][0] == 'Middle_Click'):
                            drag_box.append(box[k][1:4])
                        elif box[k][0] == 'Mouse_Scroll':
                            drag_box.append(box[k][1:3]+[box[k][4]])
                        elif box[k][0] == 'Mouse_Drag':
                            end = k
                            drag_skip = True
                            mouse_drag(drag_box)
                            Drag_Check = False
                            break
                continue
            elif box[i][0] == 'Loop_Start':
                start_loop_count += 1
                start = i + 1
                j = start
                runs = box[i][1]
                while start_loop_count != end_loop_count:
                    loop_box = []
                    for n in range(start,len(box)):
                        if box[n][0] == 'Loop_Start':
                            start_loop_count += 1
                            loop_box.append(box[n])
                        elif box[n][0] == 'Loop_End':
                            end_loop_count += 1
                            if start_loop_count != end_loop_count:
                                loop_box.append(box[n])
                            if start_loop_count == end_loop_count:
                                end = n
                                loop_skip = True
                                for_loop_2(loop_box,start,end,runs)
                        else:
                            loop_box.append(box[n])
                start_loop_count = 0
                end_loop_count = 0
                continue
            elif box[i][0] == 'Wait_Time':
                wait_time(box[i][1])
            else:
                keyboard(' '.join(box[i]))


File = open('6_Proving_Ground.txt').read().split('\n')

drag_skip = False
loop_skip = False
for i in range(0,len(File)):
    space_count = 0
    start_loop_count = 0
    end_loop_count = 0
    keys = File[i]
    split = File[i].split(' ')
    if (drag_skip == True) or (loop_skip == True):
        if (i >= j) and (i <= end):
            if i == end:
                drag_skip = False
                loop_skip = False
            continue
    elif split[0] == 'Right_Click':
        right_click(split)
    elif split[0] == 'Left_Click':
        left_click(split)
    elif split[0] == 'Middle_Click':
        middle_click(split)
    elif split[0] == 'Right_Button':
        right_button()
    elif split[0] == 'Left_Button':
        left_button()
    elif split[0] == 'Up_Button':
        up_button()
    elif split[0] == 'Down_Button':
        down_button()
    elif split[0] == 'Enter':
        enter_button()
    elif split[0] == 'Mouse_Scroll':
        mouse_scroll(split)
    elif split[0] == 'Mouse_Drag':
        j = i + 1
        Drag_Check = True
        drag_box = []
        while Drag_Check == True:
            for k in range(j,len(File)):
                split_d = File[k].split(' ')
                if (split_d[0] == 'Right_Click') or (split_d[0] == 'Left_Click') or (split_d[0] == 'Middle_Click'):
                    drag_box.append(split_d[1:4])
                elif split_d[0] == 'Mouse_Scroll':
                    drag_box.append(split_d[1:3]+[split_d[5]])
                elif split_d[0] == 'Mouse_Drag':
                    end = k  
                    drag_skip = True
                    mouse_drag(drag_box)
                    Drag_Check = False
                    break
        continue
    elif split[0] == 'Loop_Start':
        start_loop_count += 1
        start = i + 1
        j = start
        runs = split[1]
        while start_loop_count != end_loop_count:
            loop_box = []
            for n in range(start,len(File)):
                split_f = File[n].split(' ')
                if split_f[0] == 'Loop_Start':
                    start_loop_count += 1
                    loop_box.append(split_f)
                elif split_f[0] == 'Loop_End':
                    end_loop_count += 1
                    if start_loop_count != end_loop_count:
                        loop_box.append(split_f)
                    if start_loop_count == end_loop_count:
                        end = n
                        loop_skip = True
                        for_loop_1(loop_box,start,end,runs)
                else:
                    loop_box.append(split_f)
        start_loop_count = 0
        end_loop_count = 0
        continue
    elif split[0] == 'Wait_Time':
        wait_time(split[1])
    else:
        keyboard(keys)


Create_File.close()

