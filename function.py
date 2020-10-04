class Function:
    def __init__(self, func):
        self.func = func.lower().replace(" ", "").split("=")[1]
        self.parts = list(map(self.func_parts, self.func.split("+")))
        self.calcd_parts = self.parts

    def func_parts(self, x):
        if "-" in x:
            return x.split("-")
        else:
            return x
    
    def exponent(self, part):
        if "^" in part:
            return float(part.split("^")[1])
        else:
            return 1.0

    def mantissa(self, part):
        if part.split("x")[0] != "":
            return float(part.split("x")[0])
        else:
            return 1.0

    def calc_mantissa_exponent(self):
        for place, part in enumerate(self.parts):

            if type(part) is list:

                for sub_place, sub_part in enumerate(part):

                    if "x" in sub_part:
                        exponent = self.exponent(sub_part)
                        mantissa = self.mantissa(sub_part)

                        if "^" in sub_part:
                            self.calcd_parts[place][sub_place] = f"{mantissa*exponent}x^{exponent-1}"

                        else:
                            self.calcd_parts[place][sub_place] = str(mantissa)

                    else:
                        self.calcd_parts[place].remove(sub_part)
            else:
                if "x" in part:
                    exponent = self.exponent(part)
                    mantissa = self.mantissa(part)

                    if "^" in part:
                        self.calcd_parts[place] = f"{mantissa*exponent}x^{exponent-1}"

                    else:
                        self.calcd_parts[place] = str(mantissa)

                else:
                    self.calcd_parts.remove(part)

        return self.calcd_parts

    def create_subtraction(self, part):
        if type(part) is list:
            return "-".join(part)
        else:
            return part

    def create_addition(self):
        return "+".join(self.calcd_parts)

    def make_derivative(self):
        for place, part in enumerate(self.calcd_parts):
            self.calcd_parts[place] = self.create_subtraction(part)

        self.calcd_parts = self.create_addition()

        return self.calcd_parts

    def derivative(self):
        self.calc_mantissa_exponent()
        derivative = self.make_derivative()

        return derivative

    def to_eval(self, derivative):
        return derivative.replace("x", "*x").replace("^", "**")