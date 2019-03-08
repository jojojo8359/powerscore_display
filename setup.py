import configparser
import platform

if platform.system() == 'Windows':
    print("Windows has been detected as your operating system.")
elif platform.system() == "Darwin":
    print("Mac OS has been detected as your operating system.")
elif platform.system() == "Linux":
    print("Linux has been detected as your operating system.")