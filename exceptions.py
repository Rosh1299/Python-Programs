
try:
    file = open("lists.py")
    age = int(input("Age:"))
    xfactor = 10/age
    # handling multiple exceptions.
except (ValueError, ZeroDivisionError):
    print("You didn't entered a valid age.")
else:
    print('No exceptions were thrown.')
# it will executes exception ocuured or not.
finally:
    file.close()
print("Execution completed.")


# when python executes the code that we have in try block
# if any of the statement throws an exception that matches one of
# the except clauses, that except clauses is executed and the other
# except clauses are ignored.


try:
    with open("lists.py") as file:
        print("File opened.")
        file.__exit__()
except (ValueError, ZeroDivisionError):
    print("You didn't entered a valid age.")
else:
    print('No exceptions were thrown.')
