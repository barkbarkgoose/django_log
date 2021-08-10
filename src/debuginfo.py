import inspect
from inspect import getframeinfo, stack
import pdb

def debuginfo(message, debug=False):
    # --- print stack info and message ---
    caller = getframeinfo(stack()[1][0])
    print(f"called by - {caller.filename}:{caller.lineno}") # python3 syntax print
    print(f"message: {message}")

    # --- print local variables ---
    print("__local vars___")
    frame = inspect.currentframe()
    try:
        print(frame.f_back.f_locals)
    finally:
        del frame

    # local_vars = locals()
    # for item in local_vars:
    #     if local_vars[item] not in (caller, message):
    #         print(f"\t{item}: {local_vars[item]}")

    print()



"""
https://stackoverflow.com/questions/301134/how-to-import-a-module-given-its-name-as-string
import importlib
spec = importlib.util.spec_from_file_location('main', 'main.py')
module = importlib.util.module_from_spec(spec)

https://stackoverflow.com/questions/6618795/get-locals-from-calling-namespace-in-python

"""
