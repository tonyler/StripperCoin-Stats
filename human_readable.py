#A custom function to to transform numbers into human-readable formats with suffixes
def formatIt(hello):
    hello = str(hello)
    if hello.isalpha(): 
        return hello 
    else: 
        hello=int(hello)
        suffixes = ["", "K", "M", "B", "T"]
        hello = str("{:,}".format(hello))
        commas = 0
        x = 0
        while x < len(hello):
            if hello[x] == ',':
                commas += 1
            x += 1
        return hello.split(',')[0] + '.' + hello.split(',')[1][:-1] + suffixes[commas]
