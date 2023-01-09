import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,font,colorchooser,filedialog
import os

win=tk.Tk()
win.geometry('1100x800')
win.title('Text Editor')
win.wm_iconbitmap('icon.ico')
#................................main menu..............................
main_menu=tk.Menu(win)
### file menu
file=tk.Menu(main_menu,tearoff=0)
new_icon=tk.PhotoImage(file='icons2/new.png')
open_icon=tk.PhotoImage(file='icons2/open.png')
save_icon=tk.PhotoImage(file='icons2/save.png')
save_as_icon=tk.PhotoImage(file='icons2/save_as.png')
exit_icon=tk.PhotoImage(file='icons2/exit.png')

### edit menu
edit=tk.Menu(main_menu,tearoff=0)
copy_icon=tk.PhotoImage(file='icons2/copy.png')
cut_icon=tk.PhotoImage(file='icons2/cut.png')
paste_icon=tk.PhotoImage(file='icons2/paste.png')
clear_all_icon=tk.PhotoImage(file='icons2/clear_all.png')
find_icon=tk.PhotoImage(file='icons2/find.png')
 
### view menu
view=tk.Menu(main_menu,tearoff=0)

toolbar_icon=tk.PhotoImage(file='icons2/tool_bar.png')
statusbar_icon=tk.PhotoImage(file='icons2/status_bar.png')
### color menu
color_theme=tk.Menu(main_menu,tearoff=0)
light_default_icon=tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon=tk.PhotoImage(file='icons2/light_plus.png')
dark_icon=tk.PhotoImage(file='icons2/dark.png')
red_icon=tk.PhotoImage(file='icons2/red.png')
monokai_icon=tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon=tk.PhotoImage(file='icons2/night_blue.png')
  
color_tuple=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
color_dict={
'Light Default':('#000000','#ffffff'),
'Light Plus':('#474747','#e0e0e0'),
'Dark':('#c4c4c4','#2d2d2d'),
'Red':('#2d2d2d','#ffe8e8'),
'Monokai':('#d3b774','#474747'),
'Night_Blue':('#ededed','#6b9dc2')
}
## about menu
def about_func():
  about_dialouge=tk.Toplevel()
  about_dialouge.geometry('450x250+550+100')
  about_dialouge.title('About the software')
  about_dialouge.resizable(0,0)
  scroll_bar=tk.Scrollbar(about_dialouge)
  scroll_bar.pack(side=tk.RIGHT,view=tk.Y)

  about_dialouge.mainloop()

main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Themes',menu=color_theme)
main_menu.add_cascade(label='About',command=about_func)
#..............................end main menu..............................

#..............................Tool bar....................................
tool_bar=ttk.Label(win)
tool_bar.pack(side=tk.TOP,fill=tk.X)
### font box
font_var=tk.StringVar()
font_tuple=tk.font.families()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_var,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=4)
### font size box
font_size_var=tk.IntVar()
font_size_box=ttk.Combobox(tool_bar,width=10,textvariable=font_size_var,state='readonly')
font_size_box['values']=tuple(range(2,102,2))
font_size_box.current(5)
font_size_box.grid(row=0,column=1,padx=4)
### buttons
  ## bold button
bold_icon=tk.PhotoImage(file='icons2/bold.png')
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=4)

  ## italic button 
italic_icon=tk.PhotoImage(file='icons2/italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=4)

  ## underline button
underline_icon=tk.PhotoImage(file='icons2/underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=4)

 ## font color button
font_color_icon=tk.PhotoImage(file='icons2/font_color.png')
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=4)

 ##align left button
align_left_icon=tk.PhotoImage(file='icons2/align_left.png')
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=4)

 ## align center button
align_center_icon=tk.PhotoImage(file='icons2/align_center.png')
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=4)

 ## align right button
align_right_icon=tk.PhotoImage(file='icons2/align_right.png')
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=4)

#.............................END tool bar................................................

#..................................text editor...........................................
text_editor=tk.Text(win)
text_editor.config(relief=tk.FLAT)
text_editor.focus_set()
scroll_bar=tk.Scrollbar(win)
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)
## variables
current_font_family='Arial'
current_font_size=12
### font choose and font size funtionality
def change_font(event=None):
  global current_font_family
  current_font_family=font_var.get()
  text_editor.config(font=(current_font_family,current_font_size))

