while True:
    try:
        age=int(input('Enter your age '))
        10/age
    except ValueError as er1:
        print(f"Enter a number, {er1}")
    except ZeroDivisionError as er2:
        print(f"Enter a number greater than zero, {er2}")
    else:
        print("thank you,now its easy to proceed")
        break       
    finally:
        print("good") 