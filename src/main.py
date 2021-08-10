import traceback
import pdb

from debuginfo import debuginfo

# ------------------------------------------------------------------------------
def grr(arg):
    debuginfo(arg)      # <-- stack()[1][0] for this line

# grr("aargh")            # <-- stack()[2][0] for this line

# ------------------------------------------------------------------------------
def main():
    myvar = 27
    myname = "jake"
    debuginfo(f"my name is {myname}")

    # myprint(myname)
    myname = "Barker"
    debuginfo(f"my name is {myname}")

# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
    print("\n---------------------------------------------------\n")
    grr("aargh")
