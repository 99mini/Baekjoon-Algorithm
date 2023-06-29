a = [
        [
            [0,0,1],
            [1,0,0]
        ],
        [
            [0,0,1],
            [1,0,0]
        ]
    ]

r = True
for h in a:
    r &= any(-1 in e for e in h)

print(r)