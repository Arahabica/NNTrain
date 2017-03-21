rm .coverage
nosetests -i train/* -v --with-coverage
coverage html --include=train/*
echo "> open htmlcov/index.html"
