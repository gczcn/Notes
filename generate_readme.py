import os

os.chdir(os.path.dirname(__file__))

# 预设的README
text = [
    '# Notes',
    '用于存放笔记的仓库',
    '',
    '# 生成索引',
    '为更方便地写笔记，此 README 由脚本自动生成',
    '',
    '在 `notes` 文件夹下，每个 `markdown` 文件的开头两行必须遵循以下格式：',
    '```markdown',
    '# Title',
    'yyyy.mm.dd',
    '```',
    '随后在提交前，运行 `generate_readme.py` 自动生成索引',
    '',
    '# 索引',
]

notes = []

# 遍历文件
print('开始遍历笔记文件')
for root, dirs, files in os.walk('notes'):
    for file_name in files:
        if file_name.lower().endswith('.md'):
            file_path = os.path.join(root, file_name)
            with open(file_path) as file:
                title = file.readline()[2:-1]
                time = file.readline()[:-1]
                print(file_path, title, time)
                notes.append([file_path, title, time])

def takeThird(elem):
    return elem[2]

# 排序
notes.sort(key = takeThird, reverse = True)
print('已按时间顺序进行排序')

for i in notes:
    text.append(f'- [{i[1]}]({i[0]}) {i[2]}')

print(text)

# 生成README
with open('README.md', 'w') as file:
    for i in text:
        file.write(f'{i}\n')

print('README 生成完毕')
