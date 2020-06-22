n = int(input())
result = ''


def rec(n, result):
    q, mod = divmod(n, 26)

    if q == 0:
        if mod != 0:
            result += chr(mod + 96)
        return result

    if mod == 0:
        result += 'z'
        q = q - 1
    else:
        result += chr(mod + 96)

    n = q
    return rec(n, result)


result = rec(n, result)
print(result[::-1])
