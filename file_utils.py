# file_utils.py

import os
from tkinter import filedialog

# 파일 열기 대화상자: 암호화 대상 파일 선택
def select_file() -> str:
    file_path = filedialog.askopenfilename(
        title="파일 선택",
        filetypes=[("모든 파일", "*.*")]
    )
    return file_path

# 저장 경로 선택 (선택적으로 사용 가능 - 복호화 파일 저장용)
def select_save_location(default_name="decrypted_output") -> str:
    file_path = filedialog.asksaveasfilename(
        title="저장 위치 선택",
        initialfile=default_name,
        defaultextension="",
        filetypes=[("모든 파일", "*.*")]
    )
    return file_path

# ".enc" 확장자 붙이기 (중복 방지)
def get_encrypted_filename(file_path: str) -> str:
    return file_path + ".enc" if not file_path.endswith(".enc") else file_path

# 복호화된 파일 이름 생성 ("example.txt.enc" → "example.txt_decrypted")
def get_decrypted_filename(file_path: str) -> str:
    if file_path.endswith(".enc"):
        return file_path[:-4] + "_decrypted"
    else:
        return file_path + "_decrypted"
