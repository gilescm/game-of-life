import sys
import subprocess

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

# Example
if __name__ == '__main__':
    install('argparse')
    install('numpy')
    install('matplotlib')