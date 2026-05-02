.PHONY: install test demo

install:
	python3 -m pip install -e .

test:
	python3 -m pytest -q

demo:
	agent-trail init
	agent-trail start "demo AI coding session"
	agent-trail note "Investigated the target files and captured useful context."
	agent-trail decision "Keep the MVP dependency-free for easy installation."
	agent-trail risk "GitHub PR integration is not implemented yet."
	agent-trail snapshot
	agent-trail summary
