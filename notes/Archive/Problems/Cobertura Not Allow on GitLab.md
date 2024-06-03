Taken from [this](https://stackoverflow.com/questions/72164338/property-cobertura-is-not-allowed-gitlab-ci-yml).

As it was mentioned, the `artifacts:report:cobertura` has been deprecated. You can replace the

```yaml
cobertura: cobertura-coverage.xml
```

with the following:

```yaml
coverage_report:
    coverage_format: cobertura
    path: backend/coverage/cobertura-coverage.xml
```