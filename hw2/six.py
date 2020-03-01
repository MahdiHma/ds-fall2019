joel = 0
ellie = 0


def mergeSort(arr):
    global joel
    global ellie
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = L[i]
                joel += L[i] * j
                ellie += L[i] * (len(R) - j)
                i += 1
                k += 1


            elif L[i] < R[j]:
                arr[k] = R[j]
                ellie += R[j] * i
                joel += R[j] * (len(L) - i)

                j += 1
                k += 1

            else:
                count_r = 0
                f_i = i
                f_j = j
                count_l = 0
                eq = L[i]
                while i < len(L) and L[i] == eq:
                    count_l += 1
                    arr[k] = L[i]
                    k += 1
                    i += 1
                while j < len(R) and R[j] == eq:
                    count_r += 1
                    arr[k] = R[j]
                    k += 1
                    j += 1
                ellie += count_r * count_l * eq + eq * (len(R) - j) * count_l + count_r * eq * f_i
                joel += count_r * count_l * eq + eq * (len(L) - i) * count_r + count_l * f_j * eq

        while j < len(R):
            arr[k] = R[j]
            ellie += R[j] * i
            joel += R[j] * (len(L) - i)
            j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            joel += L[i] * j
            ellie += L[i] * (len(R) - j)
            i += 1
            k += 1


n = int(input())
inp = input().split()
ls = list()
for i in range(n):
    ls.append(int(inp[i]))
mergeSort(ls)

if ellie > joel:
    print("Ellie")
    print(ellie)
if ellie == joel:
    print("draw")
    print(ellie)
if ellie < joel:
    print("Joel")
    print(joel)
