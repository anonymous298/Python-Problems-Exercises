# from mypackage import module1, module2

# print(module1.adds(10, 10))
# print(module2.multiply(10, 10))

try: 
    import mypackage

    print(mypackage.adds(2,2))
    print(mypackage.multiply(2,2))

except Exception as e:
    print(e)