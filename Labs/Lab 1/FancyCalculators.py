import math

last_input = "-1"

while last_input != 'e':

    print("Which calculator would you like to use?")
    last_input = input("(C)one area / (F)ahrenheit to Celsius / (T)rapezoid area / (E)xit: ").lower()

    try:
        if last_input == 'c':
            # Calculate area of a cone
            # INPUTS
            #   - Radius (float)
            #   - Height (float)
            # OUTPUT
            #   - Area (print)
            print("~~~~~ CALCULATE AREA OF CONE ~~~~~")
            print("Area of the cone: ", (1/3)*(3.14159*math.pow(float(input("Enter radius of cone: ")),2)*float(input("Enter height of cone: "))))

        elif last_input == 'f':
            # Calculate fahrenheit to celsius
            # INPUTS
            #   - Fahrenheit (float)
            # OUTPUT
            #   - Celsius (print)
            print("\n~~~~~ CALCULATE FAHRENHEIT TO CELSIUS ~~~~~")
            print("The temperature in Celsius: ", (float(input("Enter temperature in Fahrenheit: ")) -32.0 ) * (5/9))

        elif last_input == 't':
            # Calculate area of a trapezoid
            # INPUTS
            #   - Top base (float)
            #   - Bottom base (float)
            #   - Height (float)
            # OUTPUT
            #   - Area (print)
            print("\n~~~~~ CALCULATE AREA OF TRAPEZOID ~~~~~")
            print("The area is: ", (1/2)*(float(input("Enter trapezoid length of bottom: ")) + float(input("Enter trapezoid length of top: ")))*float(input("Enter trapezoid height: ")))
    except:
        print("WARNING: An invalid input was detected! Resetting...")

    print("\n\n")
