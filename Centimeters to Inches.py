NB_CM_IN_INCH = 2.54

def convert_cm_in_inch(val):
    """Convert centermeters into inches"""
    return val / NB_CM_IN_INCH

def convert_inch_in_cm(val):
    """Convert inches into centemeters"""
    return val * NB_CM_IN_INCH

if __name__ == "__main__":
    nb_cm = float(input("Enter a number of centimeters: "))
    print("Entered number of %s centimeters is equal to %s inches" % (nb_cm, convert_cm_in_inch(nb_cm)))
