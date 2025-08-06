import tkinter as tk

def check_payment():
    try:
        payment = float(entry_payment.get())
        required = energy_kWh * price_per_kWh
        if payment >= required:
            result.set("✅ 交易成功：已轉移能源。")
        else:
            result.set("❌ 付款不足：交易失敗。")
    except ValueError:
        result.set("請輸入有效數字！")

# 參數設定
energy_kWh = 100
price_per_kWh = 0.12

# 建立視窗
window = tk.Tk()
window.title("能源交易模擬器")

tk.Label(window, text="請輸入付款金額（美元）:").pack()
entry_payment = tk.Entry(window)
entry_payment.pack()

tk.Button(window, text="執行交易", command=check_payment).pack()
result = tk.StringVar()
tk.Label(window, textvariable=result, fg="red").pack()

window.mainloop()