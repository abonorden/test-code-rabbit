import math

# Unoptimized code for basic calculus functions
class Calculus:

    def __init__(self):
        self.result = None  # store the result after computation

    def power(self, x, n):
        """Calculate power inefficiently"""
        res = 1
        for _ in range(n):
            res *= x
        return res

    def factorial(self, n):
        """Inefficient factorial function"""
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

    def differentiate(self, expr, var):
        """Differentiates a polynomial expression term by term (only polynomials supported)"""
        terms = expr.split('+')
        differentiated_terms = []

        for term in terms:
            if var in term:
                coef, power = 1, 1
                if '^' in term:
                    coef_part, power_part = term.split(var)
                    if coef_part:
                        coef = int(coef_part)
                    power = int(power_part[1:])
                elif term.strip(var):
                    coef = int(term.strip(var))

                new_coef = coef * power
                new_power = power - 1
                if new_power == 0:
                    differentiated_terms.append(f"{new_coef}")
                elif new_power == 1:
                    differentiated_terms.append(f"{new_coef}{var}")
                else:
                    differentiated_terms.append(f"{new_coef}{var}^{new_power}")

        self.result = " + ".join(differentiated_terms)
        return self.result

    def integrate(self, expr, var):
        """Integrates a polynomial expression term by term (only polynomials supported)"""
        terms = expr.split('+')
        integrated_terms = []

        for term in terms:
            if var in term:
                coef, power = 1, 1
                if '^' in term:
                    coef_part, power_part = term.split(var)
                    if coef_part:
                        coef = int(coef_part)
                    power = int(power_part[1:])
                elif term.strip(var):
                    coef = int(term.strip(var))

                new_power = power + 1
                new_coef = coef / new_power
                integrated_terms.append(f"{new_coef}{var}^{new_power}")
            else:
                integrated_terms.append(f"{term}{var}")

        self.result = " + ".join(integrated_terms) + " + C"
        return self.result

    def calculate_euler_number(self, precision):
        """Calculates Euler's number e using a very inefficient approach"""
        e = 0
        for i in range(precision):
            e += 1 / self.factorial(i)
        return e

# Sample usage (demonstrating inefficient and basic functionality)
calc = Calculus()

# Differentiation of "2x^3 + 4x^2 + 5x"
print("Differentiation result:", calc.differentiate("2x^3 + 4x^2 + 5x", "x"))

# Integration of "2x^3 + 4x^2 + 5x"
print("Integration result:", calc.integrate("2x^3 + 4x^2 + 5x", "x"))

# Calculating Euler's number with poor precision and efficiency
print("Euler's number (precision=10):", calc.calculate_euler_number(10))
