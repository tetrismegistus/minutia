import pyautogui
import time


def verify(func):
    def wrapper(loc_tup, expected_col, optional=None):
        im = pyautogui.screenshot()
        print(im.getpixel(loc_tup))
        try:
            assert (im.getpixel(loc_tup) == expected_col)
        except AssertionError:
            assert (im.getpixel(loc_tup) == optional)
        func(loc_tup)
    return wrapper


@verify
def move_and_click(loc_tup):
    pyautogui.moveTo(*loc_tup)
    pyautogui.click(*loc_tup)


@verify
def move_and_dclick(loc_tup):
    pyautogui.moveTo(*loc_tup)
    pyautogui.doubleClick(*loc_tup)


@verify
def move(loc_tup):
    pyautogui.moveTo(*loc_tup)


@verify
def drag_to(loc_up):
    pyautogui.dragTo(*loc_up, button='left', duration=0.2)


def run_sequence():
    top_folder_label = (369, 223)
    folder_titlebar = (476, 20)
    renamer_drag_area = (1113, 111)
    select_all_button = (930, 73)
    rename_button = (1369, 402)
    back_folder_button = (276, 169)
    cut_button = (352, 78)
    paste_button = (1228, 504)

    selected_folder_col = (255, 232, 150)
    select_all_col = (57, 154, 232)
    white = (255, 255, 255)
    rename_gray = (240, 240, 240)
    back_folder_col = (128, 128, 128)
    cut_col = (235, 238, 241)
    cut_col2 = (230, 239, 244)
    paste_col = (247, 247, 247)
    paste_col2 = (231, 239, 251)
    top_folder_label_col2 = (248, 249, 250)

    move_and_dclick(top_folder_label, expected_col=selected_folder_col)
    move_and_click(select_all_button, expected_col=select_all_col)
    move(top_folder_label, expected_col=white, optional=top_folder_label_col2)
    drag_to(renamer_drag_area, expected_col=white)
    move_and_click(rename_button, expected_col=rename_gray)
    move_and_click(back_folder_button, expected_col=back_folder_col)
    move_and_dclick(cut_button, expected_col=cut_col, optional=cut_col2)
    time.sleep(.3)
    move_and_dclick(paste_button, expected_col=paste_col, optional=paste_col2)
    time.sleep(.1)
    move_and_click(folder_titlebar, expected_col=white)
    pyautogui.press('f5')
    pyautogui.press('f5')


def main():
    while True:
        pyautogui.PAUSE = .3
        run_sequence()


if __name__ == '__main__':
    main()
