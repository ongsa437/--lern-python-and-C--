# เกม XO (Tic Tac Toe) โดยใช้ List

# 1) สร้างกระดาน XO เป็น list
board = [" " for _ in range(9)]  
# " " คือช่องว่าง, ใช้ 9 ช่อง (index 0-8) แทนกระดาน XO 3x3


# 2) ฟังก์ชันแสดงกระดาน
def print_board():
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")


# 3) ฟังก์ชันตรวจสอบผู้ชนะ
def check_winner(player):
    # เงื่อนไขการชนะ (index ของช่องบนกระดาน)
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # แนวนอน
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # แนวตั้ง
        [0, 4, 8], [2, 4, 6]               # แนวทแยง
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


# 4) ฟังก์ชันตรวจว่ากระดานเต็มหรือไม่ (เสมอ)
def is_draw():
    return " " not in board


# 5) เริ่มเกม
current_player = "X"   # เริ่มจาก X ก่อน

while True:
    print_board()
    try:
        move = int(input(f"Player {current_player}, เลือกตำแหน่ง (1-9): ")) - 1
        # ลบ 1 เพราะผู้ใช้เลือก 1-9 แต่ list ใช้ index 0-8

        if board[move] != " ":
            print("❌ ช่องนี้ถูกเลือกไปแล้ว ลองใหม่อีกครั้ง")
            continue
    except (ValueError, IndexError):
        print("⚠️ กรุณาใส่ตัวเลข 1-9 เท่านั้น")
        continue

    # วางสัญลักษณ์ในกระดาน
    board[move] = current_player

    # ตรวจสอบผลลัพธ์
    if check_winner(current_player):
        print_board()
        print(f"🎉 ผู้เล่น {current_player} ชนะแล้ว!")
        break

    if is_draw():
        print_board()
        print("🤝 เกมเสมอ!")
        break

    # สลับผู้เล่น
    current_player = "O" if current_player == "X" else "X"
