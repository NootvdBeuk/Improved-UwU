@echo off
set /P bed=Bed type: 
echo {"parent":"block/bed_foot","textures":{"top":"blocks/beds/%bed%/bed_feet_top","end":"blocks/beds/%bed%/bed_feet_end","left":"blocks/beds/%bed%/bed_feet_left","right":"blocks/beds/%bed%/bed_feet_right"}} > bed_foot.json
echo {"parent":"block/bed_head","textures":{"top":"blocks/beds/%bed%/bed_head_top","end":"blocks/beds/%bed%/bed_head_end","left":"blocks/beds/%bed%/bed_head_left","right":"blocks/beds/%bed%/bed_head_right"}} > bed_head.json
