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

class selector:
    def __init__(self, r, l, t, vals, func):
        self.tkvarq = StringVar(root)
        self.tkvarq.set(vals[0])
        self.l = Label(root, text = l)
        self.l.grid(row=r, column=0)
        self.sel = OptionMenu(root, self.tkvarq, *vals)
        self.sel.grid(row=r, column=1)
        self.button = Button(root, text=t, command=func)
        self.button.grid(row=r, column=2)

# beds
def write_bed_type(fi, t, p, pn):
    with open(os.path.join(bed_model_path, fi), 'w') as f:
        f.write('{"parent":"block/bed_'+pn+'","textures":{"top":"blocks/beds/'+t+'/bed_'+p+'_top","end":"blocks/beds/'+t+'/bed_'+p+'_end","left":"blocks/beds/'+t+'/bed_'+p+'_left","right":"blocks/beds/'+t+'/bed_'+p+'_right"}}')
def set_bed_type():
    print("setting bed type to " + bed.tkvarq.get())
    write_bed_type('bed_foot.json', bed.tkvarq.get(), 'feet', 'foot')
    write_bed_type('bed_head.json', bed.tkvarq.get(), 'head', 'head')

# wool
wool_types = ['texture pack default', 'outlined']
def set_wool_type():
    print("setting wool type to " + wool.tkvarq.get())
    wool_colors = ['black', 'blue', 'brown', 'cyan', 'gray', 'green', 'light_blue', 'lime', 'magenta', 'orange', 'pink', 'purple', 'red', 'silver', 'white', 'yellow']
    for i in wool_colors:
        with open(os.path.join(block_model_path, i + '_wool.json'), 'w') as f:
            f.write('{"parent":"block/cube_all","textures":{"all":"blocks/' + ('Outlined Wool/' if wool.tkvarq.get() != wool_types[0] else '') + 'wool_colored_' + i + '"}}')

# -- initializing classes --

bed = selector(0, 'bed type', 'set bed type', bed_types, set_bed_type)
wool = selector(1, 'wool type', 'set wool type', wool_types, set_wool_type)
# quit button
Button(root, text='quit', command=root.destroy).grid(row=2, columnspan=3)

root.mainloop()
