from functions import createCypher


def main():
    input("\nThis is a Caesar cypher. Click enter and ¡good luck!\n")
    # Example usage of createCypher
    character_displacement = int(input("Enter the displacement for the Caesar cipher: "))
    cipher_function = createCypher(character_displacement)

    while True:
        message = input("\nEnter a new message to cipher (or enter to quit): ")

        if message == '':
            break
        
        encrypted_message = cipher_function(message)
        print(f"Encrypted message: {encrypted_message}")

if __name__ == "__main__":
    main()