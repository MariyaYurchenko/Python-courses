import sys
import subprocess as subpr
from pkg_resources import working_set as pkg_set

required = {'cowsay'}
installed = {pkg.key for pkg in pkg_set}
missing = required - installed

if missing:
    python = sys.executable
    subpr.check_call([python, '-m', 'pip', 'install', *missing], stdout=subpr.DEVNULL)

try:
    import cowsay

except:
    sys.exit("Cowsay wasn't imported")

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])