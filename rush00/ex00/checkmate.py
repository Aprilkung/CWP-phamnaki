def checkmate(board):
    try:
        # 1. จัดการ String (หั่นเป็นบรรทัด กันปัญหาขึ้นบรรทัดใหม่ต่าง OS)
        rows = board.splitlines()
        height = len(rows)
        
        # ถ้าส่งกระดานว่างๆ มา
        if height == 0:
            return

        width = len(rows[0])
        king_pos = None
        king_count = 0

        # 2. Validate กระดาน (ต้องเป็นจัตุรัส) และหาพิกัด King
        for r in range(height):
            # เช็คว่าแต่ละบรรทัดยาวเท่ากันไหม (กันคนส่งทรงแปลกๆ หรือ Emoji ที่กินพื้นที่เกิน)
            if len(rows[r]) != width:
                return  
                
            for c in range(width):
                if rows[r][c] == 'K':
                    king_pos = (r, c)
                    king_count += 1
        
        # 3. Validate King (ต้องมีตัวเดียวเป๊ะๆ และกระดานต้องเป็นสี่เหลี่ยมจัตุรัส)
        if king_count != 1 or width != height:
            return 

        kr, kc = king_pos

        # 4. ฟังก์ชันยิงเรดาร์ (Raycasting) ออกจากตัว King
        def check_ray(dr, dc, attackers, check_pawn=False):
            r, c = kr + dr, kc + dc
            distance = 1
            
            # ยิงเรดาร์ไปเรื่อยๆ จนกว่าจะสุดขอบกระดาน
            while 0 <= r < height and 0 <= c < width:
                piece = rows[r][c]
                
                # ถ้าเจอ "หมาก" ของจริง (ตัวอักษรอื่นถือเป็นพื้นที่ว่าง เรดาร์ทะลุผ่าน)
                if piece in ['P', 'B', 'R', 'Q']:
                    
                    # ถ้าเป็นหมากศัตรูที่โจมตีในทิศนี้ได้
                    if piece in attackers:
                        return True
                        
                    # เช็คเงื่อนไขพิเศษสำหรับ Pawn (ตีทแยงลงมาได้แค่ในระยะ 1 ช่อง)
                    if check_pawn and distance == 1 and piece == 'P':
                        return True
                        
                    # ถ้าเจอหมากตัวอื่น (ที่โจมตีทิศนี้ไม่ได้) แปลว่ามัน "บัง" ทางเรดาร์อยู่
                    return False
                
                # ขยับเรดาร์ไปช่องถัดไป
                r += dr
                c += dc
                distance += 1
                
            return False

        # กำหนดทิศทาง (dr = ทิศทางขยับของ Row, dc = ทิศทางขยับของ Column)
        straight = [(-1, 0), (1, 0), (0, -1), (0, 1)] # บน, ล่าง, ซ้าย, ขวา
        diag_up = [(-1, -1), (-1, 1)]                 # เฉียงขึ้นซ้าย, เฉียงขึ้นขวา
        diag_down = [(1, -1), (1, 1)]                 # เฉียงลงซ้าย, เฉียงลงขวา

        # 5. เริ่มยิงเรดาร์ตรวจสอบการถูก Check
        
        # เช็คแนวตรง (หา Rook, Queen)
        for dr, dc in straight:
            if check_ray(dr, dc, ['R', 'Q']):
                print("Success")
                return

        # เช็คทแยงขึ้น (หา Bishop, Queen) 
        for dr, dc in diag_up:
            if check_ray(dr, dc, ['B', 'Q']):
                print("Success")
                return

        # เช็คทแยงลง (หา Bishop, Queen และเปิดโหมดเช็ค Pawn ระยะประชิด)
        for dr, dc in diag_down:
            if check_ray(dr, dc, ['B', 'Q'], check_pawn=True):
                print("Success")
                return

        # ถ้ายิงครบทุกทิศแล้วเรดาร์ไม่เจอศัตรูเลย
        print("Fail")

    except Exception:

        print("Nothing")
        return