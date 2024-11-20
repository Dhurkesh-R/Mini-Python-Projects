import curses
from curses import wrapper
import time
import random
import os

HIGHEST_WPM_FILE = "highest_wpm.txt"

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0, highest_wpm=0):
    h, w = stdscr.getmaxyx()
    if len(target) > w:
        target = target[:w]
    stdscr.addstr(0, 0, target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")
    stdscr.addstr(1, 20, f"Highest WPM: {highest_wpm}")

    for i, char in enumerate(current):
        if i < w:
            correct_char = target[i]
            color = curses.color_pair(1)
            if char != correct_char:
                color = curses.color_pair(2)

            stdscr.addstr(0, i, char, color)

def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def load_highest_wpm():
    if os.path.exists(HIGHEST_WPM_FILE):
        with open(HIGHEST_WPM_FILE, "r") as f:
            data = f.read().strip()
            if data.isdigit():
                return int(data)
    return 0

def save_highest_wpm(wpm):
    with open(HIGHEST_WPM_FILE, "w") as f:
        f.write(str(wpm))

def wpm_test(stdscr, highest_wpm):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm, highest_wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getch()
            if key == -1:
                continue
        except:
            continue

        if key == 27:  # Escape key
            break

        if key in (curses.KEY_BACKSPACE, 127, 8):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(chr(key))

    completion_time = time.time() - start_time
    return wpm, completion_time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

    highest_wpm = load_highest_wpm()
    while True:
        wpm, completion_time = wpm_test(stdscr, highest_wpm)
        stdscr.addstr(2, 0, f"You completed the text in {completion_time:.2f} seconds! Press any key to continue...")

        if wpm > highest_wpm:
            highest_wpm = wpm
            save_highest_wpm(highest_wpm)
            stdscr.addstr(3, 0, f"New highest WPM: {highest_wpm}!")

        stdscr.nodelay(False)
        key = stdscr.getch()
        
        if key == 27:  # Escape key
            break

wrapper(main)
