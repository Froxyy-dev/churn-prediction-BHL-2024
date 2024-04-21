.PHONY:
    update-requirements

update-requirements:
	pip list --format=freeze > requirements.txt