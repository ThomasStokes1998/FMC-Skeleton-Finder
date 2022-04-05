from RubiksCube import Cube
import random

rc = Cube()
validmoves = rc.poss_moves[:18]

class Node:
    def __init__(self, moves: str, initstate: dict, priorprob: float):
        self.moves = moves
        self.initstate = initstate
        self.priorprob = priorprob
        self.vissincelastexp = 0
        self.nodestate = rc.move_sim(moves, self.initstate)
    
    def score(self) -> float:
        u = self.priorprob
        n = self.vissincelastexp
        return u + (1 - u) * (n / (2 + n))

class ScrambleSearch:
    def __init__(self, scramble: str, searches: int):
        self.scramble = scramble
        self.searches = searches
        self.initstate = rc.move_sim(self.scramble)
        self.nodes = {}
        self.validmoves = validmoves

    def formatInputs(self, state: dict) -> list:
        formattedinputs = []
        centres = state["centers"]
        # For making the neural network colour neutral
        centredict = {c:i for i, c in enumerate(centres)}
        for s in state:
            for x in state[s]:
                c = x // 4
                normcolour = centredict[c]
                # Formats colours as 1/7, 2/7,..., 6/7
                if s != "centers":
                    formattedinputs.append((1 + normcolour)/7)
        return formattedinputs
    
    def evalMoves(self, movelist: list):
        beststr = ""
        besteval = -5
        bestlen = 20
        bestpieces = 0
        _movelist = []
        movestr = ""
        for m, move in enumerate(movelist):
            movestr += move
            _movelist.append(move)
            state = rc.move_sim(movestr, self.initstate)
            # Find the number of solved pieces
            s = 0
            corners = state["corners"]
            for c in [0, 1, 2, 3, 20, 21, 22, 23]:
                if corners[c] == c:
                    s += 1
            
            edges = state["edges"]
            for e in [0, 1, 2, 3, 9, 11, 17, 19, 20, 21, 22, 23]:
                if edges[e] == e:
                    s += 1
            eval = (s - 5) / (m + 1)
            if bestpieces < s <= 5 or bestpieces <= 5 and bestpieces == s and bestlen > m + 1:
                beststr = movestr
                besteval = eval
                bestlen = m + 1
                bestpieces = s
            elif s > 5 and eval > besteval:
                beststr = movestr
                besteval = eval
                bestlen = m + 1
                bestpieces = s
        return besteval, beststr, bestlen, bestpieces

    # Runs through a decision tree to find the best move sequences according to the policy
    # Returns a dictionary with the training data from the search
    def search(self, policy, maxmoves: int=20, randsearch: bool = False, trackprog: bool=True, printfreq: int=100) -> dict:
        train_data = {"scrambles":[], "moves":[], "evals":[]}
        maxeval = -5
        maxlen = 20
        maxstr = ""
        maxpieces = 0
        for i in range(1, self.searches + 1):
            searchpath = ""
            lastmove = ""
            movehist = []
            currstate = self.initstate
            # Run down the tree
            for k in range(maxmoves):
                policyinput = self.formatInputs(currstate)
                priorprobs = policy.predict([policyinput])[0]
                # Find the next move to select
                maxmove = ""
                maxnode = searchpath
                maxscore = 0
                if randsearch:
                    nodescores = []
                # Loop through the nodes to find the highest scoring node
                for j, m in enumerate(self.validmoves):
                    # Ensures a different face is turned
                    if k == 0 or k > 0 and m[0] != lastmove[0]:
                        nodepath = searchpath + m
                        if nodepath not in self.nodes:
                            self.nodes[nodepath] = Node(nodepath, self.initstate, priorprobs[j])
                        nodescore = self.nodes[nodepath].score()
                        if randsearch:
                            nodescores.append(nodescore)
                        elif nodescore > maxscore:
                            maxmove = m
                            maxnode = nodepath
                            maxscore = nodescore
                # Find the move if random search enabled
                if randsearch:
                    r = random.uniform(0, sum(nodescores))
                    movesum = 0
                    for j, ns in enumerate(nodescore):
                        movesum += ns
                        if movesum > r:
                            maxmove = self.validmoves[j]
                            maxnode = searchpath + maxmove
                            break
                # Update the nodes
                for j, m in enumerate(self.validmoves):
                    if k == 0 or k > 0 and lastmove[0] != m[0]:
                        nodepath = searchpath + m
                        if m == maxmove:
                            self.nodes[nodepath].vissincelastexp = 0
                        else:
                            self.nodes[nodepath].vissincelastexp += 1
                searchpath = maxnode
                lastmove = maxmove
                movehist.append(maxmove)
                currstate = self.nodes[searchpath].nodestate
            # Finds the best sequence of moves from the search path
            besteval, beststr, bestlen, bestpieces = self.evalMoves(movehist)
            # Add to training data
            if besteval > maxeval >= 0 or maxpieces < bestpieces <= 5 or maxpieces == bestpieces and bestlen < maxlen:
                maxstr = beststr
                maxeval = besteval
                maxlen = bestlen
                maxpieces = bestpieces
            if besteval > 0:
                train_data["scrambles"].append(self.scramble)
                train_data["moves"].append(beststr)
                train_data["evals"].append(besteval)
            if trackprog and i % printfreq == 0:
                print(f"Completed {i} searches: best eval = {round(maxeval, 2)}: ({maxpieces}, {maxlen}) Moves: {maxstr}")
        # Print Result
        print(f"Finished searches: best eval = {round(maxeval, 2)}: ({maxpieces}, {maxlen}) Moves: {maxstr}")
        return train_data


if __name__ == "__main__":
    ss = ScrambleSearch("R2L2U'BL'UB'FL'D2R'LD2B'L'U'RL'DU", 1)
    ss.evalMoves(["B2","D","U2","D","U2","D","U2","B2","D","R","U2"])