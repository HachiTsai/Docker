import sqlite3

# 快速測試連接
try:
    conn = sqlite3.connect(':memory:')  # 記憶體資料庫
    print("SQLite連接成功！")
    conn.close()
except sqlite3.Error as e:
    print(f"連接失敗: {e}")
