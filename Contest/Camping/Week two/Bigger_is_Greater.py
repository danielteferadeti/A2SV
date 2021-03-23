def biggerIsGreater(w):
    w = list(w)
    arr = []
    index = -1
    for i in range(len(w)-1,0,-1):
        arr.append(w[i])
        if ord(w[i]) > ord(w[i-1]):
            print(w[i-1],w[i])
            index = i
            arr =  sorted(arr)
            for j in range(len(arr)):
                val = arr[j]
                if ord(w[i-1]) < ord(val):
                    arr[j] = w[i-1]
                    w[i-1] = val
                    break
            break
    if index == -1:
        return "no answer"

    res = ""
    for i in range(index):
        res += w[i]
    for j in range(len(arr)):
        res += arr[j]
    return res
