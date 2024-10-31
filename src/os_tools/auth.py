# 提升权限，创建文件夹 link
import argparse
import ctypes
import os
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


def set_windows_admin_enable():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )


# This creates a symbolic link
def main():
    parser = argparse.ArgumentParser(description="创建符号链接")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-f", "--file", help="从文件读取源路径和目标路径,每行一对,用空格分隔"
    )
    group.add_argument("src", nargs="?", help="源路径")

    parser.add_argument("dst", nargs="?", help="目标路径")
    args = parser.parse_args()

    set_windows_admin_enable()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            for line in f:
                src, dst = line.strip().split(" ")
                os.symlink(src, dst)
                print(f"已创建符号链接: {src} -> {dst}")
    else:
        if not args.src or not args.dst:
            parser.error("使用单个链接模式时，需要同时提供 src 和 dst 参数")
        os.symlink(args.src, args.dst)
        print("符号链接已创建")


if __name__ == "__main__":
    main()

