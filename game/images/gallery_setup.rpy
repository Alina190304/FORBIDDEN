init python:

    def MaxScale(img, minwidth=config.screen_width, minheight=config.screen_height):
        currwidth, currheight = renpy.image_size(img)
        xscale = float(minwidth) / currwidth
        yscale = float(minheight) / currheight
        
        if xscale > yscale:
            maxscale = xscale
        else:
            maxscale = yscale
        
        return im.FactorScale(img, maxscale, maxscale)

    def MinScale(img, maxwidth=config.screen_width, maxheight=config.screen_height):
        currwidth, currheight = renpy.image_size(img)
        xscale = float(maxwidth) / currwidth
        yscale = float(maxheight) / currheight
        
        if xscale < yscale:
            maxscale = xscale
        else:
            maxscale = yscale
        
        return im.FactorScale(img, MinScale, MinScale)

    maxnumx = 3
    maxnumy = 2
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    gallery_page = 0
    closeup_page = 0


    class GalleryItem:
        def __init__(self, name, images, thumb, locked="lockedthumb"):
            self.name = name
            self.images = images
            self.thumb = thumb
            self.locked = locked
            self.refresh_lock()
        
        def num_images(self):
            return len(self.images)
        
        def refresh_lock(self):
            self.num_unlocked = 0
            lockme = False
            for img in self.images:
                if not renpy.seen_image(img):
                    lockme = True
                else:
                    self.num_unlocked += 1
            self.is_locked = lockme



    gallery_items = []
    gallery_items.append(GalleryItem("Image 1", ["img1"], "thumb1"))
    gallery_items.append(GalleryItem("Image 2", ["img2"], "thumb2"))
    gallery_items.append(GalleryItem("Image 3", ["img3"], "thumb3"))
    gallery_items.append(GalleryItem("Image 4", ["img4"], "thumb4"))
    gallery_items.append(GalleryItem("Image 5", ["img5"], "thumb5"))
    gallery_items.append(GalleryItem("Image 6", ["img6"], "thumb6"))
    gallery_items.append(GalleryItem("Image 7", ["img7"], "thumb7"))
    gallery_items.append(GalleryItem("Image 8", ["img8"], "thumb8"))
    gallery_items.append(GalleryItem("Image 9", ["img9"], "thumb9"))
    gallery_items.append(GalleryItem("Image 10", ["img10"], "thumb10"))
    gallery_items.append(GalleryItem("Image 11", ["img11"], "thumb11"))
    gallery_items.append(GalleryItem("Image 12", ["img12"], "thumb12"))
    gallery_items.append(GalleryItem("Image 13", ["img13"], "thumb13"))
    gallery_items.append(GalleryItem("Image 14", ["img14"], "thumb14"))
    gallery_items.append(GalleryItem("Image 15", ["img15"], "thumb15"))
    gallery_items.append(GalleryItem("Image 16", ["img16"], "thumb16"))
    gallery_items.append(GalleryItem("Image 17", ["img17"], "thumb17"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
