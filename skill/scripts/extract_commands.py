import json
import sys
import os

def extract_commands(jsonl_path):
    commands = []
    with open(jsonl_path, 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get('type') == 'user':
                    for content in data.get('content', []):
                        if 'text' in content:
                            commands.append(f"[USER]: {content['text']}")
                elif data.get('type') == 'gemini':
                    tool_calls = data.get('toolCalls', [])
                    for call in tool_calls:
                        name = call.get('name')
                        args = call.get('args', {})
                        arg_str = ", ".join([f"{k}={v}" for k, v in args.items()])
                        commands.append(f"[TOOL] {name}({arg_str})")
            except json.JSONDecodeError:
                continue
    return commands

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_commands.py <session_jsonl_path>")
        sys.exit(1)
    
    path = sys.argv[1]
    if not os.path.exists(path):
        print(f"File not found: {path}")
        sys.exit(1)
        
    cmds = extract_commands(path)
    for c in cmds:
        print(c)
