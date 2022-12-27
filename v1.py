import pyautogui as pag


while True:
    img = pag.screenshot(region=(746,120, 451,800))

    px1 = img.getpixel((55, 560))
    px2 = img.getpixel((155, 560))
    px3 = img.getpixel((255, 560))
    px4 = img.getpixel((350, 560))

    if px1 <= (100,100,100):
        pag.moveTo((798, 570))
        pag.mouseDown()
        pag.mouseUp()

    elif px2 <= (100,100,100):
        pag.moveTo((908, 570))
        pag.mouseDown()
        pag.mouseUp()

    elif px3 <= (100,100,100):
        pag.moveTo((1025, 570))
        pag.mouseDown()
        pag.mouseUp()

    elif px4 <= (100,100,100):
        pag.moveTo((1138, 570))
        pag.mouseDown()
        pag.mouseUp()

    else:
        pass