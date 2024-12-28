def ReplacementInsertion(replacement_string, original_string, offset, length):

    left_string = original_string[:offset]
    right_string = original_string[offset+length:]


    # return (left_string, replacement, right_string) 
    return left_string + replacement_string + right_string


replacement = 'cold'

original_string = "Hello, world!"
substring = "world"

index = original_string.find(substring)

if index != -1:
    print(f"'{substring}' found at index {index}")
else:
    print(f"'{substring}' not found")


print(ReplacementInsertion(replacement, original_string, index, length=5))



