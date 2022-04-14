from colorama import Fore, Style, Back

print([f"fore_{color.lower()}" for color in dir(Fore) if not color.startswith("_")]+[]+[])
