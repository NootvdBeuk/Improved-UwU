import os, sys
from tkinter import *

# -- os path stuff --

if os.path.dirname(os.path.realpath(__file__)) != sys.path[0]:
    print("Could not find script path, exiting")
    sys.exit()

mc_path = os.path.join(os.path.dirname(sys.path[0]), 'assets', 'minecraft')
bed_model_path = os.path.join(mc_path, 'models', 'block', 'bed')
bed_texture_path = os.path.join(mc_path, 'textures', 'blocks', 'beds')
bed_types = sorted([f for f in os.listdir(bed_texture_path) if os.path.isdir(os.path.join(bed_texture_path, f))])

# -- tkinter stuff --

# init
root = Tk()
root.title("UnU")
root.configure(bg='#ffffff')

# beds
tkvarq = StringVar(root)
tkvarq.set(bed_types[0])
bed_type = OptionMenu(root, tkvarq, *bed_types)
bed_type.grid(row=0)

def write_bed_type(fi, t, p, pn):
    with open(os.path.join(bed_model_path, fi), 'w') as f:
        f.write('{"parent":"block/bed_'+pn+'","textures":{"top":"blocks/beds/'+t+'/bed_'+p+'_top","end":"blocks/beds/'+t+'/bed_'+p+'_end","left":"blocks/beds/'+t+'/bed_'+p+'_left","right":"blocks/beds/'+t+'/bed_'+p+'_right"}}')

def set_bed_type():
    print("setting bed type to " + tkvarq.get())
    write_bed_type('bed_foot.json', tkvarq.get(), 'feet', 'foot')
    write_bed_type('bed_head.json', tkvarq.get(), 'head', 'head')

set_bed_type_button = Button(root, text='set bed type', command=set_bed_type)
set_bed_type_button.grid(row=0, column=1)

# quit button
Button(root, text='quit', command=root.destroy).grid(row=1, columnspan=2)

root.mainloop()
