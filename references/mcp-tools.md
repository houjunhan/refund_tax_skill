# MCP 工具约定

服务地址：`http://127.0.0.1:8081/mcp`

传输方式：Streamable HTTP。客户端需支持 `application/json` 和 `text/event-stream`；Codex 的 MCP 客户端负责传输层协商，技能不要自行发送原始 JSON-RPC 请求。

## `recognize_document`

识别护照或其他证件图片。

必填参数：

- `fileName`：原始文件名，例如 `passport.jpg`。
- `fileBase64`：真实文件字节的 Base64；可以带 `data:` 前缀，但默认传裸 Base64。

可选参数：

- `contentType`：MIME 类型，例如 `image/jpeg`。
- `inputs`：OCR 服务的附加输入；没有明确需求时传空字符串或省略。

不得把本地文件路径作为 `fileBase64` 传入。

## `list_tax_bills`

按证件查询税单列表。

必填参数：

- `countryCode`：证件签发国家或地区代码，例如 `NPL`。
- `documentNumber`：证件号码，例如护照号。

## `get_tax_bill_detail`

查询一张税单的完整详情。

必填参数：

- `refundApplicationNo`：退税申请单号。

## 返回结果

三个工具都返回以下外层结构：

```json
{
  "success": true,
  "code": "...",
  "message": "...",
  "data": {}
}
```

以 `success` 判断业务调用是否成功，并原样保留失败时的 `code` 与 `message`。`data` 的具体字段以服务实际响应为准，不要依赖未声明字段。

