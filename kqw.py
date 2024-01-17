def spam(quatro):
    try:
        return 42 / quatro
    except ZeroDivisionError:
        print("minha pomba")
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

