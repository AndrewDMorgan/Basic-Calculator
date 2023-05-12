
# computes the result of two values and a mathmatical operator
def Compute(val: int, sym: str, val2: int) -> int:
    if sym in "*":
        return val * val2
    if sym == "/":
        return val / val2
    if sym == "+":
            return val + val2
    if sym == "-":
        return val - val2

# compresses a syntax (like goes through and does all the multiplaction)
def ParseSyntax(syntax: list, syntaxes: list) -> list:
    newSyntaxes = syntaxes[:]
    i = 0
    for syn in syntaxes[:-1]:
        if syntaxes[i + 1] in syntax:
            del newSyntaxes[i]
            del newSyntaxes[i]
            newSyntaxes[i] = Compute(syntaxes[i], syntaxes[i + 1], syntaxes[i + 2])
            return ParseSyntax(syntax, newSyntaxes)
        i += 1
    return newSyntaxes


# gets the mathmatical expresion
expression = input(">> ")

# formats the expression into a form the computer can read easier
syntaxes = expression.split(" ")
formated = []

for syntax in syntaxes:
    try:
        formated.append(int(syntax))
    except ValueError:
        formated.append(syntax)

# compressing what the user entered into a final answer
formated = ParseSyntax(["*", "/"], formated)
formated = ParseSyntax(["+", "-"], formated)

# printing the results
print(formated)

