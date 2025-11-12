# app.py
import sys, os # <-- 錯誤 1: 一行導入多個

def main( ): # <-- 錯誤 2: 函數名稱前有空格
    print ("Hello DevSecOps")
    x =    10 # <-- 錯誤 3: = 號周圍空格過多

    unused_variable = "I am not used" # <-- 錯誤 4: 未使用的變數

    # 錯誤 5: 這行太長了，超過 80 個字元
    long_line = "This is a very very very very very very very very very very long line of code that Flake8 will definitely complain about."

if __name__ == "__main__":
    main()