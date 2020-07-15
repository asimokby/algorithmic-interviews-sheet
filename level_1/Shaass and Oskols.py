def solve():
    n = int(input())
    wires = list(map(int, input().split()))
    shots = int(input())
    for shot in range(shots):
        wire_idx, bird_idx = map(int, input().split()) 

        if wire_idx - 1 != 0:
            wires[wire_idx - 2] += bird_idx - 1 # left
        if wire_idx  != n:
            wires[wire_idx] += wires[wire_idx - 1] - bird_idx #right
        wires[wire_idx - 1] = 0

    for out in wires:
        print(out)
solve()
