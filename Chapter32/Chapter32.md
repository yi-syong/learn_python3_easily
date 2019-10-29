# Chapter 32

### 32.1
`4`
### 32.2
`3`
### 32.3
`2`
### 32.4
`3`
### 32.5
`2`
### 32.6
`1`
### 32.7
`2`
### 32.8
`3`
### 32.9
`1`
### 32.10
`4`
### 32.11

有參考前面的程式碼~ 拼湊而成

```python=
import tkinter as tk
import tkinter.font as tkfont

def but_click():
    result = name.get() + ', '
    selected_sex = sex.get()
    result += SEX_OPTIONS[selected_sex][0] + ', '
    result += str(year.get()) + '/' + str(month.get()) + '/' + str(day.get()) + ', '

    if basketball.get():
        result += '籃球'
    if swimming.get():
        result += '游泳'
    if music.get():
        result += '音樂'
    if ridding_bike.get():
        result += '騎單車'
    if reading.get():
        result += '閱讀'
        
    label_result.config(text=result)
    
tk_win = tk.Tk()
tk_win.title('輸入個人資料')
tk_win.geometry('450x700')

default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(size=15)

frame_name = tk.Frame()
frame_name.pack(padx=10, pady=(10, 5), anchor=tk.NW)

lab_name = tk.Label(frame_name, text = '姓名:')
lab_name.pack(side=tk.LEFT)

name = tk.StringVar()
ent_name = tk.Entry(frame_name, textvariable=name, width=20, font=default_font)
ent_name.pack(side=tk.LEFT)

frame_sex = tk.Frame()
frame_sex.pack(padx=10, pady=(10, 5), anchor=tk.NW)

lab_sex = tk.Label(frame_sex, text = '性別:')
lab_sex.pack(side=tk.LEFT)

SEX_OPTIONS = (('男', 0),('女', 1))

sex = tk.IntVar()
sex.set(0)

for item, value in SEX_OPTIONS:
    radbut = tk.Radiobutton(frame_sex, text=item, variable=sex, 
                            value=value, font=default_font)
    radbut.pack()

frame_birth = tk.Frame()
frame_birth.pack(padx=10, pady=(10, 5), anchor=tk.NW)

lab_birth = tk.Label(frame_birth, text = '生日(年月日):')
lab_birth.pack(side=tk.LEFT)

year = tk.IntVar()
month = tk.IntVar()
day = tk.IntVar()
year.set(1)
month.set(1)
day.set(1)

spinbox_year = tk.Spinbox(frame_birth, from_=1, to=2019,
                          textvariable=year, font=default_font, width=5)
spinbox_month = tk.Spinbox(frame_birth, from_=1, to=12, 
                           textvariable=month, font=default_font, width=5)
spinbox_day = tk.Spinbox(frame_birth, from_=1, to=31, 
                         textvariable=day, font=default_font, width=5)

spinbox_year.pack(side=tk.LEFT, padx=10, pady=10)
spinbox_month.pack(side=tk.LEFT, padx=10, pady=10)
spinbox_day.pack(side=tk.LEFT, padx=10, pady=10)

frame_hobbies = tk.Frame()
frame_hobbies.pack(padx=10, pady=(10, 5), anchor=tk.W)

lab_hobbies = tk.Label(frame_hobbies, text = '興趣:')
lab_hobbies.pack(side=tk.LEFT)

basketball = tk.IntVar()
chkbut_basketball = tk.Checkbutton(frame_hobbies, text='籃球', 
                                   variable=basketball, anchor=tk.W)
chkbut_basketball.pack(padx=10, pady=5, fill=tk.X)

swimming = tk.IntVar()
chkbut_swimming = tk.Checkbutton(frame_hobbies, text='游泳', 
                                 variable=swimming, anchor=tk.W)
chkbut_swimming.pack(padx=10, pady=5, fill=tk.X)

music = tk.IntVar()
chkbut_music = tk.Checkbutton(frame_hobbies, text='音樂', 
                              variable=music, anchor=tk.W)
chkbut_music.pack(padx=10, pady=5, fill=tk.X)

ridding_bike = tk.IntVar()
chkbut_ridding_bike = tk.Checkbutton(frame_hobbies, text='騎單車', 
                                     variable=ridding_bike, anchor=tk.W)
chkbut_ridding_bike.pack(padx=10, pady=5, fill=tk.X)

reading = tk.IntVar()
chkbut_reading = tk.Checkbutton(frame_hobbies, text='閱讀', 
                                variable=reading, anchor=tk.W)
chkbut_reading.pack(padx=10, pady=5, fill=tk.X)

but = tk.Button(tk_win, text='確定', command=but_click)
but.config(font=default_font, fg='blue', bg='sky blue', padx=15)
but.pack(padx=10, pady=5)

label_result = tk.Label(tk_win, font=default_font, fg='orange red')
label_result.pack(padx=10, pady=(5, 10))

tk_win.mainloop()
```