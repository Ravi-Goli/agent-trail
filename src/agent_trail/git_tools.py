from __future__ import annotations

import subprocess
from pathlib import Path


def run_git(root: Path, *args: str) -> tuple[int, str, str]:
    process = subprocess.run(
        ["git", *args],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    return process.returncode, process.stdout.rstrip("\n"), process.stderr.rstrip("\n")


def get_git_snapshot(root: Path) -> dict[str, object]:
    branch_code, branch, _ = run_git(root, "branch", "--show-current")
    status_code, status, status_err = run_git(root, "status", "--porcelain")
    stat_code, stat, _ = run_git(root, "diff", "--stat")

    files: list[str] = []
    for line in status.splitlines():
        if not line.strip():
            continue
        files.append(line[3:].strip())

    return {
        "branch": branch.strip() if branch_code == 0 else None,
        "files": files,
        "status": status,
        "diff_stat": stat.strip() if stat_code == 0 else "",
        "ok": status_code == 0,
        "error": status_err.strip() if status_code != 0 else "",
    }
