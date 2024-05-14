inspect() {
  if [ "$1" -ne 0 ]; then
    fails="${fails} $2"
  fi
}

echo "Starting Services"
docker-compose -f docker-compose.yml up --exit-code-from  selenium --build

inspect $? e2e

echo "Stopping Services"
docker-compose -f docker-compose.yml down -v

if [ -n "${fails}" ]; then
  echo "Tests failed ! (exit code ${fails})"
  exit 1
else
  echo "Tests Passed"
  exit 0
fi
