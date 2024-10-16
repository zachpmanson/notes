React doesn't like it when you do updates to other component's state in a `useMemo`. [This is the error that will log in console](https://github.com/facebook/react/issues/18178), this was what fixed it for me.

## Bad

```tsx

function A() {
  const rows = useMemo(() => {
	...
    if (!appliances) return [];
    const newRows = appliances.map<MonitorTableRow>((a) => ({
      id: a.site_appliance.id,
      appliance_id: a.appliance.id,
      sa: a,
      name: a.appliance.title,
      model_num: a.appliance.model_num ?? "",
      max_load: getApplianceLoad(a.appliance, a.appliance.max_load),
    }));
    dispatch(setAppliancesTable(rows));
    return newRows;
  }, [appliances, usageSources, costPerUnit, monitorAppliances, applianceIdToMonitor]);
  ...
  return <></>;
}

function B() {
  const { appliancesTable } = useSelector(state => state.appliances)
  ...
  return <></>
}

```

## Good

```tsx
function A() {
  const rows = useMemo(() => {
	...
    if (!appliances) return [];
    const newRows = appliances.map<MonitorTableRow>((a) => ({
      id: a.site_appliance.id,
      appliance_id: a.appliance.id,
      sa: a,
      name: a.appliance.title,
      model_num: a.appliance.model_num ?? "",
      max_load: getApplianceLoad(a.appliance, a.appliance.max_load),
    }));

    return newRows;
  }, [appliances, usageSources, costPerUnit, monitorAppliances, applianceIdToMonitor]);

  useEffect(() => {
    dispatch(setAppliancesTable(rows));
  }, [rows]);
  ...
  return <></>;
}

function B() {
  const { appliancesTable } = useSelector(state => state.appliances)
  ...
  return <></>
}
```