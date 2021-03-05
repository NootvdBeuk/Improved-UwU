@echo off
set /P bed=Bed type: 
echo {"parent":"block/bed_foot","textures":{"top":"blocks/beds/%bed%/bed_feet_top","end":"blocks/beds/%bed%/bed_feet_end","side":"blocks/beds/%bed%/bed_feet_side"}} > bed_foot.json
echo {"parent":"block/bed_head","textures":{"top":"blocks/beds/%bed%/bed_head_top","end":"blocks/beds/%bed%/bed_head_end","side":"blocks/beds/%bed%/bed_head_side"}} > bed_head.json
