from pathlib import Path
import subprocess, sys

ROOT=Path(__file__).resolve().parents[1]

if __name__=='__main__':
    sys.exit(subprocess.call([sys.executable, str(ROOT/'tools'/'validate.py')]))
