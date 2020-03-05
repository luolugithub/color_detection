# transparen 
convert mask_w_blue.png -fuzz 10% -transparent white a_transparent.png

# merge Merge Multiple Layers of Images into One
convert blue_mask_transparent.png green_mask_transparent.png -transparent white -composite red_mask_transparent.png -transparent white -composite result.png

