#!/usr/bin/env python3
"""Encode one local document as MCP-ready JSON."""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
from pathlib import Path


def encode_document(path_value: str) -> dict[str, str]:
    path = Path(path_value).expanduser()
    if not path.is_file():
        raise FileNotFoundError(f"Document file does not exist: {path}")

    content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return {
        "fileName": path.name,
        "contentType": content_type,
        "fileBase64": encoded,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Encode a local document for the recognize_document MCP tool."
    )
    parser.add_argument("path", help="Path to the document image or file")
    args = parser.parse_args()
    print(json.dumps(encode_document(args.path), ensure_ascii=False))


if __name__ == "__main__":
    main()

