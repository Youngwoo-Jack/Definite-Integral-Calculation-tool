# Author: Jack Jeon
#
# This simplified version calculates only the exact definite integral
# for a user-defined polynomial.

class Monomial:
    def __init__(self, coef, degree):
        self.coef = coef
        self.degree = degree

    def __str__(self):
        return f"coefficient={self.coef}, degree={self.degree}"

# --- Polynomial & Integral Creation Functions ---

def createPoly(monomials):
    """Creates the polynomial as a dictionary."""
    poly = {f.degree: f.coef for f in monomials}
    return poly

def createIntegral(monomials):
    """Creates the integral of the polynomial in dictionary form."""
    integral = {f.degree + 1: f.coef / (f.degree + 1) for f in monomials}
    return integral


def evaluateIntegral(x, integral_dict):
    """Evaluates the integral function at a specific x value."""
    total = 0
    for degree, coef in integral_dict.items():
        total += coef * (x ** degree)
    return total

# --- Input Helper Functions ---

def createMonomialArray(degree):
    """Takes user input to create a list of monomials."""
    monomialArray = []
    for i in range(degree + 1):
        coef = float(input(f"Enter coefficient for degree {degree - i}: "))
        degreeMon = degree - i
        monomialArray.append(Monomial(coef, degreeMon))
    return monomialArray

def lowerbound():
     return float(input("Enter the lower bound for the integral: "))


def upperbound():
    return float(input("Enter the upper bound for the integral: "))

# --- Main Program ---

print("This program calculates the **exact definite integral** for a user-defined polynomial.\n")

while True:
    # Step 1: Polynomial input
    degree = int(input("Enter the degree of the polynomial: "))
    monomialArray = createMonomialArray(degree)
    poly = createPoly(monomialArray)

    print("\nYour polynomial is represented as a dictionary:")
    print("Degree : Coefficient")
    for deg, coef in poly.items():
        print(f"{deg} : {coef}")

    # Step 2: Create integral
    integral_dict = createIntegral(monomialArray)
    print("\nIntegral (antiderivative) dictionary:")
    print(integral_dict)

    # Step 3: Bounds
    low = lowerbound()
    hi = upperbound()

    # Step 4: Evaluate definite integral
    upper_value = evaluateIntegral(hi, integral_dict)
    lower_value = evaluateIntegral(low, integral_dict)
    answer = upper_value - lower_value

    print(f"\nThe exact definite integral of polynomial {poly}")
    print(f"from {low} to {hi} is: {answer}\n")
    # Step 5: Continue?
    again = input("Would you like to compute another integral? (y/n): ").strip().lower()
    
    if again != "y":
        print("\nProgram terminated.")
        break
