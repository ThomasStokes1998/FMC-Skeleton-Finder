import numpy as np
import matplotlib.pyplot as plt


class Cube:
    def __init__(self, colours=("white", "orange", "green", "red", "blue", "yellow")):
        # Move dictionary
        self.movedict = {
            "":{
                "corners":[x for x in range(24)], "edges":[x for x in range(24)], "centers":[0, 1, 2, 3, 4, 5]
            },
            # Outer Layer Turns
            "L":{
                "corners":[18, 1, 2, 17, 7, 4, 5, 6, 0, 9, 10, 3, 12, 13, 14, 15, 16, 23, 20, 19, 8, 21, 22, 11],
                "edges":[0, 1, 2, 17, 7, 4, 5, 6, 8, 9, 10, 3, 12, 13, 14, 15, 16, 23, 18, 19, 20, 21, 22, 11],
                "centers":[0, 1, 2, 3, 4, 5]
            },
            "L'":{
                "corners":[8, 1, 2, 11, 5, 6, 7, 4, 20, 9, 10, 23, 12, 13, 14, 15, 16, 3, 0, 19, 18, 21, 22, 17],
                "edges":[0, 1, 2, 11, 5, 6, 7, 4, 8, 9, 10, 23, 12, 13, 14, 15, 16, 3, 18, 19, 20, 21, 22, 17],
                "centers":[0, 1, 2, 3, 4, 5]
            },
            "L2":{
                "corners":[20, 1, 2, 23, 6, 7, 4, 5, 18, 9, 10, 17, 12, 13, 14, 15, 16, 11, 8, 19, 0, 21, 22, 3],
                "edges":[0, 1, 2, 23, 6, 7, 4, 5, 8, 9, 10, 17, 12, 13, 14, 15, 16, 11, 18, 19, 20, 21, 22, 3],
                "centers":[0, 1, 2, 3, 4, 5]
            },
            "R":{
                "corners":[0, 9, 10, 3, 4, 5, 6, 7, 8, 21, 22, 11, 15, 12, 13, 14, 2, 17, 18, 1, 20, 19, 16, 23],
                "edges":[0, 9, 2, 3, 4, 5, 6, 7, 8, 21, 10, 11, 15, 12, 13, 14, 16, 17, 18, 1, 20, 19, 22, 23],
                "centers":[0, 1, 2, 3, 4, 5]
            },
            "R'":{
                "corners":[0, 19, 16, 3, 4, 5, 6, 7, 8, 1, 2, 11, 13, 14, 15, 12, 22, 17, 18, 21, 20, 9, 10, 23],
                "edges":[0, 19, 2, 3, 4, 5, 6, 7, 8, 1, 10, 11, 13, 14, 15, 12, 16, 17, 18, 21, 20, 9, 22, 23],
                "centers":[0, 1, 2, 3, 4, 5]
            },
            "R2":{
                "corners":[0, 21, 22, 3, 4, 5, 6, 7, 8, 19, 16, 11, 14, 15, 12, 13, 10, 17, 18, 9, 20, 1, 2, 23],
                "edges":[0, 21, 2, 3, 4, 5, 6, 7, 8, 19, 10, 11, 14, 15, 12, 13, 16, 17, 18, 9, 20, 1, 22, 23],
                "centers":[0, 1, 2, 3, 4, 5]
            },
            "U":{
                "corners":[3, 0, 1, 2, 8, 9, 6, 7, 12, 13, 10, 11, 16, 17, 14, 15, 4, 5, 18, 19, 20, 21, 22, 23],
                "edges":[3, 0, 1, 2, 8, 5, 6, 7, 12, 9, 10, 11, 16, 13, 14, 15, 4, 17, 18, 19, 20, 21, 22, 23],
                "centers":[0, 1, 2, 3, 4, 5]
            },
            "U'":{
                "corners":[1, 2, 3, 0, 16, 17, 6, 7, 4, 5, 10, 11, 8, 9, 14, 15, 12, 13, 18, 19, 20, 21, 22, 23],
                "edges":[1, 2, 3, 0, 16, 5, 6, 7, 4, 9, 10, 11, 8, 13, 14, 15, 12, 17, 18, 19, 20, 21, 22, 23],
                "centers":[0, 1, 2, 3, 4, 5]
            },
            "U2":{
                "corners":[2, 3, 0, 1, 12, 13, 6, 7, 16, 17, 10, 11, 4, 5, 14, 15, 8, 9, 18, 19, 20, 21, 22, 23],
                "edges":[2, 3, 0, 1, 12, 5, 6, 7, 16, 9, 10, 11, 4, 13, 14, 15, 8, 17, 18, 19, 20 , 21, 22, 23],
                "centers":[0, 1, 2, 3, 4, 5]
            },
            "D":{
                "corners":[0, 1, 2, 3, 4, 5, 18, 19, 8, 9, 6, 7, 12, 13, 10, 11, 16, 17, 14, 15, 23, 20, 21, 22],
                "edges":[0, 1, 2, 3, 4, 5, 18, 7, 8, 9, 6, 11, 12, 13, 10, 15, 16, 17, 14, 19, 23, 20, 21, 22],
                "centers":[0, 1, 2, 3, 4, 5]
            },
            "D'":{
                "corners":[0, 1, 2, 3, 4, 5, 10, 11, 8, 9, 14, 15, 12, 13, 18, 19, 16, 17, 6, 7, 21, 22, 23, 20],
                "edges":[0, 1, 2, 3, 4, 5, 10, 7, 8, 9, 14, 11, 12, 13, 18, 15, 16, 17, 6, 19, 21, 22, 23, 20],
                "centers":[0, 1, 2, 3, 4, 5]
            },
            "D2":{
                "corners":[0, 1, 2, 3, 4, 5, 14, 15, 8, 9, 18, 19, 12, 13, 6, 7, 16, 17, 10, 11, 22, 23, 20, 21],
                "edges":[0, 1, 2, 3, 4, 5, 14, 7, 8, 9, 18, 11, 12, 13, 6, 15, 16, 17, 10, 19, 22, 23, 20, 21],
                "centers":[0, 1, 2, 3, 4, 5]
            },
            "F":{
                "corners":[0, 1, 5, 6, 4, 20, 21, 7, 11, 8, 9, 10, 3, 13, 14, 2, 16, 17, 18, 19, 15, 12, 22, 23],
                "edges":[0, 1, 5, 3, 4, 20, 6, 7, 11, 8, 9, 10, 12, 13, 14, 2, 16, 17, 18, 19, 15, 21, 22, 23],
                "centers":[0, 1, 2, 3, 4, 5]
            },
            "F'":{
                "corners":[0, 1, 15, 12, 4, 2, 3, 7, 9, 10, 11, 8, 21, 13, 14, 20, 16, 17, 18, 19, 5, 6, 22, 23],
                "edges":[0, 1, 15, 3, 4, 2, 6, 7, 9, 10, 11, 8, 12, 13, 14, 20, 16, 17, 18, 19, 5, 21, 22, 23],
                "centers":[0, 1, 2, 3, 4, 5]
            },
            "F2":{
                "corners":[0, 1, 20, 21, 4, 15, 12, 7, 10, 11, 8, 9, 6, 13, 14, 5, 16, 17, 18, 19, 2, 3, 22, 23],
                "edges":[0, 1, 20, 3, 4, 15, 6, 7, 10, 11, 8, 9, 12, 13, 14, 5, 16, 17, 18, 19, 2, 21, 22, 23],
                "centers":[0, 1, 2, 3, 4, 5]
            },
            "B":{
                "corners":[13, 14, 2, 3, 1, 5, 6, 0, 8, 9, 10, 11, 12, 22, 23, 15, 19, 16, 17, 18, 20, 21, 7, 4],
                "edges":[13, 1, 2, 3, 4, 5, 6, 0, 8, 9, 10, 11, 12, 22, 14, 15, 19, 16, 17, 18, 20, 21, 7, 23],
                "centers":[0, 1, 2, 3, 4, 5]
            },
            "B'":{
                "corners":[7, 4, 2, 3, 23, 5, 6, 22, 8, 9, 10, 11, 12, 0, 1, 15, 17, 18, 19, 16, 20, 21, 13, 14],
                "edges":[7, 1, 2, 3, 4, 5, 6, 22, 8, 9, 10, 11, 12, 0, 14, 15, 17, 18, 19, 16, 20, 21, 13, 23],
                "centers":[0, 1, 2, 3, 4, 5]
            },
            "B2":{
                "corners":[22, 23, 2, 3, 14, 5, 6, 13, 8, 9, 10, 11, 12, 7, 4, 15, 18, 19, 16, 17, 20, 21, 0, 1],
                "edges":[22, 1, 2, 3, 4, 5, 6, 13, 8, 9, 10, 11, 12, 7, 14, 15, 18, 19, 16, 17, 20, 21, 0, 23],
                "centers":[0, 1, 2, 3, 4, 5]
            },
            # Middle Layer Turns
            "M":{
                "corners":[x for x in range(24)],
                "edges":[18, 1, 16, 3, 4, 5, 6, 7, 0, 9, 2, 11, 12, 13, 14, 15, 22, 17, 20, 19, 8, 21, 10, 23],
                "centers":[4, 1, 0, 3, 5, 2]
            },
            "M'":{
                "corners":[x for x in range(24)],
                "edges":[8, 1, 10, 3, 4, 5, 6, 7, 20, 9, 22, 11, 12, 13, 14, 15, 2, 17, 0, 19, 18, 21, 16, 23],
                "centers":[2, 1, 5, 3, 0, 4]
            },
            "M2":{
                "corners":[x for x in range(24)],
                "edges":[20, 1, 22, 3, 4, 5, 6, 7, 18, 9, 16, 11, 12, 13, 14, 15, 10, 17, 8, 19, 0, 21, 2, 23],
                "centers":[5, 1, 4, 3, 2, 0]
            },
            "E":{
                "corners":[x for x in range(24)],
                "edges":[0, 1, 2, 3, 4, 17, 6, 19, 8, 5, 10, 7, 12, 9, 14, 11, 16, 13, 18, 15, 20, 21, 22, 23],
                "centers":[0, 4, 1, 2, 3, 5]
            },
            "E'":{
                "corners":[x for x in range(24)],
                "edges":[0, 1, 2, 3, 4, 9, 6, 11, 8, 13, 10, 15, 12, 17, 14, 19, 16, 5, 18, 7, 20, 21, 22, 23],
                "centers":[0, 2, 3, 4, 1, 5]
            },
            "E2":{
                "corners":[x for x in range(24)],
                "edges":[0, 1, 2, 3, 4, 13, 6, 15, 8, 17, 10, 19, 12, 5, 14, 7, 16, 9, 18, 11, 20, 21, 22, 23],
                "centers":[0, 3, 4, 1, 2, 5]
            },
            "S":{
                "corners":[x for x in range(24)],
                "edges":[0, 4, 2, 6, 23, 5, 21, 7, 8, 9, 10, 11, 3, 13, 1, 15, 16, 17, 18, 19, 20, 12, 22, 14],
                "centers":[1, 5, 2, 0, 4, 3]
            },
            "S'":{
                "corners":[x for x in range(24)],
                "edges":[0, 14, 2, 12, 1, 5, 3, 7, 8, 9, 10, 11, 21, 13, 23, 15, 16, 17, 18, 19, 20, 6, 22, 4],
                "centers":[3, 0, 2, 5, 4, 1]
            },
            "S2":{
                "corners":[x for x in range(24)],
                "edges":[0, 23, 2, 21, 14, 5, 12, 7, 8, 9, 10, 11, 6, 13, 4, 15, 16, 17, 18, 19, 20, 3, 22, 1],
                "corners":[5, 3, 2, 1, 4, 0]
            },
            # Wide Turns
            "Lw":{
                "corners":[18, 1, 2, 17, 7, 4, 5, 6, 0, 9, 10, 3, 12, 13, 14, 15, 16, 23, 20, 19, 8, 21, 22, 11],
                "edges":[18, 1, 16, 17, 7, 4, 5, 6, 0, 9, 2, 3, 12, 13, 14, 5, 20, 21, 22, 19, 8, 21, 10, 11],
                "centers":[4, 1, 0, 3, 5, 2]
            },
            "Lw'":{
                "corners":[8, 1, 2, 11, 5, 6, 7, 4, 20, 9, 10, 23, 12, 13, 14, 15, 16, 3, 0, 19, 18, 21, 22, 17],
                "edges":[8, 1, 10, 11, 5, 6, 7, 4, 20, 9, 22, 23, 12, 13, 14, 15, 2, 3, 1, 19, 18, 21, 16, 17],
                "centers":[2, 1, 5, 3, 0, 4]
            },
            "Lw2":{
                "corners":[20, 1, 2, 23, 6, 7, 4, 5, 18, 9, 10, 17, 12, 13, 14, 15, 16, 11, 8, 19, 0, 21, 22, 3],
                "edges":[20, 1, 22, 23, 6, 7, 4, 5, 18, 9, 16, 17, 12, 13, 14, 15, 10, 11, 8, 19, 0, 21, 2, 3],
                "centers":[5, 1, 4, 3, 2, 0]
            },
            "Rw":{
                "corners":[0, 9, 10, 3, 4, 5, 6, 7, 8, 21, 22, 11, 15, 12, 13, 14, 2, 17, 18, 1, 20, 19, 16, 23],
                "edges":[8, 9, 10, 3, 4, 5, 6, 7, 20, 21, 22, 11, 15, 12, 13, 14, 2, 17, 0, 1, 18, 19, 16, 23],
                "centers":[2, 1, 5, 3, 0, 4]
            },
            "Rw'":{
                "corners":[0, 19, 16, 3, 4, 5, 6, 7, 8, 1, 2, 11, 13, 14, 15, 12, 22, 17, 18, 21, 20, 9, 10, 23],
                "edges":[18, 19, 16, 3, 4, 5, 6, 7, 0, 1, 2, 11, 13, 14, 15, 12, 20, 17, 22, 23, 8, 9, 10, 23],
                "centers":[4, 1, 0, 3, 5, 2]
            },
            "Rw2":{
                "corners":[0, 21, 22, 3, 4, 5, 6, 7, 8, 19, 16, 11, 14, 15, 12, 13, 10, 17, 18, 9, 20, 1, 2, 23],
                "edges":[23, 21, 20, 3, 4, 5, 6, 7, 18, 19, 16, 11, 14, 15, 12, 13, 10, 17, 8, 9, 0, 1, 2, 23],
                "centers":[5, 1, 4, 3, 2, 0]
            },
            "Uw":{
                "corners":[3, 0, 1, 2, 8, 9, 6, 7, 12, 13, 10, 11, 16, 17, 14, 15, 4, 5, 18, 19, 20, 21, 22, 23],
                "edges":[3, 0, 1, 2, 8, 9, 6, 11, 12, 13, 10, 15, 16, 17, 14, 19, 4, 5, 18, 7, 20, 21, 22, 23],
                "centers":[0, 2, 3, 4, 1, 5]
            },
            "Uw'":{
                "corners":[1, 2, 3, 0, 16, 17, 6, 7, 4, 5, 10, 11, 8, 9, 14, 15, 12, 13, 18, 19, 20, 21, 22, 23],
                "edges":[1, 2, 3, 0, 16, 17, 6, 19, 4, 5, 10, 7, 8, 9, 14, 11, 12, 13, 18, 15, 20, 21, 22, 23],
                "centers":[0, 4, 1, 2, 3, 5]
            },
            "Uw2":{
                "corners":[2, 3, 0, 1, 12, 13, 6, 7, 16, 17, 10, 11, 4, 5, 14, 15, 8, 9, 18, 19, 20, 21, 22, 23],
                "edges":[2, 3, 0, 1, 12, 13, 6, 15, 16, 17, 10, 19, 4, 5, 14, 7, 8, 9, 18, 11, 20, 21, 22, 23],
                "centers":[0, 3, 4, 1, 2, 5]
            },
            "Dw":{
                "corners":[0, 1, 2, 3, 4, 5, 18, 19, 8, 9, 6, 7, 12, 13, 10, 11, 16, 17, 14, 15, 23, 20, 21, 22],
                "edges":[0, 1, 2, 3, 4, 17, 18, 19, 8, 5, 6, 7, 12, 9, 10, 11, 16, 13, 14, 15, 23, 20, 21, 22],
                "centers":[0, 4, 1, 2, 3, 5]
            },
            "Dw'":{
                "corners":[0, 1, 2, 3, 4, 5, 10, 11, 8, 9, 14, 15, 12, 13, 18, 19, 16, 17, 6, 7, 21, 22, 23, 20],
                "edges":[0, 1, 2, 3, 4, 9, 10, 11, 8, 13, 14, 15, 12, 17, 18, 19, 16, 5, 6, 7, 21, 22, 23, 20],
                "centers":[0, 2, 3, 4, 1, 5]
            },
            "Dw2":{
                "corners":[0, 1, 2, 3, 4, 5, 14, 15, 8, 9, 18, 19, 12, 13, 6, 7, 16, 17, 10, 11, 22, 23, 20, 21],
                "edges":[0, 1, 2, 3, 4, 13, 14, 15, 8, 17, 18, 19, 12, 5, 6, 7, 16, 9, 10, 11, 22, 23, 20, 21],
                "centers":[0, 3, 4, 1, 2, 5]
            },
            "Fw":{
                "corners":[0, 1, 5, 6, 4, 20, 21, 7, 11, 8, 9, 10, 3, 13, 14, 2, 16, 17, 18, 19, 15, 12, 22, 23],
                "edges":[0, 4, 5, 6, 20, 21, 22, 7, 11, 8, 9, 10, 0, 13, 2, 3, 16, 17, 18, 19, 15, 12, 22, 14],
                "centers":[1, 5, 2, 0, 4, 3]
            },
            "Fw'":{
                "corners":[0, 1, 15, 12, 4, 2, 3, 7, 9, 10, 11, 8, 21, 13, 14, 20, 16, 17, 18, 19, 5, 6, 22, 23],
                "edges":[0, 14, 15, 12, 0, 1, 2, 7, 9, 10, 11, 8, 21, 15, 23, 20, 16, 17, 18, 19, 5, 6, 22, 4],
                "centers":[3, 0, 2, 5, 4, 1]
            },
            "Fw2":{
                "corners":[0, 1, 20, 21, 4, 15, 12, 7, 10, 11, 8, 9, 6, 13, 14, 5, 16, 17, 18, 19, 2, 3, 22, 23],
                "edges":[0, 23, 20, 21, 14, 15, 12, 7, 10, 11, 8, 9, 6, 13, 4, 5, 16, 17, 18, 19, 0, 1, 22, 3],
                "centers":[5, 3, 2, 1, 4, 0]
            },
            "Bw":{
                "corners":[13, 14, 2, 3, 1, 5, 6, 0, 8, 9, 10, 11, 12, 22, 23, 15, 19, 16, 17, 18, 20, 21, 7, 4],
                "edges":[13, 14, 2, 12, 0, 5, 2, 3, 8, 9, 10, 11, 21, 22, 23, 15, 19, 16, 17, 18, 20, 6, 7, 4],
                "centers":[3, 0, 2, 5, 4, 1]
            },
            "Bw'":{
                "corners":[7, 4, 2, 3, 23, 5, 6, 22, 8, 9, 10, 11, 12, 0, 1, 15, 17, 18, 19, 16, 20, 21, 13, 14],
                "edges":[7, 4, 2, 6, 20, 5, 22, 23, 8, 9, 10, 11, 0, 1, 2, 15, 17, 18, 19, 16, 20, 12, 13, 14],
                "centers":[1, 5, 2, 0, 4, 3]
            },
            "Bw2":{
                "corners":[22, 23, 2, 3, 14, 5, 6, 13, 8, 9, 10, 11, 12, 7, 4, 15, 18, 19, 16, 17, 20, 21, 0, 1],
                "edges":[22, 23, 2, 21, 14, 5, 12, 13, 8, 9, 10, 11, 6, 7, 4, 15, 18, 19, 16, 17, 20, 3, 0, 1],
                "centers":[5, 3, 2, 1, 4, 0]
            },
            # Rotations
            "x":{
                "corners":[8, 9, 10, 11, 5, 6, 7, 4, 20, 21, 22, 23, 15, 12, 13, 14, 2, 3, 0, 1, 18, 19, 16, 17],
                "edges":[8, 9, 10, 11, 5, 6, 7, 4, 20, 21, 22, 23, 15, 12, 13, 14, 2, 3, 0, 1, 18, 19, 16, 17],
                "centers":[2, 1, 5, 3, 0, 4]
            },
            "x'":{
                "corners":[18, 19, 16, 17, 7, 4, 5, 6, 0, 1, 2, 3, 13, 14, 15, 12, 22, 23, 20, 21, 8, 9, 10, 11],
                "edges":[18, 19, 16, 17, 7, 4, 5, 6, 0, 1, 2, 3, 13, 14, 15, 12, 22, 23, 20, 21, 8, 9, 10, 11],
                "centers":[4, 1, 0, 3, 5, 2]
            },
            "x2":{
                "corners":[20, 21, 22, 23, 6, 7, 4, 5, 18, 19, 16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 0, 1, 2, 3],
                "edges":[20, 21, 22, 23, 6, 7, 4, 5, 18, 19, 16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 0, 1, 2, 3],
                "centers":[5, 1, 4, 3, 2, 0]
            },
            "y":{
                "corners":[3, 0, 1, 2, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 4, 5, 6, 7, 21, 22, 23, 20],
                "edges":[3, 0, 1, 2, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 4, 5, 6, 7, 21, 22, 23, 20],
                "centers":[0, 2, 3, 4, 1, 5]
            },
            "y'":{
                "corners":[1, 2, 3, 0, 16, 17, 18, 19, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 23, 20, 21, 22],
                "edges":[1, 2, 3, 0, 16, 17, 18, 19, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 23, 20, 21, 22],
                "centers":[0, 4, 1, 2, 3, 5]
            },
            "y2":{
                "corners":[2, 3, 0, 1, 12, 13, 14, 15, 16, 17, 18, 19, 4, 5, 6, 7, 8, 9, 10, 11, 22, 23, 20, 21],
                "edges":[2, 3, 0, 1, 12, 13, 14, 15, 16, 17, 18, 19, 4, 5, 6, 7, 8, 9, 10, 11, 22, 23, 20, 21],
                "centers":[0, 3, 4, 1, 2, 5]
            },
            "z":{
                "corners":[7, 4, 5, 6, 23, 20, 21, 22, 11, 8, 9, 10, 3, 0, 1, 2, 17, 18, 19, 16, 15, 12, 13, 14],
                "edges":[7, 4, 5, 6, 23, 20, 21, 22, 11, 8, 9, 10, 3, 0, 1, 2, 17, 18, 19, 16, 15, 12, 13, 14],
                "centers":[1, 5, 2, 0, 4, 3]
            },
            "z'":{
                "corners":[13, 14, 15, 12, 1, 2, 3, 0, 9, 10, 11, 8, 21, 22, 23, 20, 19, 16, 17, 18, 5, 6, 7, 4],
                "edges":[13, 14, 15, 12, 1, 2, 3, 0, 9, 10, 11, 8, 21, 22, 23, 20, 19, 16, 17, 18, 5, 6, 7, 4],
                "centers":[3, 0, 2, 5, 4, 1]
            },
            "z2":{
                "corners":[22, 23, 20, 21, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 18, 19, 16, 17, 2, 3, 0, 1],
                "edges":[22, 23, 20, 21, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 18, 19, 16, 17, 2, 3, 0, 1],
                "centers":[5, 3, 2, 1, 4, 0]
            }
        }
        # Different Individual Moves and Rotations
        self.poss_moves = ["U", "U'", "U2", "L", "L'", "L2", "F", "F'", "F2", "R", "R'", "R2", "B", "B'", "B2", "D",
                           "D'", "D2", "Uw", "Uw'", "Uw2", "Lw", "Lw'", "Lw2", "Fw", "Fw'", "Fw2", "Rw", "Rw'", "Rw2",
                           "Bw", "Bw'", "Bw2", "Dw", "Dw'", "Dw2", "M", "M'", "M2", "E", "E'", "E2", "S", "S'", "S2"]
        self.rotations = ["", "x", "x'", "x2", "y", "y'", "y2", "z", "z'", "z2", "xy", "xy2", "xy'", "x'y", "x'y'",
                          "x'y2", "x2y", "x2y'", "xz", "xz'", "x'z", "x'z'", "x2z", "x2z'"]
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        # Colours
        if len(colours) != 6:
            print("Must name exactly 6 colours! Display features will not work!")
        else:
            self.colour = colours

    # Functions
    # Turning the cube
    def turn(self, move, state=None):
        if state is None:
            state = self.movedict[""]
        new = {}
        for type in state:
            swaps = move[type]
            pieces = state[type]
            new[type] = []
            for s in swaps:
                new[type].append(pieces[s])
        return new

    # Recovers a move
    def move(self, x):
        if x in self.movedict:
            return self.movedict[x]
        else:
            print(f"Move not in dictionary: {x}")
            return self.movedict[""]

    # Converts a string of moves into a list with their individual moves
    def qtm(self, turns: str) -> list:
        movelist = []
        m = ""
        for t in turns:
            if t != " ":
                if t in ["'", "2", "w"]:
                        m += t
                else:
                    if len(m) > 0:
                        movelist.append(m)
                    m = t
        movelist.append(m)
        return movelist

    # Return all unique character strings of a given length
    def combo(self, x, depth=1, cube=True):
        y = x
        while depth != 1:
            z = []
            for a in y:
                for b in x:
                    if cube:
                        if len(b) == 1:
                            if a[-1] in ["'", '2'] and b != a[-2]:
                                z.append(a + b)
                            elif a[-1] not in ["'", '2'] and b != a[-1]:
                                z.append(a + b)
                        else:
                            if a[-1] in ["'", '2'] and b[0] != a[-2]:
                                z.append(a + b)
                            elif a[-1] not in ["'", '2'] and b[0] != a[-1]:
                                z.append(a + b)
                    else:
                        if b != a[-1]:
                            z.append(a + b)
            y = z
            depth -= 1
            if depth == 1:
                break
        return y

    # Generates a scramble of an arbitrary length
    def scramble(self, length=25):
        s = ""
        l = 0
        ns = []
        while l < length:
            n = np.random.randint(0, 18, 1)[0]
            m = self.poss_moves[n]
            if l == 0:
                s += m
                ns.append(n)
                l += 1
            elif l == 1:
                # Ensures the current move does not cancel with the previous move
                if ns[0] // 3 != n // 3:
                    s += m
                    ns.append(n)
                    l += 1
            # Ensures no simplifications from previous two moves
            elif ns[l - 1] // 3 != n // 3 and ns[l - 2] // 3 != n // 3:
                s += m
                ns.append(n)
                l += 1
        return s

    # Inverts a scramble
    def invertScramble(self, scramble: str) -> str:
        inv = ""
        qscramble = self.qtm(scramble)
        for i in range(len(qscramble)):
            s = qscramble[-i - 1]
            if "'" in s:
                inv += s[0]
            elif len(s) == 1:
                inv += s + "'"
            else:
                inv += s
        return inv

    # Encodes a scramble
    def encodeScramble(self, scramble: str) -> str:
        ms = self.move_sim(scramble)
        e = ""
        for s in ms:
            for x in ms[s]:
                e += self.letters[x]
        return e
    # Decodes an encoded scramble
    def decodeScramble(self, encoding: str) -> dict:
        state = {"corners":[],"edges":[],"centers":[]}
        for i, e in enumerate(encoding):
            for j, l in enumerate(self.letters):
                    if l == e:
                        if i < 24:
                            state["corners"].append(j)
                            break
                        elif i < 48:
                            state["edges"].append(j)
                            break
                        else:
                            state["centers"].append(j)
                            break
        return state
    # Calculates the final state for an input scramble
    def move_sim(self, scramble: str, state=None):
        if state is None:
            state = self.movedict[""]
        s = state
        q = self.qtm(scramble)
        for x in q:
            m = self.move(x)
            s = self.turn(m, s)
        return s
        

    # Graphing the Cube
    # Colours
    def colours(self, n: int) -> str:
        return self.colour[n // 4]

    # Coords
    def coord(self, state):
        info = []
        cor = state["corners"]
        edg = state["edges"]
        sen = state["centers"]
        for i in range(24):
            colc = Cube().colours(cor[i])
            cole = Cube().colours(edg[i])
            cols = Cube().colours(4 * sen[i//4])
            # Up
            if i == 0:
                info.append([-3 / 2, 0, cols])
                info.append([-4 / 2, -1 / 2, colc])
                info.append([-4 / 2, 0, cole])
            if i == 1:
                info.append([-4 / 2, 1 / 2, colc])
                info.append([-3 / 2, 1 / 2, cole])
            if i == 2:
                info.append([-2 / 2, 1 / 2, colc])
                info.append([-2 / 2, 0, cole])
            if i == 3:
                info.append([-2 / 2, -1 / 2, colc])
                info.append([-3 / 2, -1 / 2, cole])
            # Left
            if i == 4:
                info.append([0, -3 / 2, cols])
                info.append([-1 / 2, -4 / 2, colc])
                info.append([-1 / 2, -3 / 2, cole])
            if i == 5:
                info.append([-1 / 2, -2 / 2, colc])
                info.append([0, -2 / 2, cole])
            if i == 6:
                info.append([1 / 2, -2 / 2, colc])
                info.append([1 / 2, -3 / 2, cole])
            if i == 7:
                info.append([1 / 2, -4 / 2, colc])
                info.append([0, -4 / 2, cole])
            # Front
            if i == 8:
                info.append([0, 0, cols])
                info.append([-1 / 2, -1 / 2, colc])
                info.append([-1 / 2, 0, cole])
            if i == 9:
                info.append([-1 / 2, 1 / 2, colc])
                info.append([0, 1 / 2, cole])
            if i == 10:
                info.append([1 / 2, 1 / 2, colc])
                info.append([1 / 2, 0, cole])
            if i == 11:
                info.append([1 / 2, -1 / 2, colc])
                info.append([0, -1 / 2, cole])
            # Right
            if i == 12:
                info.append([0, 3 / 2, cols])
                info.append([-1 / 2, 2 / 2, colc])
                info.append([-1 / 2, 3 / 2, cole])
            if i == 13:
                info.append([-1 / 2, 4 / 2, colc])
                info.append([0, 4 / 2, cole])
            if i == 14:
                info.append([1 / 2, 4 / 2, colc])
                info.append([1 / 2, 3 / 2, cole])
            if i == 15:
                info.append([1 / 2, 2 / 2, colc])
                info.append([0, 2 / 2, cole])
            # Back
            if i == 16:
                info.append([6 / 2, 0, cols])
                info.append([7 / 2, 1 / 2, colc])
                info.append([7 / 2, 0, cole])
            if i == 17:
                info.append([7 / 2, -1 / 2, colc])
                info.append([6 / 2, -1 / 2, cole])
            if i == 18:
                info.append([5 / 2, -1 / 2, colc])
                info.append([5 / 2, 0, cole])
            if i == 19:
                info.append([5 / 2, 1 / 2, colc])
                info.append([6 / 2, 1 / 2, cole])
            # Down
            if i == 20:
                info.append([3 / 2, 0, cols])
                info.append([2 / 2, -1 / 2, colc])
                info.append([2 / 2, 0 / 2, cole])
            if i == 21:
                info.append([2 / 2, 1 / 2, colc])
                info.append([3 / 2, 1 / 2, cole])
            if i == 22:
                info.append([4 / 2, 1 / 2, colc])
                info.append([4 / 2, 0, cole])
            if i == 23:
                info.append([4 / 2, -1 / 2, colc])
                info.append([3 / 2, -1 / 2, cole])
        return info

    # Visualises a given sequence of moves
    def viscube(self, scramble: str, size=400, style="dark_background"):
        ms = Cube().move_sim(scramble)
        I = Cube().coord(ms)
        for c in self.colour:
            X = []
            Y = []
            for i in I:
                if c in i:
                    X.append(i[0])
                    Y.append(i[1])
            plt.style.use(style)
            plt.scatter(X, Y, color=c, linewidths=10, s=size, marker="s")
        plt.xlabel('Moves:' + scramble)
        plt.title("Rubik's Cube")
        plt.show()


# Test Visualisation
if __name__ == "__main__":
    rc = Cube()
    rc.viscube("R2L2U'BL'UB'FL'D2R'LD2B'L'U'RL'DUB2DU2DU2DU2B2DRU2")