def change_font_size(event=None):
  global current_font_size
  current_font_size=font_size_var.get()
  text_editor.config(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size_box.bind("<<ComboboxSelected>>",change_font_size)

### bold button functionality
def make_bold():
  text_property=tk.font.Font(font=text_editor['font'])
  if text_property.actual()['weight']=='normal':
    text_editor.config(font=(current_font_family,current_font_size,'bold'))
  elif text_property.actual()['weight']=='bold':
    text_editor.config(font=(current_font_family,current_font_size,'normal'))

bold_btn.config(command=make_bold)
## italic button functionality
def make_italic():
  text_property=tk.font.Font(font=text_editor['font'])
  if text_property.actual()['slant']=='roman':
    text_editor.config(font=(current_font_family,current_font_size,'italic'))
  elif text_property.actual()['slant']=='italic':
    text_editor.config(font=(current_font_family,current_font_size,'roman'))

italic_btn.config(command=make_italic)
## underline button functionality
def make_underline():
  text_property=tk.font.Font(font=text_editor['font'])
  if text_property.actual()['underline']==0:
    text_editor.config(font=(current_font_family,current_font_size,'underline'))
  elif text_property.actual()['underline']==1:
    text_editor.config(font=(current_font_family,current_font_size,'normal'))

underline_btn.config(command=make_underline)
## font color functionslity
def change_font_color():
  color_var=tk.colorchooser.askcolor()
  text_editor.config(fg=color_var[1])

font_color_btn.config(command=change_font_color)

## align left button functionality
def align_left():
  content=text_editor.get(1.0,tk.END)
  text_editor.tag_config('left',justify=tk.LEFT)
  text_editor.delete(1.0,tk.END)
  text_editor.insert(tk.INSERT,content,'left')

align_left_btn.config(command=align_left)

## align center button functionality
def align_center():
  content=text_editor.get(1.0,tk.END)
  text_editor.tag_config('center',justify=tk.CENTER)
  text_editor.delete(1.0,tk.END)
  text_editor.insert(tk.INSERT,content,'center')

align_center_btn.config(command=align_center)

## align right button functionality
def align_right():
  content=text_editor.get(1.0,tk.END)
  text_editor.tag_config('right',justify=tk.RIGHT)
  text_editor.delete(1.0,tk.END)
  text_editor.insert(tk.INSERT,content,'right')

align_right_btn.config(command=align_right)

text_editor.config(font=('Arial',12))
#....................................END text editor....................................

#....................................status bar...................................
status_bar=ttk.Label(win,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)
text_changed=False
def changed(event=None):
  global text_changed
  if text_editor.edit_modified():
    text_changed=True
    words=len(text_editor.get(1.0,'end-1c').split())
    characters=len(text_editor.get(1.0,'end-1c'))
    status_bar.config(text=f'Words : {words} Characters : {characters}')
  text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',changed)  
#.....................................END status bar..................................

#....................................main menu functionality........................

url=''         # variable
### file menu fuctionality
def new_func(event=None):
  global url
  url=''
  text_editor.delete(1.0,tk.END) 

file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_func)

def open_func(event=None):
  global url
  url=filedialog.askopenfilename(initialdir=os.getcwd(),filetypes=(('Text files','*.txt'),('All files','*.*')),title='Select file')
  try:
    with open (url,'r') as f:
      text_editor.delete(1.0,tk.END)
      text_editor.insert(1.0,f.read())
  except FileNotFoundError:
    return
  except:
    return
  name=os.path.basename(url)
  win.title(f'{name}-Text Editor')

file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_func)

def save_func(event=None):
  global url,text_changed
  if text_changed:
    try:
      if url:
        content=text_editor.get(1.0,tk.END)
        with open (url,'w',encoding='utf-8') as f:
          f.write(content)
      else:
          url=filedialog.asksaveasfile(mode='w',filetypes=(('Text files','*.txt'),('All files','*.*')),defaultextension='.txt')
          content2=text_editor.get(1.0,tk.END)
          url.write(content2)                                                      
          url.close()   
    except:
      return    
    
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_func)

def save_as_func(event=None):
  global url
  try:
    url=filedialog.asksaveasfile(mode='w',filetypes=(('Text files','*.txt'),('All files','*.*')),defaultextension='.txt')
    content2=text_editor.get(1.0,tk.END)
    url.write(content2)
    url.close()   
  except:
    return  

