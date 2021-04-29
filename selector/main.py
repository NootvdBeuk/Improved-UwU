import os, sys
from tkinter import *

# -- os path stuff --

if os.path.dirname(os.path.realpath(__file__)) != sys.path[0]:
    print("Could not find script path, exiting")
    sys.exit()

def ensure_path(p):
    if not os.path.exists(p):
        os.mkdir(p)

mc_path = os.path.join(os.path.dirname(sys.path[0]), 'assets', 'minecraft')
model_path = os.path.join(mc_path, 'models')
block_model_path = os.path.join(model_path, 'block')
item_model_path = os.path.join(model_path, 'item')
bed_model_path = os.path.join(block_model_path, 'bed')
bed_texture_path = os.path.join(mc_path, 'textures', 'blocks', 'beds')
bed_types = sorted([f for f in os.listdir(bed_texture_path) if os.path.isdir(os.path.join(bed_texture_path, f))])

ensure_path(model_path)
ensure_path(block_model_path)
ensure_path(item_model_path)
ensure_path(bed_model_path)

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

# sand
sand_types = ['texture pack default', 'alternative']
def set_sand_type():
    print("setting sand type to " + sand.tkvarq.get())
    d = 'Alternative Sand/' if sand.tkvarq.get() == sand_types[1] else ''
    for c in ['red_', '']:
        with open(os.path.join(block_model_path, c + 'sand.json'), 'w') as f:
            f.write('{"parent":"block/cube_all","textures":{"all":"blocks/' + d + c + 'sand"}}')
        with open(os.path.join(block_model_path, c + 'sandstone_all.json'), 'w') as f:
            f.write('{"parent":"block/cube_all","textures":{"all":"blocks/' + d + c + 'sandstone_top"}}')
        with open(os.path.join(block_model_path, c + 'sandstone_normal.json'), 'w') as f:
            f.write('{"parent":"block/cube_bottom_top","textures":{"bottom":"blocks/' + d + c + 'sandstone_bottom","top":"blocks/' + d + c + 'sandstone_top","side":"blocks/' + d + c + 'sandstone_normal"}}')
        with open(os.path.join(block_model_path, c + 'sandstone_chiseled.json'), 'w') as f:
            f.write('{"parent":"block/cube_column","textures":{"end":"blocks/' + d + c + 'sandstone_top","side":"blocks/' + d + c + 'sandstone_carved"}}')
        with open(os.path.join(block_model_path, c + 'sandstone_smooth.json'), 'w') as f:
            f.write('{"parent":"block/cube_column","textures":{"end":"blocks/' + d + c + 'sandstone_top","side":"blocks/' + d + c + 'sandstone_smooth"}}')
        with open(os.path.join(block_model_path, c + 'sandstone_inner_stairs.json'), 'w') as f:
            f.write('{"parent":"block/inner_stairs","textures":{"bottom":"blocks/' + d + c + 'sandstone_bottom","top":"blocks/' + d + c + 'sandstone_top","side":"blocks/' + d + c + 'sandstone_normal"}}')
        with open(os.path.join(block_model_path, c + 'sandstone_outer_stairs.json'), 'w') as f:
            f.write('{"parent":"block/outer_stairs","textures":{"bottom":"blocks/' + d + c + 'sandstone_bottom","top":"blocks/' + d + c + 'sandstone_top","side":"blocks/' + d + c + 'sandstone_normal"}}')
        with open(os.path.join(block_model_path, c + 'sandstone_stairs.json'), 'w') as f:
            f.write('{"parent":"block/stairs","textures":{"bottom":"blocks/' + d + c + 'sandstone_bottom","top":"blocks/' + d + c + 'sandstone_top","side":"blocks/' + d + c + 'sandstone_normal"}}')
        with open(os.path.join(block_model_path, 'half_slab_' + c + 'sandstone.json'), 'w') as f:
            f.write('{"parent":"block/half_slab","textures":{"bottom":"blocks/' + d + c + 'sandstone_bottom","top":"blocks/' + d + c + 'sandstone_top","side":"blocks/' + d + c + 'sandstone_normal"}}')
        with open(os.path.join(block_model_path, 'upper_slab_' + c + 'sandstone.json'), 'w') as f:
            f.write('{"parent":"block/upper_slab","textures":{"bottom":"blocks/' + d + c + 'sandstone_bottom","top":"blocks/' + d + c + 'sandstone_top","side":"blocks/' + d + c + 'sandstone_normal"}}')

# emerald
emerald_types = ['one', 'two']
def set_emerald_type():
    print("setting emerald type to " + emerald.tkvarq.get())
    d = '1' if emerald.tkvarq.get() == emerald_types[1] else ''
    with open(os.path.join(item_model_path, 'emerald.json'), 'w') as f:
        f.write('{"parent": "builtin/generated","textures": {"layer0": "items/emerald' + d + '"},"display": {"thirdperson": {"rotation": [ -90, 0, 0 ],"translation": [ 0, 1, -3 ],"scale": [ 0.55, 0.55, 0.55 ]},"firstperson": {"rotation": [ 0, -135, 25 ],"translation": [ 0, 4, 2 ],"scale": [ 1.7, 1.7, 1.7 ]}}}')

# -- initializing classes --

bed = selector(0, 'bed type', 'set bed type', bed_types, set_bed_type)
wool = selector(1, 'wool type', 'set wool type', wool_types, set_wool_type)
sand = selector(2, 'sand type', 'set sand type', sand_types, set_sand_type)
emerald = selector(3, 'emerald type', 'set emerald type', emerald_types, set_emerald_type)
# quit button
Button(root, text='quit', command=root.destroy).grid(row=10, columnspan=3)

root.mainloop()
