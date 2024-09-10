When writing unit/integration tests in Python, the general pattern is to use `unittest.mock.patch`.  This is great, but you need to be careful about the namespaces. 

```python
# tests.py
from path.to.funcB
from unittest.mock import patch
# assume funcB calls the somepypipackage.funcA

@patch("somepypipackage.funcA")
def test_funcB(funcA):
	funcA.return_value = 3
	assert funcB() == "correct_value"
```

This will only mock `funcA` calls within the scope of  `tests.py`.  funcB is in a different namespace so calls `funcB` makes to `funcA` will not be mocked  To ensure `funcA` calls are mocked properly specifically write the namespace it needs to be mocked within

```python
# tests.py
from path.to.funcBfile import funcB
from unittest.mock import patch

# assume funcB calls the somepypipackage.funcA

@patch("path.to.funcBfile.funcA")
def test_funcB(funcA):
	funcA.return_value = 3
	assert funcB() == "correct_value"
```