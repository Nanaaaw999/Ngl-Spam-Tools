import random
import string
import requests
import os
from pystyle import Colors, Colorate
import time
import sys
def ngl():
    # Pink color scheme
    R = '\033[1;31m'  # Bright Red
    G = '\033[1;32m'  # Bright Green
    Y = '\033[1;33m'  # Bright Yellow
    B = '\033[1;34m'  # Bright Blue
    P = '\033[1;35m'  # Bright Magenta (Pink)
    C = '\033[1;36m'  # Bright Cyan
    W = '\033[0m'     # Reset
    
    def clear_screen():
        os.system('clear')
    
    def get_term_width():
        try:
            return os.get_terminal_size().columns
        except:
            return 80
    
    def deviceId():
        characters = string.ascii_lowercase + string.digits
        part1 = ''.join(random.choices(characters, k=8))
        part2 = ''.join(random.choices(characters, k=4))
        part3 = ''.join(random.choices(characters, k=4))
        part4 = ''.join(random.choices(characters, k=4))
        part5 = ''.join(random.choices(characters, k=12))
        device_id = f"{part1}-{part2}-{part3}-{part4}-{part5}"
        return device_id
    
    def UserAgent():
        try:
            with open('user-agents.txt', 'r') as file:
                user_agents = file.readlines()
                return random.choice(user_agents).strip()
        except:
            return random.choice([
                'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            ])
            
    def randomEmoji():
        return random.choice([
            '😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '😊', '😇', '🙂', '🙃', '😉', '😌', 
            '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨', '🧐', '🤓', 
            '😎', '🤩', '🥳', '😏', '😒', '😞', '😔', '😟', '😕', '🙁', '☹️', '😣', '😖', '😫', 
            '😩', '🥺', '😢', '😭', '😤', '😠', '😡', '🤬', '🤯', '😳', '🥵', '🥶', '😱', '😨', 
            '😰', '😥', '😓', '🤗', '🤔', '🤭', '🤫', '🤥', '😶', '😐', '😑', '😬', '🙄', '😯', 
            '😦', '😧', '😮', '😲', '🥱', '😴', '🤤', '😪', '😵', '🤐', '🥴', '🤢', '🤮', '🤧', 
            '😷', '🤒', '🤕', '🤑', '🤠'
        ])
        
    def progressBar(iteration, total, prefix='', suffix='', length=40):
        # Calculate percentage
        percent = 100 * (iteration / float(total))
        # Calculate filled length
        filled_length = int(length * iteration // total)
        # Create the progress bar
        bar = '█' * filled_length + '░' * (length - filled_length)
        # Format percentage to show integer when 100, else one decimal
        if percent == 100:
            percent_str = "100%"
        else:
            percent_str = f"{percent:.1f}%"
        # Print the progress bar
        print(f'\r{P}{prefix} |{G}{bar}{P}| {Y}{percent_str}{P} {suffix}{W}', end='\r')
        # Print newline when complete
        if iteration == total:
            print()
            
    def print_box(text, color=P):
        width = get_term_width()
        box_width = min(width - 4, len(text) + 4)
        padding = (width - box_width) // 2
        
        print(' ' * padding + color + '┌' + '─' * (box_width - 2) + '┐' + W)
        print(' ' * padding + color + '│' + text.center(box_width - 2) + '│' + W)
        print(' ' * padding + color + '└' + '─' * (box_width - 2) + '┘' + W)
        
    def print_centered(text, color=P):
        width = get_term_width()
        padding = (width - len(text)) // 2
        print(' ' * padding + color + text + W)
        
    def print_line(char='═', color=P):
        width = get_term_width()
        print(color + char * width + W)
        
    def loading_animation(text="Loading", duration=1):
        frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        end_time = time.time() + duration
        
        while time.time() < end_time:
            for frame in frames:
                if time.time() >= end_time:
                    break
                print(f'\r{P}[{frame}]{W} {text}...', end='')
                time.sleep(0.05)
        
        print(f'\r{P}[✓]{W} {text} completed!')
        
    def print_anime_art():
        # Anime ASCII art with pink theme
        art = [
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣷⣦⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣾⣿⠿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⣿⣿⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⢀⣴⡾⠟⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠻⠷⣶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⢀⡴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⣠⠏⠀⠀⠀⣀⣠⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⡆⠀⠀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠁⠀⠀⣰⢛⣥⣤⣤⣀⠉⠛⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣀⢀⣤⠶⠚⠛⠉⠉⠉⠛⠛⠲⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            "⠀⠀⠀⣤⣀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣤⣤⣟⣿⣷⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⡀⠙⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀",
            "⢠⣄⣀⡈⢛⣿⣿⡿⠋⡠⣴⣿⠋⠉⠙⠻⣷⡌⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠜⣹⣿⣿⡿⢿⣿⣿⡿⠛⠛⠛⠿⣿⣿⣿⣷⣦⣾⠿⢧⡀⠀⡀⠀⠀⠀",
            "⠀⠉⠻⠿⢿⣿⣿⢣⠎⢠⣿⠁⠀⠀⠀⢀⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⣿⠝⣳⣿⡿⠃⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣶⣶⡷⣞⠁⠀⠀⠀",
            "⠀⠀⠀⠀⠈⣿⡏⡆⠀⢸⡇⠀⠀⠀⢀⣾⠋⣻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠋⠀⠃⠀⣿⣿⠃⠀⠀⠀⠀⠀⢀⣼⠟⠻⣿⣿⢿⣿⣿⣶⣤⣀⣀⠀⠀",
            "⠀⠀⠀⠀⠀⠘⣿⡅⠀⢸⣷⡀⢀⣴⣿⠟⠛⢿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⢀⣤⣿⣿⣶⣾⣿⣿⠈⢻⣿⡿⠛⠛⠛⠛⠉",
            "⠀⠀⠀⠀⠀⠀⠘⢧⠀⠘⣿⣿⣿⣿⠃⠀⠀⣼⢿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣦⣤⣤⣶⣿⡟⠁⠀⠀⣿⢿⡟⠀⠸⣿⣷⠀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠹⠁⠙⣿⣷⣤⡾⡟⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡟⠙⢻⣿⡿⢿⠀⠀⢀⣴⠻⣾⠇⠀⢸⠏⠹⣆⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣡⡴⠶⢾⣅⣠⣥⣶⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⡀⣸⣿⠤⠈⣶⣖⣹⣿⡾⠃⢀⠰⠋⠀⠀⠀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣙⣷⣿⣤⣌⡿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣾⡷⠞⢛⠻⣿⠿⢒⣾⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠻⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣷⣷⣮⣭⣭⠿⠖⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠘⠋⠉⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
        ]
        
        width = get_term_width()
        max_line_len = max(len(line) for line in art)
        
        # Check if terminal is too small for the art
        if width < max_line_len:
            # Compact version for small terminals
            art = [
                "⠀⠀⠀⠀⠀⠀⣀⣤⣴⣾⠃⠀⠀⠀⠀⠈⢿⣷⣦⣤⣄⣀⠀⠀⠀⠀⠀⠀",
                "⠀⠀⢀⣤⣴⣾⣿⠿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⣿⣿⣶⣦⣤⣄⡀",
                "⠀⢀⣴⡾⠟⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠻⠷⣶⣄",
                "⢀⡴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠷⣦",
                "⣠⠏⠀⠀⠀⣀⣠⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⡆",
                "⠁⠀⠀⣰⢛⣥⣤⣤⣀⠉⠛⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣀⢀⣤⠶⠚⠛⠉⠉⠛⠛⠲⢤",
                "⣤⣀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣤⣤⣟⣿⣷⣿⣿⣿⣿⣿⣿⣷⣦",
                "⢠⣄⣀⡈⢛⣿⣿⡿⠋⡠⣴⣿⠋⠉⠙⠻⣷⡌⢳⡀⠀⠀⠀⠀⠀⠀⠜⣹⣿⣿⡿⢿⣿⣿⡿⠛⠛⠛⠿⣿⣿⣿⣷",
                "⠀⠉⠻⠿⢿⣿⣿⢣⠎⢠⣿⠁⠀⠀⠀⢀⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⣼⡿⣿⠝⣳⣿⡿⠃⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿",
                "⠀⠀⠀⠀⠈⣿⡏⡆⠀⢸⡇⠀⠀⠀⢀⣾⠋⣻⣷⠀⠀⠀⠀⠀⠀⠠⠋⠀⠃⠀⣿⣿⠃⠀⠀⠀⠀⠀⢀⣼⠟⠻⣿⣿⢿⣿",
                "⠀⠀⠀⠀⠀⠘⣿⡅⠀⢸⣷⡀⢀⣴⣿⠟⠛⢿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⢀⣤⣿⣿⣶⣾⣿⣿⠈⢻⣿",
                "⠀⠀⠀⠀⠀⠀⠘⢧⠀⠘⣿⣿⣿⣿⠃⠀⠀⣼⢿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣦⣤⣤⣶⣿⡟⠁⠀⠀⣿⢿⡟⠀⠸⣿",
                "⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠹⠁⠙⣿⣷⣤⡾⡟⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡟⠙⢻⣿⡿⢿⠀⠀⢀⣴⠻⣾⠇⠀⢸⠏",
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣡⡴⠶⢾⣅⣠⣥⣶⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⡀⣸⣿⠤⠈⣶⣖⣹⣿⡾⠃⢀⠰⠋⠀",
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣙⣷⣿⣤⣌⡿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣾⡷⠞⢛⠻⣿⠿⢒⣾⡿⠃⠀⠀⠀",
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠻⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣷⣷⣮⣭⣭⠿⠖⠛⠉⠀⠀",
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠘⠋⠉⠘⠁⠀⠀⠀⠀⠀⠀⠀"
            ]
            max_line_len = max(len(line) for line in art)
        
        # Calculate padding to center the art
        padding = (width - max_line_len) // 2
        
        # Print with pink color gradient and centering
        for line in art:
            print(' ' * padding + Colorate.Horizontal(Colors.red_to_purple, line))
            
    def print_header():
        clear_screen()
        print_anime_art()
        print_line('═', P)
        print_centered("✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦", Y)
        print_box("NGL SPAM TOOL V1.0 - PINK EDITION", P)
        print_centered("✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦", Y)
        print_line('═', P)
        print_centered("CREATED BY NANAW", Y)
        print_line('═', P)
        
    def print_info():
        print_line('═', P)
        print_centered("✦ TOOLS INFORMATION ✦", Y)
        print_line('═', P)
        print(P + "This tool allows you to send anonymous messages to NGL users" + W)
        print(P + "with different spam modes and customizable options." + W)
        print_line('═', P)
        print_centered("✦ AVAILABLE FEATURES ✦", Y)
        print_line('═', P)
        print(P + "• Multiple spam modes with different speeds" + W)
        print(P + "• Random emoji for each message" + W)
        print(P + "• Session logging to history file" + W)
        print(P + "• Device ID rotation for better anonymity" + W)
        print_line('═', P)
        print_centered("✦ DISCLAIMER ✦", Y)
        print_line('═', P)
        print(P + "This tool is for educational purposes only." + W)
        print(P + "Spam your girlfriend if she doesn't reply to your chat" + W)
        print_line('═', P)
        
    def show_main_menu():
        print_line('═', P)
        print_centered("✦ MAIN MENU ✦", Y)
        print_line('═', P)
        print(P + "[1] " + W + "Start Spam")
        print(P + "[2] " + W + "View Information")
        print(P + "[3] " + W + "Exit")
        print_line('═', P)
        
        choice = input(P + "[✦] " + W + "Choose option (1/2/3): ")
        return choice
        
    def start_spam():
        print_header()
        
        print_line('═', P)
        print_centered("✦ SELECT SPAM MODE ✦", Y)
        print_line('═', P)
        print(P + "[1] " + W + "Normal Spam (1.0s delay)")
        print(P + "[2] " + W + "Fast Spam (0.5s delay)")
        print(P + "[3] " + W + "Brutal Spam (0.1s delay)")
        print(P + "[4] " + W + "Super Brutal Spam (0.01s delay)")
        print(P + "[5] " + W + "Ultra Super Brutal Spam (0.0s delay)")
        print(P + "[6] " + W + "Custom Mode")
        print(P + "[0] " + W + "Back to Main Menu")
        print_line('═', P)
        
        mode = input(P + "[✦] " + W + "Choose mode (1/2/3/4/5/6/0): ")
        
        if mode == "0":
            return False
        
        if mode == "1":
            delay = 1.0
            mode_name = "Normal"
        elif mode == "2":
            delay = 0.5
            mode_name = "Fast"
        elif mode == "3":
            delay = 0.1
            mode_name = "Brutal"
        elif mode == "4":
            delay = 0.01
            mode_name = "Super Brutal"
        elif mode == "5":
            delay = 0.0
            mode_name = "Ultra Super Brutal"
        elif mode == "6":
            mode_name = "Custom"
            while True:
                custom_delay_input = input(P + "[✦] " + W + "Enter custom delay (in seconds): ")
                try:
                    delay = float(custom_delay_input)
                    if delay < 0:
                        print(R + "[-] " + W + "Delay cannot be negative!")
                        continue
                    break
                except ValueError:
                    print(R + "[-] " + W + "Invalid input! Please enter a number.")
        else:
            print(R + "[-] " + W + "Invalid mode selected!")
            time.sleep(2)
            return False
        
        loading_animation("Initializing spam mode")
        
        print_line('═', P)
        print_centered(f"✦ {mode_name.upper()} MODE SELECTED ✦", Y)
        print_line('═', P)
        time.sleep(1)
        
        nglusername = input(P + "[✦] " + W + "Target Username: ")
        message = input(P + "[✦] " + W + "Message: ")
        
        # Handle empty input for message count
        while True:
            count_input = input(P + "[✦] " + W + "Number of messages: ")
            if count_input.strip() == "":
                print(R + "[-] " + W + "Please enter a valid number!")
                continue
            try:
                Count = int(count_input)
                if Count <= 0:
                    print(R + "[-] " + W + "Please enter a positive number!")
                    continue
                break
            except ValueError:
                print(R + "[-] " + W + "Invalid input! Please enter a number.")
        
        print_line('═', P)
        print_centered("✦ MESSAGE PREVIEW ✦", Y)
        print_line('═', P)
        print_centered(f"{message} {randomEmoji()}", G)
        print_line('═', P)
        
        confirm = input(P + "[?] " + W + "Start sending messages? (y/n): ").lower()
        if confirm != 'y':
            print(P + "[!] " + W + "Operation cancelled.")
            time.sleep(1)
            return False
        
        loading_animation("Preparing to send messages")
        
        print_line('═', P)
        print_centered("✦ STARTING SPAM ✦", Y)
        print_line('═', P)
        print()
        
        value = 0
        notsend = 0
        
        # Initialize progress bar
        progressBar(0, Count, prefix='Progress:', suffix='Starting...')
        
        with open('history.txt', 'a') as history_file:
            history_file.write(f"\n\n=== NGL SPAM SESSION - {time.strftime('%Y-%m-%d %H:%M:%S')} ===\n")
            history_file.write(f"User: {username}\n")
            history_file.write(f"Mode: {mode_name}\n")
            history_file.write(f"Target: {nglusername}\n")
            history_file.write(f"Message: {message}\n")
            history_file.write(f"Count: {Count}\n")
            history_file.write(f"Delay: {delay}\n\n")
            
            while value < Count:
                headers = {
                    'Host': 'ngl.link',
                    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                    'accept': '*/*',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'x-requested-with': 'XMLHttpRequest',
                    'sec-ch-ua-mobile': '?0',
                    'user-agent': UserAgent(),
                    'sec-ch-ua-platform': '"Linux"',
                    'origin': 'https://ngl.link',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': f'https://ngl.link/{nglusername}',
                    'accept-language': 'en-US,en;q=0.9',
                }
                
                emoji_msg = f"{message} {randomEmoji()}"
                
                data = {
                    'username': nglusername,
                    'question': emoji_msg,
                    'deviceId': deviceId(),
                    'gameSlug': '',
                    'referrer': '',
                }
                
                try:
                    response = requests.post('https://ngl.link/api/submit', headers=headers, data=data)
                    
                    if response.status_code == 200:
                        notsend = 0
                        value += 1
                        # Update progress bar after successful send
                        progressBar(value, Count, prefix='Progress:', suffix='Complete')
                        # Print emoji message on new line after progress bar
                        print()
                        print(G + "[✓] " + W + f"Sent: {value}/{Count} -> {emoji_msg}")
                        history_file.write(f"[{time.strftime('%H:%M:%S')}] Sent: {emoji_msg}\n")
                    else:
                        notsend += 1
                        # Update progress bar even if failed (showing current progress)
                        progressBar(value, Count, prefix='Progress:', suffix='Failed')
                        # Print emoji message on new line after progress bar
                        print()
                        print(R + "[✗] " + W + "Failed to send")
                        history_file.write(f"[{time.strftime('%H:%M:%S')}] Failed to send\n")
                    
                    if notsend == 4:
                        print(Y + "[!] " + W + "Changing device information")
                        deviceId()
                        UserAgent()
                        notsend = 0
                        
                    time.sleep(delay)
                    
                except Exception as e:
                    # Update progress bar even if error
                    progressBar(value, Count, prefix='Progress:', suffix='Error')
                    # Print emoji message on new line after progress bar
                    print()
                    print(R + "[✗] " + W + f"Error: {str(e)}")
                    history_file.write(f"[{time.strftime('%H:%M:%S')}] Error: {str(e)}\n")
                    time.sleep(delay)
            
            # Final progress bar update
            progressBar(Count, Count, prefix='Progress:', suffix='Complete')
            print()
            print_line('═', P)
            print_centered("✦ SPAM COMPLETED ✦", G)
            print_centered(f"✦ {value} MESSAGES SENT ✦", G)
            print_centered("✦ LOGGED TO HISTORY ✦", G)
            print_line('═', P)
            
            time.sleep(3)
            return True
            
    def exit_program():
        print_line('═', P)
        print_centered("✦ EXITING PROGRAM ✦", Y)
        print_line('═', P)
        loading_animation("Saving session data")
        print(P + "[+] " + W + "Thank you for using NGL Spam Tool!")
        print(P + "[+] " + W + "Have a great day!")
        print_line('═', P)
        sys.exit(0)
        
    # Main program flow
    print_header()
    print_info()
    
    username = input(P + "[✦] " + W + "Username: ")
    
    print_line('═', P)
    print_centered(f"✦ WELCOME, {username.upper()}! ✦", Y)
    print_line('═', P)
    
    loading_animation("Loading user profile")
    
    while True:
        print_header()
        choice = show_main_menu()
        
        if choice == "1":
            loading_animation("Starting spam module")
            start_spam()
        elif choice == "2":
            loading_animation("Loading information")
            print_header()
            print_info()
            input(P + "[✦] " + W + "Press Enter to continue...")
        elif choice == "3":
            exit_program()
        else:
            print(R + "[-] " + W + "Invalid option!")
            time.sleep(1)
if __name__ == "__main__":
    try:
        ngl()
    except KeyboardInterrupt:
        print("\n" + R + "[!] Program interrupted by user" + W)
        sys.exit(0)
encripsi kode ini