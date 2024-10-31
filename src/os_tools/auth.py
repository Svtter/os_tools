# 提升权限，创建文件夹 link
import ctypes
import os
import sys

src = r"E:\work"
dst = r"C:\Users\svtte\Documents\work"


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


def windows():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )


# This creates a symbolic link
def main():
    windows()
    os.symlink(src, dst)
    print("symlink created")


if __name__ == "__main__":
    main()
