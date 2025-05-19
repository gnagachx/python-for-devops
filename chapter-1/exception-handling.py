thinkers = ['plato', 'playDo', 'Gumby']
while True:
    try:
        thinker = thinkers.pop()
        print(thinker)
    except IndexError as e:
        print("we tried to pop too many thinkers")
        print(e)
        break
    
# There are many built-in exceptions, such as IOError, KeyError and ImportError. Many third party packages also define their own exception classes. They indicate that something has gone very wrong.

