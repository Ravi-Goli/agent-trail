from agent_trail.git_tools import get_git_snapshot


def test_git_snapshot_preserves_first_filename_character(tmp_path):
    git_dir = tmp_path / ".git"
    git_dir.mkdir()
    readme = tmp_path / "README.md"
    readme.write_text("before\n", encoding="utf-8")

    # Simulate a repository enough for git status by initializing for real.
    import subprocess

    subprocess.run(["git", "init"], cwd=tmp_path, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "Test User"], cwd=tmp_path, check=True)
    subprocess.run(["git", "add", "README.md"], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-m", "initial"], cwd=tmp_path, check=True, capture_output=True)

    readme.write_text("before\nafter\n", encoding="utf-8")

    snapshot = get_git_snapshot(tmp_path)

    assert "README.md" in snapshot["files"]
    assert "EADME.md" not in snapshot["files"]