file.add_command(label='Save as',image=save_as_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+S',command=save_as_func)

def exit_func(event=None):
  global url,text_changed
  try:
    if text_changed:
      mbox=messagebox.askyesnocancel('Warning','Do you want to save file ?')
      if mbox is True :
        if url:
          content=text_editor.get(1.0,tk.END)
          with open (url,'w',encoding='utf-8') as f:
            f.write(content)
            win.destroy()    
        else:
            url=filedialog.asksaveasfile(mode='w',filetypes=(('Text files','*.txt'),('All files','*.*')),defaultextension='.txt')
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()  
            win.destroy()
      elif mbox is False:
        win.destroy()
    else :
        win.destroy()
  except:
    return
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exit_func)

### edit menu functionality
def find_func(event=None):
  def find():
    word=find_entry.get()
    text_editor.tag_remove('match','1.0',tk.END)
    matches=0
    if word:
      start_pos='1.0'
      while True:
        start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
        if not start_pos:
          break
        end_pos=f'{start_pos}+{len(word)}c'
        print(end_pos)
        text_editor.tag_add('match',start_pos,end_pos)
        start_pos=end_pos
        matches+=1
        text_editor.tag_config('match',foreground='red',background='yellow')
  def replace():
    find_word=find_entry.get()
    replace_word=replace_entry.get()
    content=text_editor.get(1.0,tk.END)
    new_content=content.replace(find_word,replace_word)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(1.0,new_content)

  find_dialouge=tk.Toplevel()
  find_dialouge.title('Find')
  find_dialouge.resizable(0,0)
  find_dialouge.geometry('450x250+500+200')

  ## frame
  find_frame=ttk.LabelFrame(find_dialouge,text='Find/Replace')
  find_frame.pack(pady=20)
  ## labels
  find_label=ttk.Label(find_frame,text='Find : ')
  find_label.grid(row=0,column=0,pady=4,padx=4)
  replace_label=ttk.Label(find_frame,text='Replace : ')
  replace_label.grid(row=1,column=0,pady=4,padx=4)
  ##entry
  find_entry=ttk.Entry(find_frame,width=30)
  find_entry.grid(row=0,column=1,pady=4,padx=4)
  replace_entry=ttk.Entry(find_frame,width=30)
  replace_entry.grid(row=1,column=1,pady=4,padx=4)
  ##buttons
  find_btn=ttk.Button(find_frame,text='Find',command=find)
  find_btn.grid(row=2,column=0,padx=8,pady=4)
  replace_btn=ttk.Button(find_frame,text='Replace',command=replace)
  replace_btn.grid(row=2,column=1,padx=8,pady=4)

  find_dialouge.mainloop()

def clear_all_func(event=None):
  text_editor.delete(1.0,tk.END)

edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda:text_editor.event_generate('<Control c>'))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate('<Control x>'))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate('<Control v>'))
edit.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+X',command=clear_all_func)
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_func)

### view menu functionality
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbar():
  global show_toolbar
  if show_toolbar:
    tool_bar.pack_forget()
    show_toolbar=False
  else:
    text_editor.pack_forget()
    status_bar.pack_forget()
    tool_bar.pack(side=tk.TOP,fill=tk.X)
    text_editor.pack(expand=True,fill=tk.BOTH)
    # status_bar.pack(side=tk.BOTTOM)
    show_toolbar=True

def hide_statusbar():
  global show_statusbar
  if show_statusbar:
    status_bar.pack_forget()
    show_statusbar=False
  else:
    status_bar.pack(side=tk.BOTTOM)
    show_statusbar=True

view.add_checkbutton(label='Tool Bar',image=toolbar_icon,compound=tk.LEFT,variable=show_toolbar,command=hide_toolbar)  
view.add_checkbutton(label='Status Bar',image=statusbar_icon,compound=tk.LEFT,variable=show_statusbar,command=hide_statusbar)

### themes menu functionality

def change_theme():
  choosen_theme=theme_choice.get()
  color_tuple=color_dict.get(choosen_theme)
  fg_color,bg_color=color_tuple[0],color_tuple[1]
  text_editor.config(fg=fg_color,background=bg_color)

theme_choice=tk.StringVar()
count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_tuple[count],compound=tk.LEFT,variable=theme_choice,command=change_theme) 
    count+=1

#....................................END main menu functionality..................
win.config(menu=main_menu)
# bind shortcut keys
win.bind('<Control-n>',new_func)
win.bind('<Control-o>',open_func)
win.bind('<Control-s>',save_func)
win.bind('<Control-Alt-s>',save_as_func)
win.bind('<Control-q>',exit_func)
win.bind('<Control-f>',find_func)
win.bind('<Control-Alt-x>',clear_all_func)

win.mainloop()