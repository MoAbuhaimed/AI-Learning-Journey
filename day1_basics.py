print("Hello, World")
print("Hello \"World\"")

# Asking for name and say Hello
name = input("What is your name? ")
# say Hello
# 1
print("Hello, " + name)
# 2
print("Hello," , name)
# 3
print(f"Hello, {name}")
# 4
print("Hello, ",end="")
print(name)
# 5
print("hello, ",name,sep="##")