# Session Logger Skill for Gemini CLI

A specialized skill for [Gemini CLI](https://github.com/google/gemini-cli) that extracts and saves your current session's command history into a clean, readable text file.

## Features

- **Automated Extraction**: Captures all user prompts and shell commands executed by the agent.
- **Readable Format**: Saves history to a `.txt` file for easy review or documentation.
- **Privacy Focused**: Only processes the local session log files.

## Installation

To use this skill in your Gemini CLI project:

1. Clone or copy this directory into your project's `.gemini/skills/` folder:
   ```bash
   mkdir -p .gemini/skills/
   cp -r session-logger .gemini/skills/
   ```
2. Activate the skill in your session:
   > "Use the session-logger skill"

## Usage

Once activated, you can ask Gemini CLI to:
- "Save my session history"
- "Export commands to text"
- "Log this session"

The skill will locate the latest session JSONL file and run the extraction script to generate `session_history.txt`.

## Project Structure

- `SKILL.md`: The definition and instructions for the Gemini CLI agent.
- `scripts/extract_commands.py`: The core logic for parsing JSONL session logs.
- `assets/`: Folder for supporting images or diagrams.
- `references/`: Documentation and external links.

## License

MIT
