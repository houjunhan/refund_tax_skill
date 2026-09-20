# 退税税单助手 Skill

这是一个可安装的 Codex Skill，通过本地退税 MCP 服务完成：

- 护照或其他证件识别；
- 按证件签发国家或地区代码和证件号码查询税单列表；
- 按退税申请单号查询税单详情。

## 文件结构

```text
refund_tax_skill/
├── SKILL.md                    Skill 入口与工作流
├── agents/
│   └── openai.yaml             Codex 展示信息与 MCP 依赖
├── references/
│   └── mcp-tools.md            MCP 工具参数和返回约定
├── scripts/
│   └── encode_document.py      本地文件 Base64 编码工具
├── skill.json                  展示元数据
├── README.md
└── README.en.md
```

## 前置条件

在使用 Skill 的同一台电脑上启动退税 MCP 服务，并保证以下地址可访问：

```text
http://127.0.0.1:8081/mcp
```

服务应提供以下 MCP 工具：

- `recognize_document`
- `list_tax_bills`
- `get_tax_bill_detail`

## 安装

将仓库克隆到 Codex 的技能目录，并让 `SKILL.md` 位于安装目录第一层：

```powershell
git clone https://github.com/houjunhan/refund_tax_skill.git "$env:USERPROFILE\.codex\skills\refund-tax-skill"
```

然后重启 Codex 或新开任务，让客户端重新发现 Skill 和 MCP 依赖。

## 使用示例

显式调用：

```text
使用 $refund-tax-skill 识别 C:\Documents\passport.jpg，并查询关联税单。
```

也可以自然提问：

```text
帮我识别这张护照并查询退税税单。
查询国家代码 NPL、证件号 PA1234567 的税单。
查询退税申请单号 TR20260001 的详情。
```

## 本地检查

证件编码脚本只依赖 Python 标准库：

```powershell
python scripts\encode_document.py C:\Documents\passport.jpg
```

输出 JSON 可直接作为 `recognize_document` 的参数。不要把其中的 `fileBase64` 展示在面向用户的回复中。

## 注意事项

- `127.0.0.1` 指运行 Codex 的本机。其他用户安装后，也需要在自己的电脑上运行该 MCP 服务。
- 证件和税单信息属于敏感数据，只处理用户在当前任务中指定的文件和记录。
- 本 Skill 只执行查询和识别，不修改退税业务数据。
