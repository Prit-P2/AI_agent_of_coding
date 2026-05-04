---
name: session-logger
description: Saves all user prompts and shell commands executed by Gemini CLI in the current session to a .txt file. Use this when the user wants to export their session history or keep a log of actions taken.
---

# Session Logger

This skill allows Gemini CLI to extract and save the command history of the current session to a readable text file.

## Workflow

When the user asks to "save session commands" or "export history to txt":

1. **Locate the Current Session File**:
   - The session files are stored in the project's temporary directory, typically under `~/.gemini/tmp/<project-slug>/chats/`.
   - Run `ls -lt ~/.gemini/tmp/*/chats/*.jsonl | head -n 1` to find the most recent session file.

2. **Run the Extraction Script**:
   - Use the provided script `scripts/extract_commands.py` to parse the session file.
   - Example: `python scripts/extract_commands.py <path_to_jsonl> > session_history.txt`

3. **Confirm to User**:
   - Inform the user that the commands have been saved to the specified file.

## Script Usage

The `extract_commands.py` script identifies `user` messages and `gemini` `run_shell_command` tool calls to reconstruct the sequence of actions.

```bash
python scripts/extract_commands.py path/to/session.jsonl
```
