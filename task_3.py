import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def visualize_directory_structure(path):
    try:
        directory = Path(path)
        if not directory.exists() or not directory.is_dir():
            print(f"{Fore.RED}Шлях {path} не є директорією або не існує.")
            return
        
        def print_structure(current_path, indent=""):
            for item in current_path.iterdir():
                if item.is_dir():
                    print(f"{Fore.BLUE}{indent}📂 {item.name}")
                    print_structure(item, indent + "    ")
                else:
                    print(f"{Fore.GREEN}{indent}📜 {item.name}")
        
        print_structure(directory)
    except Exception as e:
        print(f"{Fore.RED}Сталася помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Будь ласка, вкажіть шлях до директорії як аргумент.")
    else:
        visualize_directory_structure(sys.argv[1])
