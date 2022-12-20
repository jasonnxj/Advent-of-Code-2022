#size of marker
N = 14

def main():
    with open('input6.txt') as f:
        text = f.readlines()[0]
        marker = []
        count = 0
        for i in text:
            if count < N:
                marker.append(i)
            else:                                             #len(marker) = 4
                if len(set(marker)) == N:
                    print(marker, count)
                    return 1
                else:
                    marker.pop(0)
                    marker.append(i)
            count += 1
main()