from util import *

mark = ["〇：", "🔥：", "👦："]


# 评论，3段
# 直接读3段进来，保留第一段和第三段，去掉第二段。第一和第三的> 去掉。
# 如果第一段开头不是 >，删掉这一句，从这一句开始判断是否符合三段式。

def process_comment_text(filename, tag):
    with open(filename, 'r') as f:
        datas = f.readlines()

    new_datas = []
    for each in datas:
        if len(each.strip()) > 0:
            new_datas.append(each)
    datas = new_datas

    res = []
    i = 0
    while i < len(datas):
        temp_data = datas[i:min(i + 3, len(datas))]
        if isSanDuan(temp_data) == False:
            i = i + 1
        else:
            if len(res) != 0:
                temp_content = "\n"
            else:
                temp_content = ""

            temp_content += "标签：" + tag + "\n"
            temp_content += mark[0] + temp_data[0][1:].strip() + "\n"
            temp_content += mark[1] + temp_data[2][2:-3].strip() + "\n"
            temp_content += mark[2] + author.strip() + "，" + book.strip() + "\n"
            temp_content += "结束\n"
            res.append(temp_content)
            print(temp_content)
            i = i + 1
    return res


# 微信标准导入到flomo
# 去掉评论，只要标注
# weixin阅读评论导入到flomo
def process_highlight_text(filename):
    with open(filename, 'r') as f:
        datas = f.readlines()

    new_datas = []
    for each in datas:
        if len(each.strip()) > 0:
            new_datas.append(each)
    datas = new_datas

    res = []
    i = 0
    while i < len(datas):
        if datas[i].startswith("**") == False:
            i = i + 1
        else:
            j = i + 1
            while j < len(datas) and datas[j].startswith("**"):
                j = j + 1
            temp_data = datas[i:min(j, len(datas))]
            temp_data = map(lambda x: str(x).replace("**", "").strip(), temp_data)

            if len(res) != 0:
                temp_content = "\n"
            else:
                temp_content = ""

            temp_content += "标签：" + tag + "\n"
            temp_content += mark[0] + "".join(temp_data) + "\n"  # 原文
            temp_content += mark[1] + "\n"  # 想法
            temp_content += mark[2] + author.strip() + "，" + book.strip() + "\n"  # 其他信息
            temp_content += "结束\n"
            res.append(temp_content)

            print(temp_content)
            i = j

    return res


if __name__ == "__main__":
    tag = "#领域/知识管理/卡片笔记"
    author = "申克阿伦斯，陈琳译"
    book = "《卡片笔记写作法》"

    texts = process_highlight_text("highlight.txt")
    for content in texts:
        write2_file(content, "highlight_res.txt")

    texts = process_comment_text("comment.txt", tag)
    for content in texts:
        write2_file(content, "comment_res.txt")
