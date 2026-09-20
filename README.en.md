# Refund Tax Assistant Skill

This installable Codex Skill uses a local refund MCP server to:

- recognize passports and other identity documents;
- list tax bills by issuing country or region code and document number;
- retrieve tax-bill details by refund application number.

## Layout

```text
refund_tax_skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   └── mcp-tools.md
├── scripts/
│   └── encode_document.py
├── skill.json
├── README.md
└── README.en.md
```

## Prerequisite

Run the refund MCP server on the same computer as Codex and make sure this endpoint is available:

```text
http://127.0.0.1:8081/mcp
```

The server must expose `recognize_document`, `list_tax_bills`, and `get_tax_bill_detail`.

## Install

Clone the repository into the Codex skills directory, keeping `SKILL.md` at the top level:

```powershell
git clone https://github.com/houjunhan/refund_tax_skill.git "$env:USERPROFILE\.codex\skills\refund-tax-skill"
```

Restart Codex or start a new task so the client can discover the Skill and its MCP dependency.

## Examples

```text
Use $refund-tax-skill to recognize C:\Documents\passport.jpg and find its tax bills.
List tax bills for country code NPL and document number PA1234567.
Show the details for refund application TR20260001.
```

The helper script uses only the Python standard library:

```powershell
python scripts\encode_document.py C:\Documents\passport.jpg
```

Do not include the generated `fileBase64` value in user-facing responses.

Because the MCP URL uses `127.0.0.1`, every user must run the service locally. This Skill performs recognition and read-only queries; it does not modify refund data.
