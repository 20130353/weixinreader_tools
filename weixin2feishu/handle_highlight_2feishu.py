def open_file(file_name):
    # 打开一个文件
    fout = open("output.txt", "w")

    f = open(file_name)  # 返回一个文件对象
    lines = f.readlines()  # 调用文件的 readline()方法
    f.close()
    for each in lines:
        if each.startswith(">") or each.startswith("=="):
            continue
        if len(each.strip()) == 0:
            continue
        print(each.strip() + "\n")
        fout.write(each.strip().replace("**","") + "\n")
        # 关闭打开的文件
    fout.close()


if __name__ == '__main__':
    open_file("highlight.md")
