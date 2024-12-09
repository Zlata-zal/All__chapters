def transform_strings(strings):
    L = len(strings)
    N = len(strings[0])
    result = ""

    for i in range(N):
        total = 0
        for string in strings:
            char = string[i]
            if char == " ":
                total += 0
            else:
                total += ord(char) - ord("a") + 1
        avg = total // L
        if avg == 0:
            result += " "
        else:
            result += chr(avg + ord("a") - 1)
    return result
s1 = "u lk zxuq hfk as fouh"
s2 = "y l zpuv xe at sicd"
s3 = "welvayfuqbfpeaauaqcrc"

strings = [s1, s2, s3]
result = transform_strings(strings)
print(result)
