import os, sys
from tkinter import *

# -- os path stuff --

if os.path.dirname(os.path.realpath(__file__)) != sys.path[0]:
    print("Could not find script path, exiting")
    sys.exit()

mc_path = os.path.join(os.path.dirname(sys.path[0]), 'assets', 'minecraft')
block_model_path = os.path.join(mc_path, 'models', 'block')
bed_model_path = os.path.join(block_model_path, 'bed')
bed_texture_path = os.path.join(mc_path, 'textures', 'blocks', 'beds')
bed_types = sorted([f for f in os.listdir(bed_texture_path) if os.path.isdir(os.path.join(bed_texture_path, f))])

# -- tkinter stuff --

# init
root = Tk()
root.title("UnU")
root.configure(bg='#ffffff')

# beds
tkvarq_bed = StringVar(root)
tkvarq_bed.set(bed_types[0])
bed_type = OptionMenu(root, tkvarq_bed, *bed_types)
bed_type.grid(row=0)
def write_bed_type(fi, t, p, pn):
    with open(os.path.join(bed_model_path, fi), 'w') as f:
        f.write('{"parent":"block/bed_'+pn+'","textures":{"top":"blocks/beds/'+t+'/bed_'+p+'_top","end":"blocks/beds/'+t+'/bed_'+p+'_end","left":"blocks/beds/'+t+'/bed_'+p+'_left","right":"blocks/beds/'+t+'/bed_'+p+'_right"}}')
def set_bed_type():
    print("setting bed type to " + tkvarq_bed.get())
    write_bed_type('bed_foot.json', tkvarq_bed.get(), 'feet', 'foot')
    write_bed_type('bed_head.json', tkvarq_bed.get(), 'head', 'head')
set_bed_type_button = Button(root, text='set bed type', command=set_bed_type)
set_bed_type_button.grid(row=0, column=1)

# wool
wool_colors = ['black', 'blue', 'brown', 'cyan', 'gray', 'green', 'light_blue', 'lime', 'magenta', 'orange', 'pink', 'purple', 'red', 'silver', 'white', 'yellow']
wool_types = ['texture pack default', 'outlined']
tkvarq_wool = StringVar(root)
tkvarq_wool.set(wool_types[0])
wool_type = OptionMenu(root, tkvarq_wool, *wool_types)
wool_type.grid(row=1)
def set_wool_color(c, d):
    with open(os.path.join(block_model_path, c+'_wool.json'), 'w') as f:
        f.write('{"parent":"block/cube_all","textures":{"all":"blocks/' + ('Outlined Wool/' if not d else '') + 'wool_colored_' + c + '"}}')
def set_wool_type():
    print("setting wool type to " + tkvarq_wool.get())
    for i in wool_colors:
        set_wool_color(i, tkvarq_wool.get() == wool_types[0])
set_wool_type_button = Button(root, text='set wool type', command=set_wool_type)
set_wool_type_button.grid(row=1, column=1)

# quit button
Button(root, text='quit', command=root.destroy).grid(row=2, columnspan=2)

root.mainloop()
