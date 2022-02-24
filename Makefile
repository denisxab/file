auto_doc:
	sphinx-autobuild -b html ./docs/source ./docs/build/html


# Создать файл зависимостей для Read The Docs
req:
	poetry export -f requirements.txt --output ./docs/requirements.txt --dev --without-hashes;