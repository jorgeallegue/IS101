def createCypher(character_displacement: int):
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ "

    def cipher(message: str):
        result = []
        alphabet_length = len(alphabet)

        for character in message.upper():
            if character in alphabet:
                original_index = alphabet.index(character)
                cyphered_index = (original_index + character_displacement) % alphabet_length
                result.append(alphabet[cyphered_index])
            else:
                result.append(character)
        
        return "".join(result)
    
    return cipher