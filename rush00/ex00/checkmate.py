def checkmate(board):
    try:

        if not isinstance(board, str):
            print("Error")
            return
        rows = []
        for line in board.splitlines():
            if len(line) > 0:
                rows.append(line)

        size = len(rows)
        if size == 0:
            print("Error")
            return
        for row in rows:
            if len(row) != size:
                print("Error")
                return
        kr = -1
        kc = -1
        king_count = 0
        for r in range(size):
            for c in range(size):
                if rows[r][c] == "K":
                    kr = r
                    kc = c
                    king_count = king_count + 1
        if king_count != 1:
            print("Error")
            return
        
        for r in range(size):
            for c in range(size):
                piece = rows[r][c]
                if piece == "P":
                    if r - 1 == kr and (c - 1 == kc or c + 1 == kc):
                        print("Success")
                        return
                    
                if piece == "R" or piece == "Q":
                    if r == kr:
                        blocked = False
                        start = min(c, kc) + 1
                        end = max(c, kc)
                        for col in range(start, end):
                            if rows[r][col] in "PBRQ":
                                blocked = True
                        if not blocked:
                            print("Success")
                            return
                        
                    if c == kc:
                        blocked = False
                        start = min(r, kr) + 1
                        end = max(r, kr)
                        for row in range(start, end):
                            if rows[row][c] in "PBRQ":
                                blocked = True
                        if not blocked:
                            print("Success")
                            return
                        
                if piece == "B" or piece == "Q":

                    dist_r = abs(kr - r)
                    dist_c = abs(kc - c)
                    if dist_r == dist_c and dist_r > 0:
                        if kr > r:
                            step_r = 1
                        else:
                            step_r = -1

                        if kc > c:
                            step_c = 1
                        else:
                            step_c = -1

                        blocked = False
                        for i in range(1, dist_r):
                            check_r = r + (i * step_r)
                            check_c = c + (i * step_c)
                            if rows[check_r][check_c] in "PBRQ":
                                blocked = True

                        if not blocked:
                            print("Success")
                            return

        print("Fail")

    except Exception:
        print("Error")
        return