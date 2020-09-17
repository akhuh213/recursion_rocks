# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

word ="cat"

def reverse(string, result=""):
    # Write code here
    string1 = list(string)
    print(string1)
    last_str = string1.pop()
    result = result + last_str
    print('hello {}'.format(result))
    if len(string1) == 0:
        return result
    return reverse("".join(string1), result)

print(reverse(word))


# print(reverse("")) 
# => ""
# print(reverse("a")) 
# => "a"
# print(reverse("ab")) 
# => "ba"
# print(reverse("computer")) 
# => "retupmoc"
# print(reverse(reverse("computer"))) 
# => "computer"

