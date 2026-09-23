def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

if __name__ == "__main__":
    greetings('Alexandra')
    greetings('Wil')
    greetings()
    greetings(42)