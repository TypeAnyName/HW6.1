colors = ["░", "▒", "▓"]


def draw_carpet(w, h):
    if h <= 2:
        for i in range(0, h):
            print("▓" + "░" * w + "▓")
    elif h > 2:
        print("▓" + "░" * w + "▓")
        for i in range(0, h - 2):
            print("▓" + "░" + "▒" * (w - 2) + "░" + "▓")
        print("▓" + "░" * w + "▓")
