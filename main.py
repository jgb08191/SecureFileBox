# main.py

import tkinter as tk
from tkinter import messagebox, scrolledtext
from crypto_utils import encrypt_file, decrypt_file
from file_utils import select_file, get_encrypted_filename, get_decrypted_filename

class SecureFileBoxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SecureFileBox - 파일 암호화 도구")
        self.root.geometry("500x350")
        self.root.resizable(False, False)

        self.selected_file = ""
        
        # 파일 선택 버튼
        self.file_btn = tk.Button(root, text="📂 파일 선택", command=self.select_file)
        self.file_btn.pack(pady=10)

        # 선택한 파일 경로 출력
        self.file_label = tk.Label(root, text="파일이 선택되지 않았습니다.", wraplength=450)
        self.file_label.pack()

        # 비밀번호 입력
        self.pw_label = tk.Label(root, text="비밀번호 입력:")
        self.pw_label.pack(pady=(15, 0))
        self.password_entry = tk.Entry(root, show="*", width=30)
        self.password_entry.pack()

        # 암호화 / 복호화 버튼
        self.encrypt_btn = tk.Button(root, text="암호화", command=self.encrypt)
        self.encrypt_btn.pack(pady=(10, 5))

        self.decrypt_btn = tk.Button(root, text="복호화", command=self.decrypt)
        self.decrypt_btn.pack()

        # 로그 출력 영역
        self.log_text = scrolledtext.ScrolledText(root, height=8, width=60, state='disabled')
        self.log_text.pack(pady=15)

    # 파일 선택 핸들러
    def select_file(self):
        self.selected_file = select_file()
        if self.selected_file:
            self.file_label.config(text=self.selected_file)
            self.log(f"파일 선택됨: {self.selected_file}")
        else:
            self.file_label.config(text="파일이 선택되지 않았습니다.")

    # 암호화 함수
    def encrypt(self):
        if not self.selected_file:
            messagebox.showerror("오류", "먼저 파일을 선택하세요.")
            return
        password = self.password_entry.get()
        if not password:
            messagebox.showerror("오류", "비밀번호를 입력하세요.")
            return
        try:
            encrypt_file(self.selected_file, password)
            self.log("암호화 완료: " + get_encrypted_filename(self.selected_file))
        except Exception as e:
            self.log("암호화 실패: " + str(e))

    # 복호화 함수
    def decrypt(self):
        if not self.selected_file:
            messagebox.showerror("오류", "먼저 파일을 선택하세요.")
            return
        password = self.password_entry.get()
        if not password:
            messagebox.showerror("오류", "비밀번호를 입력하세요.")
            return
        try:
            decrypt_file(self.selected_file, password)
            self.log("복호화 완료: " + get_decrypted_filename(self.selected_file))
        except Exception as e:
            self.log("복호화 실패: " + str(e))

    # 로그 출력 함수
    def log(self, message: str):
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state='disabled')

# GUI 실행
if __name__ == "__main__":
    print("DEBUG: encrypt_file =", encrypt_file)
    print("DEBUG: decrypt_file =", decrypt_file)
    root = tk.Tk()
    app = SecureFileBoxApp(root)
    root.mainloop()
