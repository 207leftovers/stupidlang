Symbol = str

# Determines the object type of the token string and returns the 
# token as its corresponding type
def typer(token):
    # If the token is the string 'true' or 'false', returns the 
    # corresponding boolean value
    if token == 'true':
        return True
    elif token == 'false':
        return False
    try:
        # If the token is not a boolean, check if it is an int, 
        # if so, return it as an int
        t = int(token)
        return t
    except ValueError:
        try:
            # If the token is neither a boolean, nor an int, check 
            # to see if it is a float, if so, return it as a float
            t = float(token)
            return t
        except ValueError:
            # If the type of the token isn't boolean, int or float, 
            # then return it as a string
            return Symbol(token)

# lex takes in a string, adds spacing to the parentheses, splits 
# it into its components and then runs typer on each element, 
# recombining the typed elements into a list
def lex(loc):
    tokenlist =  loc.replace('(', ' ( ').replace(')', ' ) ').split()
    return [typer(t) for t in tokenlist]

# syn takes in a list of tokens and breaks it up into sublists 
# based on parenthesis
def syn(tokens):
    # If there are no tokens in the list, then return an empty list
    if len(tokens) == 0:
        return []
    # Pop the first token off the list of tokens
    token = tokens.pop(0)
    # If the first token is a left parenthesis
    if token == '(':
        L = []
        # Recursively add sublists of tokens to the main list
        while tokens[0] != ')':
            L.append(syn(tokens))
        tokens.pop(0) # pop off ')'
        return L
    # If the first token wasn't a left parenthesis
    else:
        # If the first token was a right parenthesis then something 
        # is a bit screwy
        if token==')':
            assert 1, "should not have got here"
        # Otherwise, if the first token is neither a left nor right 
        # parenthesis, simply return the token
        return token
    
# Break down the string loc into a list with sublists for each
# parenthesied set of variables and operations
def parse(loc):
    return syn(lex(loc))